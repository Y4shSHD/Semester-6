#!/usr/bin/python3
import re

f = open('test2.c','r')

operators = { '=': 'Assignment Operator',
              '+': 'Additon Operator',
              '-' : 'Substraction Operator',
              '/' : 'Division Operator',
              '*': 'Multiplication Operator',
              '++' : 'increment Operator',
              '--' : 'Decrement Operator',
              '==' : 'Assignment Operator'
            }
optr_keys = operators.keys()

comments = {r'//' : 'Single Line Comment',
            r'/*' : 'Multiline Comment Start', r'*/' : 'Multiline Comment End',
            '/**/' : 'Empty Multiline comment'
           }
comment_keys = comments.keys()

header = {'.h': 'header file'}
header_keys = header.keys()

sp_header_files = {'<stdio.h>':'Standard Input Output Header',
		   '<stdlib.h>': 'Standard Library header', 
                   '<string.h>':'String Manipulation Library',
                   '<math.h>': 'Mathematical Functions',
                   '<conio.h>':'An Obsolete library, for running programs in TurboC/C++!'
		  }

macros = {r'#\w+' : 'macro'}
macros_keys = macros.keys()

datatype = {'int': 'Integer',
            'float' : 'Floating Point',
            'char': 'Character',
            'long': 'long int'
           }
datatype_keys = datatype.keys()

keyword = {'return' : 'keyword that returns a value from a block'}
keyword_keys = keyword.keys()

delimiter = {';':'terminator symbol semicolon (;)'}
delimiter_keys = delimiter.keys()

blocks = {'{' : 'Blocked Statement Body Open', '}':'Blocked Statement Body Closed'}
block_keys = blocks.keys()

builtin_functions = {'printf':'printf prints its argument on the console',
                     'scanf': 'scanf takes input from the user'
                    }

non_identifiers = ['_','-','+','/','*','`','~','!','@','$','#','%','^','&','*','(',')','=','|','"',':',';','{'
,'}','[',']','<','>','?','/']

numerals = ['0','1','2','3','4','5','6','7','8','9']

# Flags
dataFlag = False


i = f.read()

count = 0
program =  i.split('\n')
for line in program:
    count = count+1
   
    print("\n\r")
    print ("Line #",count,": ",line,"\n")    
     
    tokens = line.split(' ')
    print ("Tokens are",tokens)
    print ("Line #",count,'properties \n')
    for token in tokens:
        
        if '\r' in token:
            position = token.find('\r')
            token=token[:position]
        # print 1
        
        if token in block_keys:
            for i,j in enumerate(block_keys):
                if j == token:
                 print ("DType[",i,"]")
            #print (blocks[token])
	    
        if token in datatype_keys:            
            for i,j in enumerate(datatype_keys):
                if j == token:
                 print ("DType[",i,"]")
            #print ("Datatype used: ", datatype[token])
            
        if token in optr_keys:
            for i,j in enumerate(optr_keys):
                if j == token:
                 print ("Operator[",i,"]")
            #print ("Operator is: ", operators[token])

        if token in comment_keys:
            for i,j in enumerate(comment_keys):
                if j == token:
                 print ("CommentType[",i,"]")
            #print ("Comment Type: ", comments[token])

        if token in macros_keys:
            for i,j in enumerate(macros_keys):
                if j == token:
                 print ("DType[",i,"]")
            print ("Macro is: ", macros[token])

        if '.h' in token:
            print ("Header File is: ",token, sp_header_files[token])
        if '()' in token:
            print ("Function named", token)
        
        if dataFlag == True and (token not in non_identifiers) and ('()' not in token):
            print ("Identifier: ",token)
        if token in datatype_keys:
            print ("type is: ", datatype[token])
            dataFlag = True
        
        if token in keyword_keys:
            for i,j in enumerate(keyword_keys):
                if j == token:
                 print ("KType[",i,"]")
            print (keyword[token])
            
        if token in delimiter:
            for i,j in enumerate(delimiter_keys):
                if j == token:
                 print ("DeType[",i,"]")
            print ("Delimiter" , delimiter[token])
        if '#' in token:
            match = re.search(r'#\w+', token)
            print ("Macro", match.group())
        if token in numerals:
            print (token,type(int(token)))
            
    dataFlag = False   
            
    
    print ("________________________")
    

f.close()
