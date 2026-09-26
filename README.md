# 🎬 Descargador de Video y Audio (MP3 / MP4)

Un programa de escritorio **sencillo pero muy útil** para descargar videos en formato **MP4** (video) o **MP3** (audio), con una interfaz gráfica fácil de usar. Solo pegas el link, eliges el formato y presionas un botón.

Funciona con **YouTube y con muchísimos otros sitios**, ya que usa yt-dlp, que es compatible con cientos de plataformas de video y audio (redes sociales, sitios de streaming, plataformas de música independiente, etc.). Consulta la [lista oficial de sitios compatibles](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

## ¿Por qué existe este programa?

En internet hay muchísimas páginas que convierten videos (de YouTube y otras plataformas) a MP3 o MP4, pero la mayoría tienen problemas:

- Están llenas de **anuncios** intrusivos y ventanas emergentes.
- Muchas redirigen a sitios engañosos o piden instalar cosas innecesarias, con el **riesgo de virus o malware**.
- Suelen limitar la calidad, el tamaño o la cantidad de descargas.

Este programa evita esos problemas porque funciona **de forma local en tu computadora** y usa [**yt-dlp**](https://github.com/yt-dlp/yt-dlp), una librería de código abierto, muy popular y mantenida activamente por la comunidad. No hay anuncios, no hay registros, y todo el código es visible y revisable por cualquiera (son menos de 150 líneas en un solo archivo).

> 💡 Como con cualquier software, descarga siempre desde fuentes confiables (este repositorio y el sitio oficial de yt-dlp y ffmpeg).

## ✨ Características

- Interfaz gráfica simple (hecha con `tkinter`, incluido en Python).
- Selector de formato: **MP4** o **MP3**.
- Campo para pegar el link del video (YouTube u otro sitio compatible con yt-dlp).
- Elección de la carpeta de destino.
- Barra de progreso y mensajes de estado.
- La ventana no se congela mientras descarga.

## 📋 Requisitos

| Requisito | Para qué sirve | Cómo obtenerlo |
|---|---|---|
| **Python 3.8 o superior** | Ejecutar el programa | [python.org/downloads](https://www.python.org/downloads/) |
| **yt-dlp** | Descargar los videos | `pip install yt-dlp` |
| **ffmpeg** | Convertir a MP3 y unir video + audio en MP4 | Ver instalación abajo |

> Al instalar Python en Windows, marca la casilla **"Add Python to PATH"**.

## 🚀 Instalación

### 1. Descargar el proyecto

**Opción A: con Git**

```bash
git clone https://github.com/HernanQuijano/Video-and-audio-downloader
cd Video-and-audio-downloader
```

**Opción B: sin Git**

1. En la página del repositorio, haz clic en el botón verde **Code**.
2. Selecciona **Download ZIP**.
3. Descomprime la carpeta y ábrela.

### 2. Instalar las librerías de Python

Desde una terminal dentro de la carpeta del proyecto:

```bash
pip install -r requirements.txt
```

O directamente:

```bash
pip install yt-dlp
```

> Si `pip` no funciona, prueba con `python -m pip install yt-dlp`.

### 3. Instalar ffmpeg

**Windows** (desde PowerShell o CMD):

```bash
winget install ffmpeg
```

**macOS** (con [Homebrew](https://brew.sh/)):

```bash
brew install ffmpeg
```

**Linux (Debian/Ubuntu):**

```bash
sudo apt install ffmpeg
```

Para comprobar que quedó instalado, ejecuta `ffmpeg -version` en la terminal. Si muestra información de la versión, todo está bien. (Después de instalarlo, cierra y vuelve a abrir la terminal.)

## ▶️ Uso

1. Ejecuta el programa:

   ```bash
   python downloader.py
   ```

2. En la ventana:
   1. Pega el **link del video** en el campo de texto (de YouTube o de cualquier otro sitio compatible).
   2. Elige el formato: **MP4** (video) o **MP3** (audio).
   3. (Opcional) Cambia la carpeta de destino con **Examinar...**
   4. Presiona **Descargar**.
3. Cuando termine, verás el mensaje "¡Descarga completada!" y el archivo estará en la carpeta elegida (por defecto, `Descargas`).

## 🛠️ Solución de problemas

| Problema | Posible solución |
|---|---|
| `ModuleNotFoundError: No module named 'yt_dlp'` | Instala la librería: `pip install yt-dlp` |
| Error relacionado con `ffmpeg` o `ffprobe` | Instala ffmpeg y reinicia la terminal (ver paso 3) |
| La descarga falla de repente con videos que antes funcionaban | YouTube cambia con frecuencia; actualiza yt-dlp: `pip install -U yt-dlp` |
| `pip` o `python` no se reconocen | Reinstala Python marcando "Add Python to PATH" |
| El link es de una lista de reproducción | Por defecto solo se descarga el video individual (ver `noplaylist` en el código) |
| Un sitio que no es YouTube no funciona | Verifica que esté en la [lista de sitios compatibles](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md), actualiza yt-dlp y ten en cuenta que algunos sitios exigen inicio de sesión o tienen contenido protegido (DRM) que no se puede descargar |

## ⚖️ Aviso legal

Este programa es una herramienta educativa y de uso personal. Descarga únicamente contenido que sea tuyo, que tenga licencia libre o para el que tengas permiso. **Respeta los derechos de autor y los Términos de Servicio de cada plataforma (YouTube u otras)**. El autor no se hace responsable del uso que se le dé.

## 🙌 Créditos

- [yt-dlp](https://github.com/yt-dlp/yt-dlp): la librería que hace todo el trabajo de descarga.
- [ffmpeg](https://ffmpeg.org/): conversión y procesamiento de audio y video.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.
