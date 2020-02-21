# ProyectoUbicuas

ESTACIÓN DE BAJO COSTO PARA HUMEDAD

PRESENTADO A: PhD. GUSTAVO RAMIREZ GONZALEZ
POR: CARLOS ALBERTO SUAREZ MUÑOZ

1.Propósito del proyecto

El presente proyecto tiene como objetivo proponer una estación de bajo costo para medir la humedad relativa del ambiente en diferentes puntos sobre cultivos agrícolas con ayuda del paradigma del Internet de las cosas(IOT) el cual permite la conexión entre objetos para capturar datos, los cuales a través de servicios en la nube se almacenan y procesan, para luego servir de insumos a herramientas de agricultura de precisión [1] permitiendo el monitoreo de múltiples variables en tiempo real y así ayudar a la toma de decisiones buscando favorecer la producción agrícola [2]. No medir la humedad relativa en los cultivos agrícolas hace que no existan datos suficientes que permitan realizar procesos de pronostico de infestación e incidencia de algunas enfermedades como ocurre en el cultivo café[3]. La estación de bajo costo para medir la humedad relativa que se propone a través de este documento está integrado con la tecnología Raspberry pi 3, la placa de pruebas, sensores de humedad DTH11 y los datos en tiempo real que se pueden obtener en línea desde el middleware llamado thingspeak.com.

2.Problema a resolver

Las observaciones meteorológicas sirven de insumo en la agricultura de precisión permitiendo que la gestión agrícola sea mas selectiva y efectiva en el uso de insumos y toma de decisiones para aumentar la productividad y ayudar al control de plagas y enfermedades [4]. La humedad relativa hace parte de las múltiples variables que pueden ser medidas dentro de un cultivo a través de estaciones IOT e incide en la producción y presencia de enfermedades en los cultivos. Es de gran importancia en el cultivo de Café llevar a cabo el monitoreo de su comportamiento ya que esta variable bajo determinados valores puede favorecer el crecimiento y aparición de plagas y enfermedades como: La roya cuando el valor es superior al 85% [5], el ojo de gallo cuando el valor supera 80% [6] y la broca con un valor de humedad relativa de un 90% a 100% [6], las cuales generan perdidas económicas debido al control necesario para le manejo, perdidas de cosechas, baja productividad y baja calidad del grano lo que ocasiona perdidas en la producción del cultivo de Café, para el caso de la roya pueden alcanzar un 31% [7], en el ojo de gallo entre 20% a 30%[8] y en cultivos con presencia de roya se genera baja producción y calidad del Café [9]. 

Ademas una estación climática que permita medir la humedad relativa requiere inversión económica alta por parte del caficultor que debido a sus condiciones económicas y sociales no puede realizar ya que los bajos margenes de ganancia producto de su actividad no lo permite, así es de gran utilidad proponer una estación de bajo costo que permita capturar datos de humedad en el cultivo de Café, con lo cual se facilita la su adopción permitiendo la recolección de datos de humedad relativa en varias regiones del departamento del Cauca para que expertos en agricultura de precisión cuenten con datos suficientes que permitan el uso de herramientas tecnológicas de análisis de datos climáticos para el pronostico de infestación e incidencia de plagas y enfermedades con lo cual pueden sugerir medidas de prevención o control mas eficientes y eficaces.

3.Hadware

Para el desarrollo de la estación de bajo costo para medir la humedad se requieren los siguientes materiales:

a)Raspberry Pi 3, la cual tiene las siguientes especificaciones:

  CPU Quadcom 1.2MHz Broadcom BCM2837 64bit.
  1 GB de RAM.
  BCM43438 LAN inalámbrica y Bluetooth de baja energía (BLE) a bordo.
  100 Base Ethernet.
  GPIO extendido de 40 pines.
  4 puertos USB 2.
  Salida estéreo de 4 polos y puerto de video compuesto.
  HDMI de tamaño completo.
  Puerto de cámara CSI para conectar una cámara Raspberry Pi.
  Puerto de pantalla DSI para conectar una pantalla táctil Raspberry Pi.
  Puerto Micro SD para cargar su sistema operativo y almacenar datos.
  Fuente de alimentación micro USB conmutada actualizada hasta 2.5A.

b)Tarjeta micro SD 32 GB
c)Conector de corriente Micro USB (2.1 A)
d)6 Jumpers hembra
e)2 Sensores de humedad DTH11

El DHT11 es un sensor que proporciona una salida de datos digital. 	Entre sus ventajas podemos mencionar el bajo coste y el despliegue 	de datos digitales. Esto supone una gran ventaja frente a los sensores 	del tipo análogo, algunas de sus características son: 

Tensión de funcionamiento: 3v – 5.5v.
Rango de valores del 20% al 90% de Humedad Relativa.
Rango de valores de 0ºC a 50ºC de Temperatura.
Resolución de lectura: 1, es decir, nos proporciona tan sólo valores 	enteros tanto de humedad relativa como de temperatura.
Precisión de la humedad relativa: ±5%.
Precisión de la temperatura: ±2ºC.

f)Computador(escritorio o portátil) con las siguientes especificaciones:  Sistema Operativo: Windows 10.
RAM 6GB o superior.
Disco duro 500GB o superior.

