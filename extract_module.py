import os
from tkinter import *
import sys
from proj2 import checksyntax
c=[]
c1=[]
def getline():
    directory=str(entry1.get())
    #print(e1)
#directory="C:\\Users\Ajeya\Javafiles"
    for content in os.listdir(directory):
        x=directory+"\\"+content
        if(x.endswith(".java")):
            checksyntax(x)
        sys.stdout.write=redirector
def redirector(inputStr):
    text1.insert(INSERT, inputStr)
root=Tk()
root.title("Code Semantic Scanner")
root.geometry("500x500")
upframe=Frame(root,height=200,width=200)
upframe.pack()
downframe=Frame(root,height=200,width=200)
downframe.pack()
label1=Label(upframe,text="ENTER THE ADDRESS")
label1.pack()
entry1=Entry(upframe,width=500)
entry1.pack(fill=X)
button1=Button(upframe,text="ENTER",command=getline)
button1.pack()
label2=Label(downframe,text="ERRORS IN YOUR FILE")
label2.pack()
text1=Text(downframe)
text1.pack()
root.mainloop()
