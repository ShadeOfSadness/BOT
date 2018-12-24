# -*- coding: utf-8 -*-
import pygeoip 
import ipaddress
import config
import telebot
bot = telebot.TeleBot(config.token)
g = pygeoip.GeoIP('GeoLiteCity.dat')

@bot.message_handler(func=lambda m: True)
def echo_ip(message):
        try:
            ipaddress.ip_address(message.text)   
        except:   
            bot.send_message(message.chat.id, 'Это не IP-адрес') 
        try:
            rec =g.record_by_addr(message.text)
            x=(f'Код страны: {rec["country_code3"]}\n')
        except:
            bot.send_message(message.chat.id, 'В базе данных данного IP нет')
        try:        
          x+=(f'Название страны: {rec["country_name"]}\n')
          p = rec['region_code']
          if p != None:
            x+=(f'Код региона: {rec["region_code"]}\n')
          p = rec['city']
          if p != 'Research' and p!=None:
            x+=(f'Город: {rec["city"]}\n')
          else:
            x+=(f'Город не определен\n')
          x+=(f'Широта: {rec["latitude"]}\n')
          x+=(f'Долгота: {rec["longitude"]}\n')
          p = rec['dma_code']
          if p != 0:
            x+=(f'Код организации: {rec["dma_code"]}\n')
          p = rec['postal_code']
          if p != 0 and None:
            x+=(f'Почтовый индекс: {rec["postal_code"]}\n')
          p = rec['time_zone']
          if p != 0:
            x+=(f'Временная зона: {rec["time_zone"]}\n')
          bot.send_message(message.chat.id, x)
          
        except:
                bot.send_message(message.chat.id, "Некоторая информация отсутствует")

    
if __name__ == '__main__':
    bot.polling(none_stop=True)