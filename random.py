# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:16:56 2016

@author: ziyma
"""
import random
from Tkinter import *

topic_list=[]
name_list=[]
#---------------get data from txt documents-------------------------
def get_file(filename):
    try:
        with open(filename) as f:
            datas=[]
            for eachline in f:
                data=eachline.strip()
                datas.append(data)
            return(datas)
    except IOError:
        print('Flie error')
        return(None)
#---------------make a window and show result-----------------------
def showout(name_list):
    window=Tk() 
    window.title("Topic matching result:")  
    frame = Frame(window, relief=RIDGE, borderwidth=0)  
    frame.pack(fill=BOTH, expand=0)   
    result = Listbox(window,font="Monotype\ Corsiva -30 bold")
    result.insert(0,'  ')
    for eachname in name_list:    
        result.insert(1, '            '+eachname + "'s     topic    is     "+ topic_list.pop(0))
    result.pack(fill=BOTH, expand=30)    
    window.geometry('1000x600')   
    window.update_idletasks()  
    window.deiconify()  
    window.mainloop()    

topic_list=get_file('Topics.txt')  #get datas
name_list=get_file('Members.txt')
random.shuffle(name_list)          #made it out of order
random.shuffle(topic_list)
showout(name_list)                 #show out result