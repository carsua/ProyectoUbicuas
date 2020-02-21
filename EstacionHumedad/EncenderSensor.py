
#Importamos las librerias
from time import sleep
import http.client, urllib
from dhtxx import DHT11, DHT22

# ¡Ajuste el puerto GPIO 

dht11 = DHT11(14)
dht11_2 = DHT11(16)

#ciclo While
while True:
 
 r = dht11.get_result(max_tries=10)
 
 
 if r:
  print('Humedad Superior: {1:0.1f} %'.format(r[0], r[1]))
  
  #CONEXION A LA NUBE THINGSPEAK
  params = urllib.parse.urlencode({'field1': r[0],'field2': r[1], 'key':'S5B184KONC3ZGTPF'})
  headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
  conn = http.client.HTTPConnection("api.thingspeak.com:80")

  #INFORMACION DE ERROR POR MEDIO DE EXCEPCIONES TRY
  try:
   conn.request("POST", "/update", params, headers)
   response = conn.getresponse()
   print(response.status, response.reason)
   data = response.read()
   conn.close()
  except:
   print("Conexion Fallida")
  sleep(2)
 else:
  print('Error al obtener resultado!')
 
 r2 = dht11_2.get_result(max_tries=10)
 
 if r2:
  print('Humedad Inferior: {1:0.1f} %'.format(r2[1]))
  
  #CONEXION A LA NUBE THINGSPEAK
  params = urllib.parse.urlencode({'field3': r2[1], 'key':'550P1PN9KGXZAWH3'})
  headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
  conn = http.client.HTTPConnection("api.thingspeak.com:80")

  #INFORMACION DE ERROR POR MEDIO DE EXCEPCIONES TRY
  try:
   conn.request("POST", "/update", params, headers)
   response = conn.getresponse()
   print(response.status, response.reason)
   data = response.read()
   conn.close()
  except:
   print("Conexion Fallida")
  sleep(2)
 else:
  print('Error al obtener resultado!')
 
