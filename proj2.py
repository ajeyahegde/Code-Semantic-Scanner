def checksyntax(directory):
    import re
    def CheckIf():
        x=re.match(p2,lines)
        if(x==None):
            return 0
        else:
            return 1
    def CheckDatatype():
        x=re.match(p3,lines)
        if(x==None):
            return 0
        else:
            return 1
    def CheckWhile():
        x=re.match(p4,lines)
        if(x==None):
            return 0
        else:
            return 1
    def CheckTry():
        x=re.match(p5,lines)
        if(x==None):
            return 0
        else:
            return 1
    def CheckFor():
        x=re.match(p7,lines)
        if(x==None):
            return 0
        else:
            return 1
    def CheckPublic():
        x=re.match(p8,lines)
        if(x==None):
            return 0
        else:
            return 1
    def CheckClass():
        x=re.match(p9,lines)
        if(x==None):
            return 0
        else:
            return 1
    p1="(if|while|for|try|int|float|String|class|public|private)"
    p2="\s*if\s\(\w+\s(==|!=|<|>|>=|<=)\s\w+\)\s{\n"
    p3="(\s*(int|float|String)\s\w+\;)|(\s*(int|float|String)\s\w+\s\=\s\w+\;)|(\s*(int|float|String)\s\w+\s\=\s\w+\s(\+|\-|\*)\s\w+\;)"
    p4="\s*while\s\(\w+\s(==|!=|<|>|>=|<=)\s\w+\)\s{\n"
    p5="\s*try\s\{"
    p6="\s*\}\scatch\s\(\w+\s\w+\)\s{\n"
    p7="\s*for\s\(\s(int\s\w+\s\=\s(\w+|\d+)|\w+\s\=\s(\w+|\d+)|)\;\s\w+(<=|>=|<|>|==|!=)\d+\s\;\s\w+(\+\+|\-\-)\s\)\s\{"
    p8="\s*(public|private)\sclass\s\w+\s*\n"
    p9="\s*\class\s\w+\s*\n"
    f=open(directory,"r")
    print("This is for file",directory)
    count=1
    bracketcount=0
    trymatch=0
    for lines in f.readlines():
        l=lines.split()
        if(len(l)==0):
            count=count+1
            continue
        if(re.match(p1,l[0])!=None):
            if(l[0]=="if"):
                x=CheckIf()
                if(x==0):
                    print("Line ",count," should be of the form 'if (variable (==|!=|>|<|>=|<=) variable) {'")
                    print(lines)
                else:
                    bracketcount=bracketcount+1
            elif(l[0]=="while"):
                x=CheckWhile()
                if(x==0):
                    print("Line ",count," should be of the form 'while (variable (==|!=|>|<|>=|<=) variable) {'")
                    print(lines)
                else:
                    bracketcount=bracketcount+1
            elif(l[0]=="for"):
                x=CheckFor()
                if(x==0):
                    print("Line ",count," should be of the form 'for ( int variable = integer; variable<5 ; variable++) {'")
                    print(lines)
                else:
                    bracketcount=bracketcount+1
            elif(l[0]=="try"):
                x=CheckTry()
                if(x==0):
                    print("Line ",count," should be of the form 'try {'")
                    print(lines)
                else:
                    trymatch=trymatch+1
            elif(l[0]=="int" or "float" or "String"):
                x=CheckDatatype()
                if(x==0):
                    print("Line ",count," should be of the form 'variabletype variable = variable + variable;'")
                    print(lines)
            elif(l[0]=="class"):
                x=CheckClass()
                if(x==0):
                    print("Line ",count," should be of the form 'classtype class classname'")
                    print(lines)
                else:
                    bracketcount=bracketcount+1
            elif(l[0]=="public" or l[0]=="private"):
                x=CheckPublic()
                if(x==0):
                    print("Line ",count," should be of the form 'classtype class classname'")
                    print(lines)
                else:
                    bracketcount=bracketcount+1
        if(l[0]=="}"):
            x=re.match(p6,lines)
            if(x!=None):
                trymatch=trymatch-1
                bracketcount=bracketcount+1
                count=count+1
                continue
            x=re.match("\s*\}\s*\n|\s*\}\s*//",lines)
            if(x!= None):
                bracketcount=bracketcount-1
            else:
                print("There shud be only bracket in a line")
        count=count+1
    if(bracketcount!=0 and trymatch!=0):
        print("There is some semantic error in file")
    print("____________________________________________________________________________________________________")
    f.close()
