import pygeoip 
import ipaddress
g = pygeoip.GeoIP('GeoLiteCity.dat') 
def geoip(iptext):
   try:
      return ipaddress.ip_address(iptext)
   except:
      print("Это не IP-адрес")

iptext = input("Введите IP: ")
geoip
g.record_by_addr(iptext)
rec = g.record_by_addr(iptext)
x=(f'Код страны: {rec["country_code3"]}\n')
x+=(f'Название страны: {rec["country_name"]}\n')
x+=(f'Код региона: {rec["region_code"]}\n')
p = rec['city']
if p != 'Research' or 'None':
   x+=(f'Город: {rec["city"]}\n')
else:
   x+=(f'Город не определен\n')
x+=(f'Широта: {rec["latitude"]}\n')
x+=(f'Долгота: {rec["longitude"]}\n')
p = rec['dma_code']
if p != 0:
   x+=(f'Код организации: {rec["dma_code"]}\n')
p = rec['postal_code']
if p != 0:
   x+=(f'Почтовый индекс: {rec["postal_code"]}\n')
p = rec['time_zone']
if p != 0:
   x+=(f'Временная зона: {rec["time_zone"]}\n')
print(x)