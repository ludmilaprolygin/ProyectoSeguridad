import cv2
import numpy as np

def to_bin(data):
    """Codifica _data_ en su representacion binaria de 8 bits"""
    """La representacion a utilizar es la de 8 bits puesto que la codificacion RGB utiliza 8 bits por canal"""
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes):
        return ''.join([ format(i, "08b") for i in data ])
    elif isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")
    
# Agregando texto a la imagen
def encode_text(image_name, secret_data):
    image = cv2.imread(image_name)

    #Cantidad maxima de bytes que se pueden codificar
        #3 canales RGB, 8 bits por canal
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8 
    
    print("[*] Maximum bytes to encode:", n_bytes)
    if len(secret_data) > n_bytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or less data.")
    
    # Delimitador de fin de mensaje
    secret_data += "=====" 
    data_index = 0

    binary_secret_data = to_bin(secret_data)
    data_len = len(binary_secret_data)
    
    for row in image:
        for pixel in row:
            # Convertir RGB a binario
            r, g, b = to_bin(pixel)

            if data_index < data_len:
                # Modificar LSB del pixel rojo
                pixel[0] = int(r[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # Modificar LSB del pixel verde
                pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # Modificar LSB del pixel azul
                pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                data_index += 1

            if data_index >= data_len:
                break
    return image

# Descifrando texto de la imagen
def decode_text(image_name):
    image = cv2.imread(image_name)

    binary_data = ""

    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)

            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]

    # Dividir la cadena binaria en bytes
    all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
    
    # Converir de binario a texto
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2)) 
        if decoded_data[-5:] == "=====":
            break
    return decoded_data[:-5]


if __name__ == "__main__":
    input_image = "resources/original_images/DCIC.png"
    output_image = "resources/encoded_images/DCIC_encoded.png"
    secret_data = "Proyecto de esteganografia de Seguridad en Sistemas."

    encoded_image = encode_text(image_name=input_image, secret_data=secret_data)

    # Guardar la imagen codificada
    cv2.imwrite(output_image, encoded_image)

    decoded_data = decode_text(output_image)
    # decoded_data = decode_text(input_image) # Test para mostrar imagen sin datos codificados

    print("[+] Decoded data:", decoded_data)