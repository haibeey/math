import sys
import re


operations={
    "/":lambda x,y:x/y,
    "+":lambda x,y:x+y,
    "-":lambda x,y:x-y,
    "*":lambda x,y:x*y,
    "^":lambda x,y:x**y
}
def removeWhiteSpace(command):
    return re.sub("\s","",command)
    
def performOperation(tokens,operate):
    stack=[]
    lentokens=len(tokens)
    index=0
    while index<lentokens:
        operation=tokens[index]
        if operation==operate:
            value=int(stack.pop())
            if index+1>= lentokens:
                raise ValueError("could not process this string.\n are you missing a value?")
            valuenext=int(tokens[index+1])
            stack.append(operations[operate](value,valuenext))
            index= index+2
        else:
            stack.append(operation)
            index=index+1
    return stack
    
def tokenize(string):
    resultTokens=[]
    stack=[]
    count=0
    countPrev=0
    matchnumbers=re.compile("(\d+)")
    i=0 #index of string
    lenstring=len(string)

    while i<lenstring:
        c=string[i] #char of string
        if c=="(":
            if not stack:
                countPrev=i
            stack.append(0)
            count= count+ 1
            i=i+1
        elif c==")":
            count= count+1
            stack.pop()
            if not stack:
                resultTokens.append(string[countPrev:countPrev+count])
                count=0
            i=i+1
        elif c in ["/","+","-","*","^"]:
            if stack:
                count=count +1
            else:
                resultTokens.append(c)
            i=i +1
        else:
            if stack:
                count=count +1
                i=i+1
            else:
                a,b=matchnumbers.match(string[i:]).span() #find matching numbers
                resultTokens.append(string[i:i+b])
                i=i+b
    return resultTokens

def processString(command):
    command=removeWhiteSpace(command)
    lenghts=len(command)
    if command[0]=="(":
        if command[-1]!=")":
            raise  ValueError("invalid command")
        command=command[1:lenghts-1] # remove the braces
    tokens=tokenize(command)
    solveBraces=[]
    for toks in tokens:
        if toks[0]=="(": #first value is a brace
            solveBraces.append(processString(toks))
        else:
            solveBraces.append(toks)

    #using bodmas rule solve division first then multiplication 
    # then addition then subtraction

    for op in ["^","/","*","+","-"]:
        solveBraces=performOperation(solveBraces,op)
    return  solveBraces[0]
args=sys.argv
string=""
for i in args[1:]:
    string+=i

print(processString(string))