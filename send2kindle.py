#!/usr/bin/env python

import argparse
from src.main import *

def parsear():
    # Inicializo parser
    parser = argparse.ArgumentParser(description="A tool to automate the process of uploading an ebook to your Kindle.")

    # Argumentos posicionales
    parser.add_argument("file", type=str, help="The path of the file you want to send in a valid format.")
    parser.add_argument("to", type=str, help="Your Kindle e-mail address.")

    args = parser.parse_args() # Parsea los argumentos y los devuelve de una manera en la que podamos trabajar

    return args

def main():
    args = parsear()
    server = crearConexion()
    
    mail = crearMIME(args.file, args.to)

    mandar(args.to, mail, server)
    cerrarConexion(server)
    server = 0


if __name__ == "__main__":
    main()