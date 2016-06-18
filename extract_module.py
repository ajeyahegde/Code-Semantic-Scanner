import os
from proj2 import checksyntax
c=[]
c1=[]
directory="C:\\Users\Ajeya\Javafiles"
for content in os.listdir(directory):
    x=directory+"\\"+content
    if(x.endswith(".java")):
        checksyntax(x)

