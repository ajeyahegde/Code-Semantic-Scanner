import re
def checkif():
    x=re.match(p2,lines)
    if(x==None):
        return 0
    else:
        return 1
def checkdatatype():
    x=re.match(p3,lines)
    if(x==None):
        return 0
    else:
        return 1
def checkwhile():
    x=re.match(p4,lines)
    if(x==None):
        return 0
    else:
        return 1
def checktry():
    x=re.match(p5,lines)
    if(x==None):
        return 0
    else:
        return 1
def checkfor():
    x=re.match(p7,lines)
    if(x==None):
        return 0
    else:
        return 1
def checkpublic():
    x=re.match(p8,lines)
    if(x==None):
        return 0
    else:
        return 1
def checkclass():
    x=re.match(p9,lines)
    if(x==None):
        return 0
    else:
        return 1
#f=open("sample.txt","w")
#f.write(" if (a == b) {\nsomething is written\nfor ( x = 1; x<50 ; x++ ) {\nint x = y;\n } \n  while (a <= b) {\n try { \n } catch (except x) {\n }\n}\n")
#f.close()
p1="(if|while|for|try|int|float|string|class|public|private)"
p2="\s*if\s\(\w+\s(==|!=|<|>|>=|<=)\s\w+\)\s{\n"
p3="(\s*(int|float|string)\s\w+\;)|(\s*(int|float|string)\s\w+\s\=\s\w\;)"
p4="\s*while\s\(\w+\s(==|!=|<|>|>=|<=)\s\w+\)\s{\n"
p5="\s*try\s\{"
p6="\s*\}\scatch\s\(\w+\s\w+\)\s{\n"
p7="\s*for\s\(\s(int\s\w+\s\=\s(\w+|\d+)|\w+\s\=\s(\w+|\d+)|)\;\s\w+(<=|>=|<|>|==|!=)\d+\s\;\s\w+(\+\+|\-\-)\s\)\s\{"
p8="\s*(public|private)\sclass\s\w+\s*\n"
p9="\s*\class\s\w+\s*\n"
f=open("sample.txt","r")
count=1
bracketcount=0
trymatch=0
for lines in f.readlines():
    l=lines.split()
    print(lines)
    print(l)
    if(re.match(p1,l[0])!=None):
        if(l[0]=="if"):
            x=checkif()
            print(x)
            if(x==0):
                print("error in line",count)
            else:
                bracketcount=bracketcount+1
        elif(l[0]=="while"):
            x=checkwhile()
            print(x)
            if(x==0):
                print("error in line",count)
            else:
                bracketcount=bracketcount+1
        elif(l[0]=="for"):
            x=checkfor()
            print(x)
            if(x==0):
                print("error in line",count)
            else:
                bracketcount=bracketcount+1
        elif(l[0]=="try"):
            x=checktry()
            print(x)
            if(x==0):
                print("error in line",count)
            else:
                trymatch=trymatch+1
        elif(l[0]=="int" or "float" or "string"):
            x=checkdatatype()
            print(x)
            if(x==0):
                print("error in line",count)
        elif(l[0]=="class"):
            x=checkclass()
            print(x)
            if(x==0):
                print("error in line",count)
            else:
                bracketcount=bracketcount+1
        elif(l[0]=="public" or l[0]=="private"):
            x=checkpublic()
            print(x)
            if(x==0):
                print("error in line",count)
            else:
                bracketcount=bracketcount+1
    if(l[0]=="}"):
        x=re.match(p6,lines)
        if(x!=None):
            print("1")
            trymatch=trymatch-1
            bracketcount=bracketcount+1
            count=count+1
            print("bracketcount",bracketcount)
            continue
        x=re.match("\s*\}\s*\n",lines)
        if(x!= None):
            bracketcount=bracketcount-1
        else:
            print("There shud be only bracket in a line")
    count=count+1
    print("bracket count",bracketcount)
    print("trymatch",trymatch)
f.close()
