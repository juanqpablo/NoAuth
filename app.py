# -*- coding: utf-8 -*-
import sys, requests, json, pandas as pd
from lib.parser import Parser
from lib.noauth import NoAuth
from lib.animation import Animation
import colorama
from colorama import Fore
from colorama import Style
import argparse, time

colorama.init(strip=False)
#-------------------------------------------------------------------------------
#                           Models - Entities
#-------------------------------------------------------------------------------
from models.entities.Request import Request


#Funciones
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Argumento para indicar el nombre del archivo postman a procesar.")
    parser.add_argument("-e", "--env",  help="Argumento para indicar el nombre del archivo con las variables de ambiente (postman)")

    args = parser.parse_args()
    return args
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

    args = get_args()
    variables = vars(args)
    noauth.print_banner()
    animation.load_animation("analizando la información del archivo...")

    if args.file:
        text_file = parser.transform_json_text(args.file)
        if parser.check_expression(text_file):
            noauth.print_banner()
            noauth.print_not_environment()
        else:
            data = parser.read_file(args.file)
            total_request = parser.get_parser_request(data)
            list_obj_req = parser.get_items_request(total_request)
            noauth.print_banner()
            animation.load_animation("enviando solicitudes http...")
            noauth.print_banner()
            obj_res = noauth.request(list_obj_req)



    if (args.file and args.env):
        data_pre = parser.transform_json_text(args.file)
        file_env = parser.read_file(args.env)
        list_env = parser.get_environment(file_env)
        result = parser.recursive_replace(data_pre, list_env, len(list(list_env))-1)
        #convert string to  object
        json_object = json.loads(result)
        #print(json_object)
        total_request = parser.get_parser_request(json_object)
        list_obj_req = parser.get_items_request(total_request)
        noauth.print_banner()
        animation.load_animation("enviando solicitudes http...")
        noauth.print_banner()
        obj_res = noauth.request(list_obj_req)



if __name__ == '__main__':
    main()
