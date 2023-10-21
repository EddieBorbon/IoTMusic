# Proyecto IoTMusic - Teleperformance de Música y Tecnología

Este proyecto utiliza MicroPython para integrar una fotoresistencia con la tecnología IoT (Internet de las cosas) y música, enviando los valores de una fotoresistencia a través de UDP a un servidor y luego controlar parámetros sonoros en pure data.

## Requisitos

- Hardware: Placa ESP32, Sensores (fotoresistencia) y actuadores (LED).
- Visual Studio.
- NodeJs.
- MicroPython.

## 1. Configuración de Placa ESP32

Para comenzar a trabajar con la placa ESP32 y este proyecto, sigue estos pasos para configurar los controladores:

1. **Descargar el Controlador:**
   - Visita el sitio web del fabricante de tu placa ESP32 y busca la sección de descargas o soporte. Puedes encontrar controladores USB en el [sitio oficial de Espressif](https://www.espressif.com/en/support/download/all) si estás utilizando un módulo de Espressif.

2. **Instalar el Controlador:**
   - Descarga el controlador adecuado para tu sistema operativo (Windows, macOS, o Linux).
   - Sigue las instrucciones de instalación proporcionadas por el fabricante.

3. **Conectar la Placa ESP32:**
   - Conecta la placa ESP32 a tu computadora mediante un cable USB.

4. **Verificar la Conexión:**
   - Abre el Administrador de Dispositivos en Windows o utiliza comandos como `ls /dev` en Linux/macOS para verificar si la placa ESP32 aparece correctamente.

5. **Configuración en Visual Studio Code con Pymakr:**
   - Asegúrate de tener la extensión Pymakr instalada en Visual Studio Code.
   - Abre tu proyecto y selecciona el puerto COM correcto para tu ESP32 en la configuración de Pymakr.

6. **Reiniciar Visual Studio Code:**
   - Reinicia Visual Studio Code después de configurar los controladores y el puerto COM.

Para una guía visual detallada sobre cómo configurar tu placa ESP32 y Visual Studio Code con la extensión Pymakr, puedes consultar el siguiente video tutorial:

[![Configuración de Placa ESP32 con Pymakr](https://img.youtube.com/vi/YOeV14SESls/0.jpg)](https://www.youtube.com/watch?v=YOeV14SESls&t=186s)

Asegúrate de seguir los pasos y ajustar la configuración según las necesidades de tu proyecto. Si tienes alguna pregunta específica después de ver el video o necesitas más ayuda, no dudes en preguntar en nuestro [foro de soporte](#enlace-al-foro) o [comunidad en línea](#enlace-a-comunidad).

## 2.Configuración de la Red WiFi

Antes de ejecutar el script en tu dispositivo ESP32, asegúrate de configurar correctamente la conexión WiFi. Sigue estos pasos:

1. Descarga la carpeta 1. Configurar RED Wifi, carga los scripts en un proyecto de Visual Studio.

2. Busca la sección de **Configuración de WiFi** en el código. Debería verse algo así:

    ```python
    # Configuración de WiFi
      SSID = 'WRITE YOUR NAME NETWORK HERE'
      PASS = 'WRITE YOUR PASSWORD NETWORK HERE'
      CONNECTING_TRIES = 3
    ```

    Reemplaza `'SSID'` y `'PASS'` con los detalles de tu red WiFi.

3. Guarda los cambios en el archivo.

4. Presiona el botón de carga (Upload) en Pymakr para cargar el script en tu dispositivo.

5. Realiza un reinicio del dispositivo (hard reset) para ejecutar el script. Puedes hacer esto a través de los botones proporcionados por Pymakr o según las instrucciones específicas de tu placa.
   
Si encuentras problemas de conexión, asegúrate de que los detalles de la red WiFi sean correctos y de que la placa ESP32 está en un rango de señal adecuado.

En consola te parecer un mensaje como el siguiente

```python
Uploading and running the script...
Upload and run complete!
Connecting to "YOUR NETWORK"
Connection Successfully to "YOUR NETWORK"
Executing code
Connected to 192.168.2.2:8888
MicroPython v1.21.0 on 2023-10-05; Generic ESP32 module with ESP32
```

### Sugerencia:
Si no conoces tu IP, realiza el siguiente procedimiento:

## Configuración del Servidor UDP

Antes de ejecutar el script, puedes obtener dinámicamente la dirección IP del servidor UDP utilizando el comando `ipconfig` en la terminal de Windows. Sigue estos pasos:

1. **Abre la terminal de Windows:**
   - Busca "cmd" o "Símbolo del sistema" en el menú de inicio y ábrelo.

2. **Ejecuta el comando `ipconfig` para obtener información sobre las interfaces de red:**
   - Utiliza el siguiente comando:

   ```plaintext
   > ipconfig

Busca la sección correspondiente a tu interfaz de red activa, generalmente "Adaptador de Ethernet" o "Adaptador de Wi-Fi". Allí encontrarás tu "Dirección IPv4". Anota esta dirección IP.

Adaptador de Ethernet:
...
   ```plaintext
   Dirección IPv4. . . . . . . . . . . . . . : xxx.xxx.xxx.xxx
   ```
Configura el servidor UDP con la dirección IP anotada:

En tu script, utiliza la dirección IP que has anotado para la conexión al servidor UDP.
```plaintext
pd_host = 'xxx.xxx.xxx.xxx'  # Utiliza la dirección IP anotada
pd_port = 8888
pd.connect((pd_host, pd_port))
```
### 3. Recibir Datos de un Sensor

En este paso, configuraremos la placa ESP32 para leer datos de un sensor de fotorresistencia. Sigue estos pasos:

1. **Configura el Sensor:**
   - Conecta el sensor de fotorresistencia al pin analógico 36 de la placa ESP32.

2. **Ver Resultados:**
   - Ejecuta el código y observa los valores de la fotorresistencia que se imprimen en la consola.

Con estos pasos, tu placa ESP32 estará configurada para recibir datos de un sensor y enviarlos al servidor.

![Logo de Mi Proyecto](https://github.com/EddieBorbon/IoTMusic/main/Images/esp32-ldr-wiring.jpg)
![Logo de Mi Proyecto](https://github.comEddieBorbon/IoTMusic/main/Images/ESP32-Pinout.jpg)

## Configuración de la Placa

1. Conecta el potenciómetro al pin correspondiente en tu dispositivo.
2. Ajusta la dirección IP y el puerto del servidor en el código.

## Uso

1. Carga el script en tu dispositivo con MicroPython.
2. Ejecuta el script y observa cómo se envían los valores del potenciómetro al servidor.

## Contribución

Si deseas contribuir a este proyecto en IoTMusic:
- Realiza un fork del repositorio.
- Crea una rama para tu nueva característica o corrección de errores.
- Envía una solicitud de extracción.

## Licencia

Este proyecto está bajo la Licencia [nombre de la licencia].

## Contacto

Para preguntas o comentarios, contáctame en [tu dirección de correo electrónico] o [tus redes sociales].
