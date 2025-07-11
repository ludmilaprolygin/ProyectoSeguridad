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

## Notas importantes

- Se recomienda usar imágenes PNG (sin compresión con pérdida).
- El archivo o texto oculto no debe superar la capacidad de la imagen.
- La longitud del mensaje se codifica en los primeros 32 bits de la imagen.
- El mensaje se guarda sin delimitador, garantizando robustez con cualquier valor de `n_bits`.

---