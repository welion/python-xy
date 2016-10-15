# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:49:19 2016

Get Tumblr dashboard info

@author: welion
"""

import threading
import urllib,urllib2
import os,sys
import pytumblr
import time

PATH = '/root/Pictures/'

class Welion_Tumblr():
    API_KEY = '2JK7GvJw1PnwHnDJPJKUyqsK37UlFvrzdVzsHMku8hUvRgEu4N'
    
    Consumer_Key = '2JK7GvJw1PnwHnDJPJKUyqsK37UlFvrzdVzsHMku8hUvRgEu4N'
    Consumer_Secret = '13ch8DVC8NQ7F12xejwVfhaIR8tDkgH4eFa0jZHbi3MGQJFbq9'
    Token = 'XS8GUNVHCillcIzGNQFGN7n820EBcLZA1WcFlGp2WvzFJAmAzi'
    Token_Secret = 'CeKqFEY1DWY76yf2MwEum7jN0c8Hqsf3OA2sba7kWkRTpzIzFm'
    
    client = pytumblr.TumblrRestClient(Consumer_Key,Consumer_Secret,Token,Token_Secret)

    def get_photo_url(self,name):
        cli = pytumblr.TumblrRestClient('2JK7GvJw1PnwHnDJPJKUyqsK37UlFvrzdVzsHMku8hUvRgEu4N')
        
        url_list = []
        resp = cli.posts(name+'.tumblr.com',type='photo',limit=50)

        posts_num = len(resp['posts'])
        for i in range(posts_num):
            photos = resp['posts'][i]
            for j in photos['photos']:
                url =  j['original_size']['url']
                url_list.append(url)

        return url_list

    def download_photo(self,URL,PATH):
        name = URL.split('/')[-1]
        if os.path.exists(PATH+name) == False:
            os.chdir(PATH)
            try:
                jpg = urllib.urlopen(URL).read()
                with open(name,'wb') as f:
                    f.write(jpg)
                print "Download "+name+" OK :)"+ time.ctime()
            except Exception as e:
                print 'Download Error %s' %e
                pass
        else:
            print name + " Already Download -.-"


    def multiple_download(self,URL_LIST,PATH):
        lenth = len(URL_LIST)
        split_list = []
        if lenth > 30 :
            split_list = [URL_LIST[i:i+30] for i in range(0,lenth,30)]
        else:
            split_list.append(URL_LIST)

        for list_item in split_list:
            threads = []
            for i in range(len(list_item)):
                t = threading.Thread(target=self.download_photo,args=(list_item[i],PATH))
                threads.append(t)
            for t in threads:
                t.setDaemon(True)
                t.start()
                print "Threading ON!"
            t.join()
        




if __name__ == '__main__':
    if len(sys.argv) > 1:
        blog = sys.argv[1:]
    else:
        blog = ['hello-happylim-blog']
    for i in blog:
        url_list = Welion_Tumblr().get_photo_url(i)
        print len(url_list)
        path = os.path.join(PATH,i)
        if os.path.exists(path) == False:
            os.mkdir(path)
        os.chdir(path)
        print os.getcwd()
    
        Welion_Tumblr().multiple_download(url_list,path)
        print "All Done"
        
