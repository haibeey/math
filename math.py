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
            value=float(stack.pop())
            if index+1>= lentokens:
                raise ValueError("could not process this string.\n are you missing a value?")
            valuenext=float(tokens[index+1])
            stack.append(operations[operate](value,valuenext))
            index= index+2
        else:
            stack.append(operation)
            index=index+1
    return stack 

def processString(command):
    command=removeWhiteSpace(command)
    lenghts=len(command)
    if command[0]=="(":
        if command[-1]!=")":
            raise  ValueError("invalid command")
        command=command[1:lenghts-1] # remove the braces
    tokens = re.findall(r'(\d+(?=[*/^+-]|$)|\d+\.\d+|[*/^+-])', command)    
    #tokens = re.findall(r'(\d+|[*/^+-])', command)     #using bodmas rule solve division first then multiplication 
    # then addition then subtraction

    for op in ["^","/","*","+","-"]:
        tokens=performOperation(tokens,op) 
    return  tokens[0]
def processBraces(string): 
    try:
        float(string)
        print(string)
        return
    except:
        pass
    pattern = re.compile(r'\((\d+\.?\d?[*/^+-]?)*\)') #match the smallest open and closing brace
    match = re.search(pattern, string) 
    if match: 
        ans = processString(match.group()) 
        newstring = re.sub(pattern,str(ans),string,1)
    else: 
        #no brace found, so process string like that
        newstring = str(processString(string)) 
    processBraces(newstring) 
 
args=sys.argv
string=""
if __name__=="__main__":
    for i in args[1:]:
        string+=i
    processBraces(string) 