# -*- coding: utf-8 -*-
import sys, requests, json, pandas as pd
from lib.parser import Parser
from lib.noauth import NoAuth
from lib.animation import Animation
import colorama
from colorama import Fore
from colorama import Style
import optparse

colorama.init(strip=False)
#-------------------------------------------------------------------------------
#                           Models - Entities
#-------------------------------------------------------------------------------
from models.entities.Request import Request


#Funciones
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="file", help="Argumento para indicar el nombre del archivo postman a procesar.")
    parser.add_option("-t", "--token", dest="token", help="Argumento para indicar el ingreso de un token.")
    parser.add_option("-u", "--url", dest="url", help="Si el postman no posee las variables de entorno Argumento para indicar el host/URL.")

    (options, arguments) = parser.parse_args()
    if not options.file:
        parser.error("[+] Porfavor especifica un archivo, usa --help para más información")

    return options
#-------------------------------------------------------------------------------
#                           Main Function
#-------------------------------------------------------------------------------
def main():
    #---------------------------------------------------------------------------
    #                          Class Instance
    #---------------------------------------------------------------------------
    parser = Parser()
    noauth = NoAuth()
    animation = Animation()


    options = get_args()
    if options.file:
        noauth.print_banner()
        animation.load_animation("analizando la información del archivo...")
        data = parser.read_file(options.file)

        total_request = parser.get_parser_request(data)
        list_obj_req = parser.get_items_request(total_request)
        noauth.print_banner()
        animation.load_animation("enviando solicitudes http...")
        noauth.print_banner()
        obj_res = noauth.request(list_obj_req)
        #for i in obj_res:
        #    print(i)


if __name__ == '__main__':
    main()
