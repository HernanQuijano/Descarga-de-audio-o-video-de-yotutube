import os
import threading
import yt_dlp
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Descargador de Audio o Video")
        self.geometry("560x300")
        self.resizable(False, False)

        self.url_var = tk.StringVar()
        self.formato_var = tk.StringVar(value="mp4")
        self.carpeta_var = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Downloads"))
        self.estado_var = tk.StringVar(value="Listo.")

        self._crear_widgets()

    def _crear_widgets(self):
        pad = {"padx": 12, "pady": 6}

        # Información
        self.button_info = ttk.Button(self, text="¡", command=self._mostrar_info)
        self.button_info.grid(row=0, column=2, sticky="e", **pad)
        # Link
        ttk.Label(self, text="Link de YouTube:").grid(row=0, column=0, sticky="w", **pad)
        ttk.Entry(self, textvariable=self.url_var, width=52).grid(row=1, column=0, columnspan=3, sticky="we", **pad)

        # Formato
        ttk.Label(self, text="Formato:").grid(row=2, column=0, sticky="w", **pad)
        marco = ttk.Frame(self)
        marco.grid(row=2, column=1, sticky="w")
        ttk.Radiobutton(marco, text="MP4 (video)", variable=self.formato_var, value="mp4").pack(side="left", padx=6)
        ttk.Radiobutton(marco, text="MP3 (audio)", variable=self.formato_var, value="mp3").pack(side="left", padx=6)

        # Carpeta
        ttk.Label(self, text="Guardar en:").grid(row=3, column=0, sticky="w", **pad)
        ttk.Entry(self, textvariable=self.carpeta_var, width=40).grid(row=4, column=0, columnspan=2, sticky="we", **pad)
        ttk.Button(self, text="Examinar...", command=self._elegir_carpeta).grid(row=4, column=2, **pad)

        # Botón
        self.boton = ttk.Button(self, text="Descargar", command=self._iniciar)
        self.boton.grid(row=5, column=0, columnspan=3, pady=10)

        # Progreso
        self.barra = ttk.Progressbar(self, length=530, maximum=100)
        self.barra.grid(row=6, column=0, columnspan=3, padx=12)
        ttk.Label(self, textvariable=self.estado_var).grid(row=7, column=0, columnspan=3, pady=6)

    def _mostrar_info(self):
        info_text = (
            "Descargador de Audio o Video de YouTube\n"
            "Versión: 1.0\n"
            "Autor: Hernan Quijano\n"
            "Este programa permite descargar videos o audios de YouTube en formato MP4 o MP3.\n"
            "Asegúrate de revisar el readme en el repositorio de gitHub para más información.\n"
            "Repositorio: 'https://github.com/HernanQuijano/Video-and-audio-downloader'"

        )
        messagebox.showinfo("Información", info_text)

    def _elegir_carpeta(self):
        carpeta = filedialog.askdirectory(initialdir=self.carpeta_var.get())
        if carpeta:
            self.carpeta_var.set(carpeta)

    def _iniciar(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Falta el link", "Pega un link de YouTube.")
            return
        self.boton.config(state="disabled")
        self.barra["value"] = 0
        self.estado_var.set("Iniciando...")
        # Hilo aparte para que la ventana no se congele
        threading.Thread(target=self._descargar, args=(url,), daemon=True).start()

    def _hook(self, d):
        if d["status"] == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate")
            if total:
                porcentaje = d["downloaded_bytes"] / total * 100
                self.after(0, self._actualizar, porcentaje, f"Descargando... {porcentaje:.1f}%")
        elif d["status"] == "finished":
            self.after(0, self._actualizar, 100, "Procesando archivo (ffmpeg)...")

    def _actualizar(self, valor, texto):
        self.barra["value"] = valor
        self.estado_var.set(texto)

    def _descargar(self, url):
        carpeta = self.carpeta_var.get()
        opciones = {
            "outtmpl": os.path.join(carpeta, "%(title)s.%(ext)s"),
            "progress_hooks": [self._hook],
            "noplaylist": True,
            "quiet": True,
        }

        if self.formato_var.get() == "mp3":
            opciones.update({
                "format": "bestaudio/best",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            })
        else:
            opciones.update({
                "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                "merge_output_format": "mp4",
            })

        try:
            with yt_dlp.YoutubeDL(opciones) as ydl:
                ydl.download([url])
            self.after(0, self._terminar, True, "¡Descarga completada!")
        except Exception as e:
            self.after(0, self._terminar, False, f"Error: {e}")

    def _terminar(self, ok, mensaje):
        self.boton.config(state="normal")
        self.estado_var.set(mensaje if ok else "Falló la descarga.")
        if ok:
            messagebox.showinfo("Listo", mensaje)
        else:
            messagebox.showerror("Error", mensaje)


if __name__ == "__main__":
    App().mainloop()
