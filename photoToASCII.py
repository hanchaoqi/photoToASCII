# -*- coding:utf8 -*-
# Author:aisk

import sys
import PIL
import Image

HEIGHT = 150
chars = "#####%%%%%%^^^^^&&&&&&((((((*+*****"

def pic2ascii(filename):
    output = ''
    image = Image.open(filename)
    size = getsize(image)
    image = image.resize(size)
    image = image.convert('L')
    pixs = image.load()
    for y in range(size[1]):
        for x in range(size[0]):
            output += chars[pixs[x,y]/10]
        output += '\n'
    #print output
    f = open('fairy.txt','w+')  
    f.writelines(output)  
    f.close()  
    print 'Done'

def getsize(image):
    '''Calculate the target picture size
    '''
    s_width = image.size[0]
    s_height = image.size[1]
    t_height = HEIGHT
    t_width = (t_height*s_width)/s_height
    t_width = int(t_width * 2.3)
    t_size = (t_width ,t_height)
    return t_size

if __name__ == '__main__':
    filename = 'D:\\fairy.jpg'
    pic2ascii(filename)
