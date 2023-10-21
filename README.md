# Proyecto IoTMusic - Teleperformance de Música y Tecnología

Este proyecto utiliza MicroPython para integrar una fotoresistencia con la tecnología IoT (Internet de las cosas) y música, enviando los valores de una fotoresistencia a través de UDP a un servidor y luego controlar parámetros sonoros en pure data.

## Requisitos

- Hardware: Placa ESP32, Sensores (fotoresistencia) y actuadores (LED).
- Visual Studio.
- NodeJs.
- MicroPython.

## Configuración de Placa ESP32

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
