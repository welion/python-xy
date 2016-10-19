#!/usr/bin/env python

import os
import sys
import pymongo
import bson.binary
from cStringIO import StringIO
import datetime


class img2mongo():


    def __init__(self):
        self.BASE_PATH = '/home/welion/Pictures'
        self.connect = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db = self.connect.img
        self.coll = self.db.images

    def Load_file(self,name):

        file_path = os.path.join(self.BASE_PATH,name)
        print "file_path" + file_path
        os.chdir(file_path)
        file_list = os.listdir(file_path)
        print file_list

        for file_name in file_list:
            source_path=os.path.join(file_path,file_name)
            with open(source_path,'rb') as open_file:
                content = StringIO(open_file.read())
                content = bson.binary.Binary(content.getvalue())
                img_dict = {'name':file_name,
                            'source_path':source_path,
                            'content':content,
                            'blog':name,
                            'update_time':datetime.datetime.now()}
                self.coll.save(img_dict)

    def Get_file(self,file_name):
        with open(file_name,'wb') as out_file:
            content = self.coll.find({'name':file_name})[0]['content']
            out_file.write(content)

if __name__ == '__main__':
    if sys.argv[1] > 0:
        name = sys.argv[1]
    else:
        name = 'test'

    img2mongo().Load_file(name)


#    img2mongo().Get_file('tumblr_o8byejp8nj1v8l9ijo5_540.jpg')





