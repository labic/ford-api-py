# -*- coding: utf-8 -*-
"""
author: Andrei Bastos
organization: Labic/Ufes
data: 19/01/2018
"""

from enum import Enum
import json, os

import subprocess, threading

query = {
    "source": "twitter",
    "type": "flashback",
    "flashback_data": "tweets",
    "arguments": {        
        "terms": "dilma",
        "max_days": 5,
        "max_number": 10,
        "since_id": "15155345_56595951",
        "max_id": "-1",
        "language": "pt",
        "geocodes": {
            "lat": -20.351,
            "long": -40.175,
            "radius": 100
        },
        "filters": {
            "is_reverse": True,
            "terms": [
                {
                    "status.text": "não"
                },
                {
                    "status.user.screen_name": "andreibastos"
                }
            ]}
    }
}

arguments = {"minimum":None, "maximum":None, "days":1, "geocodes":[], "lang":"pt","number":None}

def type_input(data_input):
    formats = ['tab','csv', 'txt']
    for data_format in formats:
        if "."+ data_format in data_input:
            return 'file'
    return 'argument'


class Twitter(threading.Thread):    
    def __init__(self,data_input,arguments):
        threading.Thread.__init__(self)        
        self.arguments = arguments
        self.data_input = data_input    

    @staticmethod    
    def terms(data_input, arguments):
        command = "-t --twitter-data tweets -i "
        command = command + data_input

        command = command + " -o {0}".format(data_input)
        arguments_str = ""

        
        for argument in arguments.keys():
            if arguments.get(argument):            
                arguments_str =  arguments_str +  " --" +argument + " "+ str(arguments.get(argument))

        command =  "ford {0} {1} -n 100 -q".format(command,arguments_str)
        execute_command(command)
    
    def run  (self)  :
        print("iniciando")
        self.terms(self.data_input,arguments)
    
def execute_command(command):    
    print(command)
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()
        return process
        # print(process.pid, output, error)
    except Exception as identifier:
        print(identifier)

class Mine():
    Name = ''
    command = ""
    ## ford config
    Input = ''
    Output = ''
    Timezone = 'GMT'
    MaxMemory = 1024
    
    def Twitter(self):
        self.command += "-t "     

        def type_input():
            formats = ['tab','csv', 'txt']
            for format in formats:
                if "."+format in self.Input:
                    return 'file'
            return 'argument'

        def Collect(self):
            self.command += "--twitter-data "
            Minimum =  -1
            Maximum = -1
            Days = 1
            Geocodes = []
            def terms(self):
                self.command += "terms "

                print(self.command)
                pass
            
            def tweet_ids(self):
                self.command += "tweet-ids "
                pass

            def timelines(self):
                self.command += "timelines "
                pass

            def users(self):
                self.command += "users "
                pass
            
            def friends(self):
                self.command += "friends "
                pass

            def followers(self):
                self.command += "followers "
                pass

            def retweets(self):
                self.command += "retweets "
                
                pass
        
        def Stream():
            self.command.append("s")
            port = 8181
            ats_only = []
            rts_only = []
            no_gephi  = False

        def replies(self):
            self.command.append("r")
            pass

        def scrap(self):
            self.command.append("w")
            pass    

        def treding_topics(self):
            self.command.append("t")
            pass

    def Facebook():
        def Format(Enum):
            CLASSIC = 1
            ADVANCED = 2
            REACTIONS = 3
            SPLIT = 4
            BASIC = 5

        Format = Format.CLASSIC        
    
        def Data():
            def feeds(self):
                pass

            def pages(self):
                pass

            def members(self):
                pass

            def post_ids(self):
                pass
            def shares(self):
                pass            
            def comments(self):
                pass

        def feeds(self):
            pass
        def hashtag(self):
            pass
        def search(self):
            pass

    

    def Imagem():
        """
    IMAGES: faz o download de imagens dentro de páginas ou URLs em um dataset.
    precisa alterar um arquivo de configurações chamado: /lib/basiccrawler/cfg.txt conferir
    deve-se especificar a coluna do usuário 
    """
        def download():
            pass
class Collect():
    pid = 0
    priority = 0
    source = ""
    type = ""
    arguments = {}

    def __init__(self,query):
        self.source = query.get("source") or self.source
        self.type = query.get("type")
        self.arguments = query.get("arguments")
        self.flashback_data = query.get("flashback_data")
        
    def twitter(self, arguments):
        self.source = "twitter"
        pass

    def facebook(self, arguments):
        self.source = "facebook"
        pass
    
    def restart(self):
        pass

    def kill():
        pass


a = Twitter("dilma", arguments)
b = Twitter("lula", arguments)
c = Twitter("tweet.csv", arguments)

a.start()
b.start()
c.start()

# a.run()
# b.run()
# c.run()

minhas_threads = [a,b,c]

for minha_thread in minhas_threads:
    minha_thread.join()