Nota: Ademas de tener disponible de un TV o Monitor con entrada HDMI, Cable HDMI, Teclado y Mouse, el cual se usara solo para configuración inicial



4.Software

Para el desarrollo de la estación de bajo costo para medir la humedad relatica se usan las siguientes tecnologías:

a)Thingspeak.com: es una aplicación y API de Internet de las Cosas (IoT) de código abierto para almacenar y recuperar datos de cosas usando el protocolo HTTP y MQTT a través de Internet o a través de una red de área local. ThingSpeak permite la creación de sensores aplicaciones de registro, aplicaciones de seguimiento de ubicación y una red social de cosas con actualizaciones de estado. Pagina oficial de registro: https://thingspeak.com/users/sign_up 
b)RealVNC: es una empresa que ofrece software de acceso remoto. El software consta de una aplicación de servidor (VNC Server) y de cliente (VNC Viewer) para el protocolo Virtual Network Computing (VNC) para controlar la pantalla de otra computadora de forma remota. Pagina de registro https://manage.realvnc.com/es/ link de descarga para VNC Viwer https://www.realvnc.com/en/connect/download/viewer/windows/ 
c)Wamp server: es un entorno de desarrollo web de Windows. Le permite crear aplicaciones web con Apache2, PHP y una base de datos MySQL. Además tiene PhpMyAdmin que le permite administrar fácilmente sus bases de datos. Enlace para descargar http://www.wampserver.com/en/ de acuerdo a la arquitectura windows. 
d)Raspbian: es el sistema operativo oficial para todos los modelos de Raspberry Pi. Link de descarga del archivo NOOBS que viene pre instalado para copiar y pegar en la tarjeta micro SD: https://www.raspberrypi.org/downloads/ 
e)Codigo Python: Es necesario contar con un par de archivos escritos en Python para leer los datos del sensor DTH11, los cuales están a disposición en https://drive.google.com/drive/folders/1hJI96TAB_yY0M6b12yx3wPbYr-E6bg9r?usp=sharing 

5.Modelo Case 3D

Es necesario proteger tanto el sensor y los pines con sus conexiones a que sean manipuladas o afectadas por la exposición al exterior para lo cual se opta por un case para DTH11 el cual fue diseñado por J.T. bajo licencia CC que nos permite el uso en nuestro proyecto.  

Este case permite que el sensor capture la humedad del aire y ademas ofrece la facilidad de fijarlo sobre una superficie.

6.Arquitectura 

En esta arquitectura  diferentes estaciones instaladas dentro del cultivo tienen dos sensores lo que nos permite realizar mediciones a 2 diferentes alturas brindando mas información sobre la humedad relativa tanto en la parte media de cada planta y su parte superior, esta información captada por los sensores es enviada a la Raspberry la cual una vez procesa los datos con ayuda del lenguaje Phyton los envía por medio de una petición POST bajo el protocolo HTTP a ThingSpeak que los almacena en la nube y pone a disposición para su consumo por medio de una API para ser consumidos por un navegador web.

Referencias

[1]	W.-L. Chen et al., “AgriTalk: IoT for Precision Soil Farming of Turmeric Cultivation,” IEEE Internet of Things Journal, vol. 6, no. 3, pp. 5209–5223, Jun. 2019.
[2]	Murugan Krishnan and Ruslaimi Abd.Kadir, “Smart IOT Agricultural Kit for Precision Farming,” Politeknik & Kolej Komuniti Journal of Engineering and Technology, vol. 4, no. 1, pp. 82–90, 2019.
[3]	Consuelo Montes Rojas, O. Armando, and Roberto Amilcar Cadena, “Infestación e incidencia de broca, roya y mancha de hierro en cultivo de café del departamento del Cauca,” Biotecnología en el Sector Agropecuario y Agroindustrial: BSAA, vol. 10, no. 1, pp. 98–108, 2012.
[4]	R. Finger, S. M. Swinton, N. El Benni, and A. Walter, “Precision Farming at the Nexus of Agricultural Production and the Environment,” Annual Review of Resource Economics, vol. 11, no. 1, pp. 313–335, Oct. 2019.
[5]	C. A. Rivillas Osorio, C. A. Serna Giraldo, M. A. Cristancho Ardila, and A. L. Gaitán Bustamante, “La Roya del Cafeto en Colombia Impacto, manejo y costos del control,” Feb. 2011.
[6]	R. A. Villarreyna Acuña, “Efecto de la sombra sobre las plagas y enfermedades, a través del microclima, fenología y estado fisiológico del cafeto,” Jun. 2016.
[7]	J. Avelino et al., “The coffee rust crises in Colombia and Central America (2008–2013): impacts, plausible causes and proposed solutions,” Food Security, vol. 7, no. 2, pp. 303–321, Mar. 2015.
[8]	C. A. Rivillas-Osorio and Á. M. Castro-Toro, “Ojo de Gallo o Gotera del Cafeto (Omphalia flavida): Enfermedad severa en algunas regiones cafeteras de Colombia, asociada a eventos climáticos fríos como ‘La Niña,’” Jul. 2011.
[9]	A. E. BUSTILLO PARDEY, “Una revisión sobre la broca del café, Hypothenemus hampei (Coleoptera: Curculionidae: Scolytinae), en Colombia,” Revista Colombiana de Entomología, vol. 32, no. 2: 101-116, Oct. 2006.
