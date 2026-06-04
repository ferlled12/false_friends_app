# 🃏 False Friends - Vocabulary App

Una aplicación de escritorio interactiva y ligera diseñada para practicar y dominar los "falsos amigos" (*false friends*) del vocabulario en inglés. Construida completamente en Python puro, proporciona retroalimentación visual inmediata sin necesidad de dependencias externas. Fué la aplicación que cree como proyecto final de mi curso en inglés Stanford University's Code in Place 2026 edition.

## 🚀 Características

* **Interfaz minimalista:** Diseño limpio y centrado en el mensaje para evitar distracciones durante el aprendizaje.
* **Interactividad inmediata:** Detección precisa de clics (hitboxes) con respuesta visual al instante (verde para aciertos, rojo para errores).
* **Gestión de estado autónoma:** El flujo de la aplicación se actualiza de forma dinámica, avanzando de palabra automáticamente tras procesar la respuesta.
* **Zero dependencies:** Utiliza `Tkinter`, la librería gráfica estándar de Python. Funciona *out-of-the-box* en cualquier sistema sin necesidad de configurar entornos virtuales ni instalar paquetes adicionales.

## 🛠️ Tecnologías utilizadas

* **Lenguaje:** Python 3.x
* **Librería gráfica:** Tkinter (Nativa)

## 🛠️ Demostración visual

![Captura de pantalla de la app](https://i.imgur.com/37TjYE5.png)

## 📦 Instalación y ejecución

Al no requerir librerías de terceros (no es necesario hacer `pip install`), ejecutar el proyecto es extremadamente sencillo:

1. Clona este repositorio o descarga el archivo principal.
2. Debemos tener python instalado.
3. Abrimos la terminal y navegamos hasta el directorio del proyecto.
4. Ejecuta el siguiente comando:

   ```bash
   python false_friends.py
