## Python
### Laptop
#### 1. python steg.py -d .\resources\encoded_images\DCIC_encoded_1.png -b 1
#### 2. python steg.py -d .\resources\encoded_images\DCIC_encoded_2.png -f archivo.pdf -b 1
#### 3. python steg.py -d .\resources\encoded_images\DCIC_encoded_3.png -f archivo.mp4 -b 7

### Escritorio
#### 1. python3 steg.py -d resources/encoded_images/DCIC_encoded_1.png -b 1
#### 2. python3 steg.py -d resources/encoded_images/DCIC_encoded_2.png -f archivo.pdf -b 1
#### 3. python3 steg.py -d resources/encoded_images/DCIC_encoded_3.png -f archivo.mp4 -b 7
---
## Steghide
#### 1. Mostrar directorio y abrir imagen para verla
#### 2. Mostrar estado de la imagen
steghide info Akira.jpg
#### 3. Crear documento
echo "Proyecto de Seguridad en Sistemas ~ Esteganografía: ocultamiento de información en entornos digitales" > mensaje_oculto.txt
#### 4. Esconder archivo en imagen
steghide embed -cf Akira.jpg -ef mensaje_oculto.txt
#### 5. Mostrar estado de la imagen
steghide info Akira.jpg
#### 6. Mostrar directorio y abrir imagen para verla
#### 7. Extraer archivo
steghide extract -sf Akira.jpg
#### 8. Mostrar contenido del archivo
---
## Herramientas de deteccion
### Binwalk
#### 1. Analisis de la imagen
binwalk Akira.jpg
#### 2. Extraccion de contenido
binwalk -e Akira.jpg
#### 3. Append de contenido en jpg
cat Akira_original.jpg mensaje_oculto.txt > Akira.jpg
#### 4. Extraccion de contenido
binwalk -e Akira.jpg
#### 5. Append de contenido en png
cat DCIC_original.png hidden_file.pdf > DCIC.png
#### 6. Extraccion de contenido
binwalk -e DCIC.png 

### Strings
#### Mostrar contenido de tipo texto
strings Akira.jpg | tail