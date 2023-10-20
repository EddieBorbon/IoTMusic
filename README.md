# Proyecto IoTMusic - Teleperformance de Música y Tecnología

Este proyecto utiliza MicroPython para integrar un potenciómetro con la tecnología IoT (Internet de las cosas) y música, enviando los valores del potenciómetro a través de UDP a un servidor.

## Requisitos

- Hardware: Placa ESP32, Sensores y actuadores.
- Visual Studio.
- NodeJs
- MicroPython: Asegúrate de tener MicroPython instalado en tu dispositivo.

## Configuración de Placa ESP32

Para comenzar a trabajar con la placa ESP32 y este proyecto, sigue estos pasos para configurar los controladores:

1. **Descargar el Controlador:**
   - Visita el sitio web del fabricante de tu placa ESP32 y busca la sección de descargas o soporte. Puedes encontrar controladores USB en el [sitio oficial de Espressif](https://www.espressif.com/en/support/download/all) si estás utilizando un módulo de Espressif.

2. **Instalar el Controlador:**
   - Descarga el controlador adecuado para tu sistema operativo (Windows, macOS, o Linux).
   - Sigue las instrucciones de instalación proporcionadas por el fabricante.

3. **Conectar la Placa ESP32:**
   - Conecta la placa ESP32 a tu computadora mediante un cable USB.
   - Asegúrate de que la placa esté alimentada correctamente.

4. **Verificar la Conexión:**
   - Abre el Administrador de Dispositivos en Windows o utiliza comandos como `ls /dev` en Linux/macOS para verificar si la placa ESP32 aparece correctamente.

5. **Configuración en Visual Studio Code con PlatformIO:**
   - Abre tu proyecto en Visual Studio Code.
   - Asegúrate de tener la extensión PlatformIO instalada.
   - En la barra lateral, selecciona "PlatformIO" y luego "Devices" para ver si la placa ESP32 está detectada.

6. **Seleccionar el Puerto COM:**
   - Si estás utilizando Windows, ve a "Administrador de Dispositivos" y busca el puerto COM asignado a tu ESP32. En Visual Studio Code, selecciona este puerto en la configuración de PlatformIO.

7. **Reiniciar Visual Studio Code y PlatformIO:**
   - Reinicia Visual Studio Code después de configurar los controladores y el puerto COM.


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
