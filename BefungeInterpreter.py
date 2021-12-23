###########
# IMPORTS #
###########

import math
import random

########################
# DEFINING TOKEN TYPES #
########################

TT_PLUS         = 'PLUS'
TT_MINUS        = 'MINUS'
TT_MULT         = 'MULT'
TT_DIV          = 'DIV'
TT_MOD          = 'MOD'
TT_NOT          = 'NOT'
TT_GRTR         = 'GRTR'
TT_RIGHT        = 'RIGHT'
TT_LEFT         = 'LEFT'
TT_UP           = 'UP'
TT_DOWN         = 'DOWN'
TT_RANDIR       = 'RANDIR'
TT_CONLR        = 'CONLR'
TT_CONUD        = 'CONUD'
TT_STR          = 'STR'
TT_DUPE         = 'DUPE'
TT_SWAP         = 'SWAP'
TT_BIN          = 'BIN'
TT_PPRINT       = 'PPRINT'
TT_PPASCII      = 'PPASCII'
TT_SKIP         = 'SKIP'
TT_PUT          = 'PUT'
TT_GET          = 'GET'
TT_INT_INP      = 'INT_INP'
TT_ASCII_INP    = 'ASCII_INP'
TT_END          = 'END'
TT_SPACE        = 'SPACE'
TT_INVALID      = 'INVALID'

#############
# CONSTANTS #
#############

NUMS = "0123456789"
CODE = []

########
# MAIN #
########

def run(code: list):
   global CODE
   CODE = code
   tokens = Tokenise()
   Evaluate(tokens)
    
############
# TOKENISE #
############
           
def Tokenise() -> list:
    ret_code = []
    for i in range(len(CODE) - 1):
        ret_code.append([])
    
    isInString = False

    for i in range(len(CODE) - 1):
        for j in range(len(CODE[i]) - 1):
            curr = CODE[i][j]
            if isInString != True:
                if curr == '+':
                    ret_code[i].append(TT_PLUS)
                elif curr == '-':
                    ret_code[i].append(TT_MINUS)
                elif curr == '*':
                    ret_code[i].append(TT_MULT)
                elif curr == '/':
                    ret_code[i].append(TT_DIV)
                elif curr == '%':
                    ret_code[i].append(TT_MOD)
                elif curr == '!':
                    ret_code[i].append(TT_NOT)
                elif curr == "'":
                    ret_code[i].append(TT_GRTR)
                elif curr == '>':
                    ret_code[i].append(TT_RIGHT)
                elif curr == '<':
                    ret_code[i].append(TT_LEFT)
                elif curr == '^':
                    ret_code[i].append(TT_UP)
                elif curr == 'v':
                    ret_code[i].append(TT_DOWN)
                elif curr == '?':
                    ret_code[i].append(TT_RANDIR)
                elif curr == '_':
                    ret_code[i].append(TT_CONLR)
                elif curr == '|':
                    ret_code[i].append(TT_CONUD)
                elif curr == '"':
                    ret_code[i].append(TT_STR)
                    isInString = not isInString # Inverts current value of isInString
                elif curr == ':':
                    ret_code[i].append(TT_DUPE)
                elif curr == '\\':
                    ret_code[i].append(TT_SWAP)
                elif curr == '$':
                    ret_code[i].append(TT_BIN)
                elif curr == '.':
                    ret_code[i].append(TT_PPRINT)
                elif curr == ',':
                    ret_code[i].append(TT_PPASCII)
                elif curr == '#':
                    ret_code[i].append(TT_SKIP)
                elif curr == 'p':
                    ret_code[i].append(TT_PUT)
                elif curr == 'g':
                    ret_code[i].append(TT_GET)
                elif curr == '&':
                    ret_code[i].append(TT_INT_INP)
                elif curr == '~':
                    ret_code[i].append(TT_ASCII_INP)
                elif curr == '@':
                    ret_code[i].append(TT_END)
                elif str(curr) in NUMS:
                    ret_code[i].append(curr)
                else:
                    ret_code[i].append(TT_SPACE)
            else: # If in a string, the characters will just be appended, not tokenised.
                if curr == '"':
                    ret_code[i].append(TT_STR)
                    isInString = not isInString
                    continue
                ret_code[i].append(curr)
    
    return ret_code


            


