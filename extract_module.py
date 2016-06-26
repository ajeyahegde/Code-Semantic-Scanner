import os
import tkinter
import sys
from proj2 import checksyntax
c = []
c1 = []
def getline():
    directory=str(entry1.get())
#directory="C:\\Users\Ajeya\Javafiles"
    for content in os.listdir(directory):
        x=directory+"\\"+content
        if(x.endswith(".java")):
            checksyntax(x)
        sys.stdout.write=redirector
def redirector(inputStr):
    text1.insert(tkinter.INSERT, inputStr)
root=tkinter.Tk()
root.title("Code Semantic Scanner")
root.geometry("500x500")
upframe=tkinter.Frame(root,height=200,width=200)
upframe.pack()
downframe=tkinter.Frame(root,height=200,width=200)
downframe.pack()
label1=tkinter.Label(upframe,text="Enter the Directory Path")
label1.pack()
entry1=tkinter.Entry(upframe,width=500)
entry1.pack(fill=tkinter.X)
button1=tkinter.Button(upframe,text="Scan",command=getline)
button1.pack()
label2=tkinter.Label(downframe,text="Semantic Analysis")
label2.pack()
text1=tkinter.Text(downframe,width=500)
text1.pack()
root.mainloop()
