import json, requests as re
import pandas as pd
from pandas.io.json import json_normalize
import colorama, time
from colorama import Fore
from colorama import Style

from models.entities.Output import Output

colorama.init(strip=False)

class NoAuth():

    #---------------------------------------------------------------------------
    #                             Print banner
    #---------------------------------------------------------------------------
    def print_banner(title=""):

        print(Fore.CYAN + """
         ____     __     ____       ____     __   __      __      __    __
        |   _ \  |  |  /  __  \   /  __  \  |  | |  |  __|  |__  |  |__|  |
        |  |\  \ |  | |  |  |  | |  |  |  | |  | |  | |__    __| |  |__|  |
        |  | \  \/  | |  |__|  | |  |__|  | |  |_|  |    |  |    |  |  |  |
        |__|   \__,_|  \ ____ /  |__|  |__|  \_____/     |__|    |__|  |__|
                                                        @4r13s > v.1.3
        """ + Style.RESET_ALL)

    #---------------------------------------------------------------------------
    #          Method that verify if data structure is empty or not empty.
    #---------------------------------------------------------------------------
    def is_empty(self, data_structure):
        if data_structure:
            #print("No está vacía")
            return False
        else:
            #print("Está vacía")
            return True

    #---------------------------------------------------------------------------
    #                   Method that makes the http request
    #---------------------------------------------------------------------------
    def request(self, objets):
        c = 0
        list_output = []
        space = 3
        output = ""
        for obj in objets:
            c+=1
            if c >= 10:
                space = 2
            if c>= 100:
                space = 1
            if obj.method == 'POST':
                if self.is_empty( obj.headers):
                    headers = {'Content-Type': 'application/json' , 'charset': 'utf-8'}
                    response = re.post(obj.url, headers=headers, data=obj.body )

                else:
                    response = re.post(obj.url, headers=obj.headers, data=obj.body )
                #print(response.status_code)
                if response.status_code == 200:
                    print (" "*2 + str(c) + " "*space + "[+] Endpoint: ", obj.url, "status:" , Fore.RED + "[ UNVALIDATED ]" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "  [ METHOD " + obj.method+" ]" +Style.RESET_ALL)

                    output = Output(
                        endpoint = obj.url,
                        code_status = response.status_code,
                        method = obj.method
                    )
                if response.status_code == 401:
                    print (" "*2 + str(c) + " "*space + "[+] Endpoint: ", obj.url, "status:" , Fore.GREEN + "[ VALIDATED ]" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " [ METHOD " +obj.method+" ]" + Style.RESET_ALL )
                    output = Output(
                        endpoint = obj.url,
                        code_status = response.status_code,
                        method = obj.method
                    )
                if response.status_code == 404:
                    print (" "*2 + str(c) + " "*space + "[+] Endpoint: ", obj.url, "status:" , Fore.GREEN + "[ VALIDATED ]" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " [ METHOD " +obj.method+" ]" + Style.RESET_ALL )
                    output = Output(
                        endpoint = obj.url,
                        code_status = response.status_code,
                        method = obj.method
                    )


            if obj.method == 'GET':
                response = re.get(obj.url, headers=obj.headers )
                if response.status_code == 200:
                    print (" "*2 + str(c) + " "*space + "[+] Endpoint: ", obj.url, "status:" , Fore.RED + "[ UNVALIDATED ]" + Style.RESET_ALL+ Fore.LIGHTCYAN_EX + " [ METHOD "+obj.method+" ]" +Style.RESET_ALL)

                    output = Output(
                        endpoint = obj.url,
                        code_status = response.status_code,
                        method = obj.method
                    )
                if response.status_code == 401:
                    print (" "*2 + str(c) + " "*space +"[+] Endpoint: ", obj.url, "status:" , Fore.GREEN + "[ VALIDATED ]" + Style.RESET_ALL+ Fore.LIGHTCYAN_EX + " [ METHOD "+obj.method+" ]" + Style.RESET_ALL )
                    output = Output(
                        endpoint = obj.url,
                        code_status = response.status_code,
                        method = obj.method
                    )
                if response.status_code == 404:
                    print (" "*2 + str(c) + " "*space + "[+] Endpoint: ", obj.url, "status:" , Fore.GREEN + "[ VALIDATED ]" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " [ METHOD " +obj.method+" ]" + Style.RESET_ALL )
                    output = Output(
                        endpoint = obj.url,
                        code_status = response.status_code,
                        method = obj.method
                    )

            list_output.append(output)

        return list_output



    def print_not_environment(self):
        print (" "*2 + "[+] Menssage: "+ Fore.YELLOW + "El Documento ingresado contiene variables de ambiente, favor ingresar el archivo environment!" +Style.RESET_ALL )
