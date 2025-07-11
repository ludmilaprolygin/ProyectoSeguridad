#!/usr/bin/env python3

import cv2
import numpy as np
import argparse
import os

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
    
# Agregando informacion a la imagen
# n_bits puede variar de 1 a 6; representa la cantidad de bits que van a guardar informacion
def encode(image_name, secret_data, n_bits=2):
    image = cv2.imread(image_name)

    #Cantidad maxima de bytes que se pueden codificar
        #3 canales RGB, 8 bits por canal
    n_bytes = image.shape[0] * image.shape[1] * 3 * n_bits // 8 
    
    print("[*] Maximum bytes to encode:", n_bytes)
    print("[*] Encoding data length:", len(secret_data))
    if len(secret_data) > n_bytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or less data.")
    
    # Delimitador de fin de mensaje
    if isinstance(secret_data, str):
        secret_data += "====="
    elif isinstance(secret_data, bytes):
        secret_data += b"====="
    data_index = 0

    binary_secret_data = to_bin(secret_data)
    data_len = len(binary_secret_data)
    
    for bit in range(1, n_bits+1):
        for row in image:
            for pixel in row:
                # Convertir RGB a binario
                r, g, b = to_bin(pixel)

                if data_index < data_len:
                    if bit == 1:
                        # Modificar LSB del pixel rojo
                        pixel[0] = int(r[:-bit] + binary_secret_data[data_index], 2)
                    elif bit > 1:
                        pixel[0] = int(r[:-bit] + binary_secret_data[data_index] + r[-bit+1:], 2)
                    data_index += 1
                if data_index < data_len:
                    if bit == 1:
                        # Modificar LSB del pixel verde
                        pixel[1] = int(g[:-bit] + binary_secret_data[data_index], 2)
                    elif bit > 1:
                        pixel[1] = int(g[:-bit] + binary_secret_data[data_index] + g[-bit+1:], 2)
                    data_index += 1
                if data_index < data_len:
                    if bit == 1:
                        # Modificar LSB del pixel azul
                        pixel[2] = int(b[:-bit] + binary_secret_data[data_index], 2)
                    elif bit > 1:
                        pixel[2] = int(b[:-bit] + binary_secret_data[data_index] + b[-bit+1:], 2)
                    data_index += 1

                if data_index >= data_len:
                    break
    return image

# Descifrando texto de la imagen
def decode(image_name, n_bits=1, in_bytes=False):
    image = cv2.imread(image_name)

    binary_data = ""

    for bit in range(1, n_bits+1):
        for row in image:
            for pixel in row:
                r, g, b = to_bin(pixel)
                binary_data += r[-bit]
                binary_data += g[-bit]
                binary_data += b[-bit]

    # Dividir la cadena binaria en bytes
    all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
    
    if in_bytes:
        # Si se quiere decodificar data binaria, se inicializa un bytearray y no un string
        decoded_data = bytearray()
        for byte in all_bytes:
            decoded_data.append(int(byte, 2))
            if decoded_data[-5:] == b"=====":
                break
    else:
        # Converir de binario a texto
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2)) 
            if decoded_data[-5:] == "=====":
                break

    return decoded_data[:-5]



def set_args():
    parser = argparse.ArgumentParser(description="Esteganografia. Este script oculta informacion en imagenes.")
    parser.add_argument("-t", "--text", help="El texto que quiere ocultarse en la imagen, solo deberia especificarse para el encoding")
    parser.add_argument("-f", "--file", help="El archivo que quiere ocultarse en la imagen, solo deberia especificarse para el encoding")
    parser.add_argument("-e", "--encode", help="Encoding de la imagen")
    parser.add_argument("-d", "--decode", help="Decoding de la imagen")
    parser.add_argument("-b", "--n-bits", help="Cantidad de LSB al hacer el encoding", type=int, default=2)
    return parser.parse_args()

if __name__ == "__main__":
    args = set_args()

    if args.encode:
        if args.text:
            secret_data = args.text
        elif args.file:
            with open(args.file, "rb") as f:
                secret_data = f.read()

        input_image = args.encode

        filename = os.path.basename(input_image)
        name, ext = os.path.splitext(filename)

        base_dir = os.path.dirname(__file__)

        output_dir = os.path.join(base_dir, "resources", "encoded_images")
        os.makedirs(output_dir, exist_ok=True)

        output_image = os.path.join(output_dir, f"{name}_encoded{ext}")
        encoded_image = encode(image_name=input_image, secret_data=secret_data, n_bits=args.n_bits)
        cv2.imwrite(output_image, encoded_image)
        print("[+] Saved encoded image.")
    if args.decode:
        input_image = args.decode
        if args.file:
            decoded_data = decode(input_image, n_bits=args.n_bits, in_bytes=True)
            with open(args.file, "wb") as f:
                f.write(decoded_data)
            print(f"[+] File decoded, {args.file} is saved successfully.")
        else:
            decoded_data = decode(input_image, n_bits=args.n_bits)
            print("[+] Decoded data:", decoded_data)