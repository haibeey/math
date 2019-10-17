import sys
import re


operations={
    "/":lambda x,y:x/y,
    "+":lambda x,y:x+y,
    "-":lambda x,y:x-y,
    "*":lambda x,y:x*y,
    "^":lambda x,y:x**y
}
pattern = re.compile(r'\((\d+\.?\d?[*/^+-]?)*\)') #match the smallest open and closing brace
subBracketPattern = r'(\d+(?=[*/^+-]|$)|\d+\.\d+|[*/^+-])'


def removeWhiteSpace(command):
    return re.sub("\s","",command)
    
isFloat = lambda x: x.isdigit() and float(x)-int(x)>0

def globMultipleOperation(tokens):
    returnTokes=[]
    addMe=""

    for t in range(len(tokens)-1):
        # :(
        if tokens[t]=="-":
            if not (tokens[t+1] in operations) and  tokens[t-1] in operations:
                addMe="-"
            else:
                returnTokes.append(str(tokens[t]))
        else:
            returnTokes.append(addMe+str(tokens[t]))
            addMe=""
    returnTokes.append(addMe+str(tokens[-1]))
    return returnTokes



def performOperation(tokens,operate):
    tokens=globMultipleOperation(tokens)

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
    tokens = re.findall(subBracketPattern, command)
    print(tokens,"tokw")
   
    
    for op in ["^","/","*","+","-"]:
        tokens=performOperation(tokens,op)
    
    return  tokens[0]

def processBraces(string): 
    #base case
    try:
        float(string)
        return string
    except:
        pass
    
    match = re.search(pattern, string) 
    print(string)
    if match:
        print(match)
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
    
       