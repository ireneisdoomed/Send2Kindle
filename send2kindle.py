#!/usr/bin/env python

import argparse
from src.main import *

def parsear():
    # Inicializo parser
    parser = argparse.ArgumentParser(description=
    "A tool to automate the process of uploading an ebook to your Kindle. Supported files:")

    # Argumentos posicionales
    parser.add_argument("file", type=str, help="The path of the file you want to send in a valid format.")
    parser.add_argument("to_email", type=str, help="Your Kindle e-mail address.")

    args = parser.parse_args() # Parsea los argumentos y los devuelve de una manera en la que podamos trabajar

    return args

def main():
    args = parsear()
    server = crearConexion()
    
    mail = crearMIME(args.file, args.to_email)

    mandar(args.to_email, mail, server)
    cerrarConexion(server)

def welcome():
    print("-----------------------------------------------")
    print("""
  ____                 _ ____  _  ___           _ _      _ 
 / ___|  ___ _ __   __| |___ \| |/ (_)_ __   __| | | ___| |
 \___ \ / _ \ '_ \ / _` | __) | ' /| | '_ \ / _` | |/ _ \ |
  ___) |  __/ | | | (_| |/ __/| . \| | | | | (_| | |  __/_|
 |____/ \___|_| |_|\__,_|_____|_|\_\_|_| |_|\__,_|_|\___(_)
                                                           

    """)
    print("Welcome to Send2Kindle! These are the vasupportedlid formats for your file:")
    print("""
    Microsoft Word (.DOC, .DOCX)
    HTML (.HTML, .HTM)
    RTF (.RTF)
    JPEG (.JPEG, .JPG)
    Kindle Format (.MOBI, .AZW)
    GIF (.GIF)
    PNG (.PNG)
    BMP (.BMP)
    PDF (.PDF)\n""")
    print("-----------------------------------------------\n\n")


if __name__ == "__main__":
    welcome()
    main()