# Esteganografía LSB - Seguridad en Sistemas

Este proyecto implementa una herramienta de **esteganografía LSB (Least Significant Bit)** que permite ocultar texto o archivos binarios dentro de imágenes PNG, utilizando una cantidad configurable de bits menos significativos por canal RGB.

---

## Uso

### Requisitos
- Python 3.x
- OpenCV → `pip install opencv-python`
- NumPy → `pip install numpy`
- Alternativa: `pip3 install -r requirements.txt`

---

### Codificar texto:
```bash
python3 esteganografia.py -e imagen.png -t "mensaje secreto" -b 3
```

Esto guarda una imagen en `resources/encoded_images/imagen_encoded.png` con el mensaje oculto usando 3 bits LSB por canal.

---

### Codificar archivo (ej: PDF, MP4):
```bash
python3 esteganografia.py -e imagen.png -f archivo.mp4 -b 4
```

---

### Decodificar texto:
```bash
python3 esteganografia.py -d resources/encoded_images/imagen_encoded.png -b 3
```

---

### Decodificar archivo:
```bash
python3 esteganografia.py -d resources/encoded_images/imagen_encoded.png -f archivo_extraido.mp4 -b 4
```

---

## Parámetros

| Opción       | Descripción                                  |
|--------------|----------------------------------------------|
| `-e`         | Ruta a la imagen original para codificar     |
| `-d`         | Ruta a la imagen codificada para decodificar |
| `-t`         | Texto a ocultar (solo encoding)              |
| `-f`         | Archivo a ocultar o recuperar                |
| `-b`         | Bits LSB a usar (1 a 6). Default: `2`        |

---
---

## Stegosploit educativo

Este proyecto también incluye una demostración de esteganografía activa, donde se oculta un fragmento de código JavaScript dentro de los bits menos significativos (LSB) del canal rojo de una imagen PNG. Al ser renderizada en una página HTML, el navegador recupera y ejecuta dicho código automáticamente mediante canvas.

---

### Requisitos
- Python 3.x
- Pillow → `pip install pillow`

---

### Generar la imagen con código oculto

1. Editar el script `embed_stegosploit.py` para modificar el código JavaScript a ocultar:

```python
codigo = 'alert("Este es un stegosploit educativo");'
```

2. Ejecutar el script:

```bash
python3 embed_stegosploit.py
```

Esto generará un archivo `imagen_oculta.png` con el código oculto en sus píxeles.

---

### Probar el stegosploit en el navegador

1. Abrir el archivo `demo.html` en un navegador.

2. La imagen se renderiza y automáticamente el navegador recupera el código oculto y lo ejecuta. En el ejemplo incluido, se muestra un `alert()` con un mensaje.

---

### Archivos relacionados

- `embed_stegosploit.py`: script para ocultar código JavaScript en una imagen PNG.
- `imagen_base.png`: imagen inicial sin código oculto.
- `imagen_oculta.png`: imagen resultante con el stegosploit embebido.
- `demo.html`: página que carga la imagen, extrae el código y lo ejecuta.

### Probar desde un servidor local

Algunos navegadores bloquean la ejecución de código desde archivos locales (`file://`) por razones de seguridad. Para evitar esto, se recomienda levantar un servidor HTTP local.

```bash
# Desde el directorio donde están demo.html e imagen_oculta.png
python3 -m http.server 8000
# Desde el navegador
http://0.0.0.0:8000/demo.html
```

---
---

## Notas importantes

- Se recomienda usar imágenes PNG (sin compresión con pérdida).
- El archivo o texto oculto no debe superar la capacidad de la imagen.
- La longitud del mensaje se codifica en los primeros 32 bits de la imagen.
- El mensaje se guarda sin delimitador, garantizando robustez con cualquier valor de `n_bits`.
- Este proyecto fue realizado con fines educativos y no debe utilizarse en contextos reales ni maliciosos.
---