############
# EVALUATE #
############

def Evaluate(tokens: list) -> None:
    STEPS = [
        (0, 0),  # Stationary: 0
        (0, 1),  # Right: 1
        (0, -1), # Left: 2
        (-1, 0),  # Up : 3
        (1, 0)  # Down: 4
    ]
    
    flow = STEPS[1]
    stack = []

    i = 0
    j = 0
    curr = tokens[i][j]
    while (i < len(tokens)) and (j < len(tokens[i])):
        curr = tokens[i][j]

        if str(curr) in NUMS:
            stack.append(curr)

        elif curr == TT_PLUS:
            a = stack.pop()
            b = stack.pop()

            stack.append(a + b)

        elif curr == TT_MINUS:
            a = stack.pop()
            b = stack.pop()

            stack.append(b - a)
        
        elif curr == TT_MULT:
            a = stack.pop()
            b = stack.pop()

            stack.append(a * b)

        elif curr == TT_DIV:
            a = stack.pop()
            b = stack.pop()

            stack.append(math.floor(b / a))
        
        elif curr == TT_MOD:
            a = stack.pop()
            b = stack.pop()

            stack.append(b % a)
        
        elif curr == TT_NOT:
            a = stack.pop()

            if a == 0: stack.append(1)
            else: stack.append(0)
        
        elif curr == TT_GRTR:
            a = stack.pop()
            b = stack.pop()

            if b > a : stack.append(1)
            else: stack.append(0)
        
        elif curr == TT_RIGHT:
            flow = STEPS[1]
       
        elif curr == TT_LEFT:
            flow = STEPS[2]
       
        elif curr == TT_UP:
            flow = STEPS[3]
       
        elif curr == TT_DOWN:
            flow = STEPS[4]
        
        elif curr == TT_RANDIR:
            dir = random.randint(1, 4)
            flow = STEPS[dir]
        
        elif curr == TT_CONLR:
            if stack:
                a = stack.pop()
                
                if a == 0: flow = STEPS[1]
                else: flow = STEPS[2]
            else :
                flow = STEPS[1]

        elif curr == TT_CONUD:
            a = stack.pop()

            if a == 0: flow = STEPS[4]
            else: flow = STEPS[3]
        
        elif curr == TT_STR:
            i += flow[0]
            j += flow[1]

            curr = tokens[i][j]
            while curr != TT_STR:
                stack.append(ord(curr))
                i += flow[0]
                j += flow[1]
                curr = tokens[i][j]
        
        elif curr == TT_DUPE:
            if stack:
                a = stack[-1]
                stack.append(a)
            
        elif curr == TT_SWAP:
            a = stack.pop()
            b = stack.pop()

            stack.append(a)
            stack.append(b)
        
        elif curr == TT_BIN:
            a = stack.pop()

        elif curr == TT_PPRINT:
            a = stack.pop()
            print(a, " ", end="")
        
        elif curr == TT_PPASCII:
            a = stack.pop()
            print(chr(a), end="")
        
        elif curr == TT_SKIP:
            i += flow[0]
            j += flow[1]
        
        elif curr == TT_PUT:
            y = stack.pop()
            x = stack.pop()
            val = stack.pop()

            CODE[x][y] = chr(val)
            tokens = Tokenise()
        
        elif curr == TT_GET:
            y = stack.pop()
            x = stack.pop()
            stack.append(chr(CODE[x][y]))
        
        elif curr == TT_INT_INP:
            stack.append(int(input("Enter a integer: ")))
        
        elif curr == TT_ASCII_INP:
            stack.append(ord(input("Enter a character: ")))

        elif curr == TT_END:
            return
        
        #print("END OF CYCLE :", stack)
        i += flow[0]
        j += flow[1]
            