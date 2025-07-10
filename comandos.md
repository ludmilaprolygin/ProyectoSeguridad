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