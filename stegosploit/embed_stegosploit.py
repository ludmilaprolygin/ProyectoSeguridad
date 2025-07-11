from PIL import Image
import sys

def ocultar_codigo(imagen_original, output, codigo_js):
    # Convertir el código a binario
    bits = ''.join(f'{ord(c):08b}' for c in codigo_js) + '00000000'  # Byte nulo para marcar el fin
    
    img = Image.open(imagen_original)
    img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size
    i = 0

    for y in range(height):
        for x in range(width):
            if i < len(bits):
                r, g, b = pixels[x, y]
                bit = int(bits[i])
                r = (r & ~1) | bit  # Reemplazar el LSB
                pixels[x, y] = (r, g, b)
                i += 1
            else:
                break
        if i >= len(bits):
            break

    img.save(output)
    print(f"Imagen generada con el código oculto: {output}")

# Ejemplo de uso
codigo = 'alert("Este es un stegosploit educativo");'
ocultar_codigo('imagen_base.png', 'imagen_oculta.png', codigo)