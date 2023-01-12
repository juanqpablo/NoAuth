import  json, re
from models.entities.Request import Request

#---------------------------------------------------------------------------
#                           Define global variables
#---------------------------------------------------------------------------
list_object = []

class Parser():
    #---------------------------------------------------------------------------
    #           Read File
    #---------------------------------------------------------------------------
    def read_file(self, URL):
        with open(URL, 'r') as f:
           data = json.load(f)
        return data

    #---------------------------------------------------------------------------
    #          Get Total Request with file Postman
    #---------------------------------------------------------------------------
    def get_parser_request(self, data):
        total_request = []
        list_request = []
        keys_data = data.keys()
        if 'item' in keys_data:
            array_item = data['item']
            self.find_request(array_item, len(array_item)-1)
            total_request = list_object
        return total_request

    #---------------------------------------------------------------------------
    # Get items from request
    #---------------------------------------------------------------------------
    def get_items_request(self, list_request, without_token = True, without_cookie = False):
        _body = {}
        list_headers = {}
        method = ""
        dict_data = {}
        objets = []

        #Get data for generate object
        for index in range(len(list_request)):
            #Parser data
            name = list_request[index]['name']
            method = list_request[index]['request']['method']
            lengh_headers = len(list_request[index]['request']['header'])
            header = list_request[index]['request']['header']
            url = list_request[index]['request']['url']['raw']
            # verify if method is isn't  the get method
            if method!= 'GET':
                if 'body' in list_request[index]['request']:
                    if 'raw' in list_request[index]['request']['body']:
                        body = list_request[index]['request']['body']['raw']

                    else:
                        body = list_request[index]['request']['body']

                else:
                    body = None

            headers = {}
            # remove of each object depending on the condition and stores the remaining
            for h in header:
                if h['key']!="":
                    if (h['key']!= 'authorization' and without_token == True) and without_cookie == False:
                        headers[h['key']] = h['value']

                    if (h['key']!= 'cookie' and  without_cookie == True) and ( h['key']!= 'authorization' and without_token == True):
                        headers[h['key']] = h['value']
                else:
                    continue

            # Create new object request
            obj_request = Request(
                name = name,
                method = method,
                headers = headers,
                body = body,
                url = url
            )

            objets.append(obj_request)
        return objets


    #---------------------------------------------------------------------------
    # Recursive method for find request object on Dict Postman
    #---------------------------------------------------------------------------
    def find_request(self, array_item, lengh):
        if lengh!=-1:
            if 'request' in array_item[lengh].keys():
                obj_lvl = array_item[lengh]
                obj_lvl.pop('response', None)
                list_object.append(obj_lvl)
                lengh-=1
                self.find_request(array_item, lengh)

            else:
                if 'item' in array_item[lengh].keys():
                    self.find_request(array_item[lengh]['item'], len(array_item[lengh]['item']) -1)
        else:
            return list_object



    #---------------------------------------------------------------------------
    # Methods that get environment variables
    #---------------------------------------------------------------------------
    def get_environment(self, file_env):

        dict_data = {}
        keys = file_env.keys()
        try:
            if 'values' in file_env:
                for i in range(len(file_env['values'])):
                    dict_env = file_env['values'][i]
                    if 'key' in dict_env or 'value' in dict_env:
                        #if dict_env['value']!="":
                        dict_data[ dict_env['key'] ] = dict_env['value']

                    else:
                        return None
            else:
                return None

        except Exception as e:
            raise Exception(e)

        return dict_data.items()

    #---------------------------------------------------------------------------
    # Method that transforms a json to text
    #---------------------------------------------------------------------------
    def transform_json_text(self, filename ):
        with open(filename, 'r+') as fr:
            pre_ = fr.read()
        return pre_

    #---------------------------------------------------------------------------
    # Recursive method that replaces expressions with their respective values
    #---------------------------------------------------------------------------
    def recursive_replace( self, file_text, list_env, lengh):
        if lengh < 0:
            return file_text

        else:
            if isinstance(file_text, str):
                if list(list_env)[lengh][0]:
                    if '{{' +list(list_env)[lengh][0] + '}}' in file_text:
                        file_text = file_text.replace("{{"+list(list_env)[lengh][0]+"}}", list(list_env)[lengh][1])
                        return self.recursive_replace(file_text, list_env,  lengh - 1)
                    else:
                        return self.recursive_replace(file_text, list_env, lengh - 1)
            else:
                return None




    #---------------------------------------------------------------------------
    # Verify expression in content file
    #---------------------------------------------------------------------------
    def check_expression(self, file):
        """
        identify expression {{variable}} in content file
        """
        exp = '{[{]|}}'

        m = re.search(exp, file)
        if m.group(0) == '{{':
            return True
        else:
            return False
