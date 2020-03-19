import sys
import re


operations={
    "/":lambda x,y:x/y,
    "+":lambda x,y:x+y,
    "-":lambda x,y:x-y,
    "*":lambda x,y:x*y,
    "^":lambda x,y:x**y
}

isFloat = lambda x: x.isdigit() and float(x)-int(x)>0 

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
    integers = '[+-]?\d+' #matches negative or positive integers
    decimals = '[+-]?\d+\.\d+' #matches negative or positive decimal numbers
    operators = '(?<=\d)[*/^+-]' #[*/^+-] matches any operator while (?<=\d) ensures that it is preceeded by a number and not another operator
     
    tokens = re.findall(r'{}|{}|{}'.format(operators,decimals,integers), command)

    for op in ["^","/","*","+","-"]:
        tokens=performOperation(tokens,op) 
    return  tokens[0]
def processBraces(string): 
    try:
        float(string)
        return string
    except:
        pass
    pattern = re.compile(r'\((\d+\.?\d?[*/^+-]*)*\)') #match the smallest open and closing brace
    match = re.search(pattern, string) 
    if match: 
        ans = processString(match.group()) 
        newstring = re.sub(pattern,str(ans),string,1)
    else: 
        #no brace found, so process string like that
        newstring = str(processString(string)) 
    return processBraces(newstring) 

def result(string):
    res=processBraces(string)
    if not isFloat(res):
        return res.split(".")[0]
    else:
        return res
args=sys.argv
string=""
if __name__=="__main__":
    for i in args[1:]:
        string+=i
    print(result(string))


