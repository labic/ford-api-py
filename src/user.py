# -*- coding: utf-8 -*-
"""
author: Andrei Bastos
organization: Labic/Ufes
data: 04/02/2018
"""

import pymongo
import  time, datetime


client = pymongo.MongoClient()

db = client['ford']

collection_document = db['document']
collection_user = db['user']

class Document(object):
    user = None
    id_document = None     

    def __init__(self, type, name):
        self.type  = type 
        self.name = name
    
    @classmethod
    def CreateDirectory(cls, name,id_user, source_id = None, is_favorited = False, is_root = False  ):
        if not source_id:
            source_id = cls.GetRootIdDocument(id_user)     

        date_created = datetime.datetime.now()
        directory = {'id_user':id_user, 'type':'directory', 'name':name,'source_id':source_id, 'date_created' : date_created, 'date_modified': date_created, 'is_root':is_root}
        
        cls.CreateDirectorySystem(directory)
        
        collection_document.insert(directory)

    @staticmethod
    def GetRootIdDocument(id_user):
        query = {'id_user':id_user, 'is_root':True}
        result = collection_document.find_one(query)
        if result:
            return result['id_document']       
    
    @staticmethod
    def GetLastIdDocument( id_user):
        query = {'id_user':id_user}
        result = collection_document.find_one(query,sort=[("_id", pymongo.DESCENDING)])
        if result:
            return result.id_document
        else:
            return 0

    @staticmethod
    def CreateDirectorySystem(directory):
        pass
    
    def insert(self):
        pass

    def update(self):
        pass
    
    def delete(self):
        pass

class User(object):
    def __init__(self, id_user,name, roles, email, photo, country, city,settings):
        self.id_user = id_user
        self.name = name
        self.roles = roles 
        self.photo = photo
        self.country = country
        self.city = city
        self.settings = settings
    
    
    def GetLastIdUser(self):
        return 10    
    
    def new(self, arguments):
        id_user = self.GetLastIdUser()
        name = arguments.get('name')
        roles = arguments.get('roles')
        email = arguments.get('email')
        photo = arguments.get('photo')
        country = arguments.get('country')
        city = arguments.get('city')
        settings = [{"type":"system", "data":{"basepath":"/ford/"}}]
        Document.CreateDirectory(name,id_user, source_id =  )
        return User(id_user,name,roles,email,photo, country, city, settings)
    
    def create_directory(self, name):
        document = {"id":self.GetLastIdUser(),"type":"directory", "name":name}


        pass
    
    def create_collect(self,name):
        pass

    def create_file(self):
        pass
