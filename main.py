import numpy as np
import sys
import re
from pprint import pprint
from src.FourierMotzkin import FourierMotzkin


if len(sys.argv)<2:
    raise Exception("Missing arguments")

if len(sys.argv)==2:
    c = sys.argv[1]
    if c[0]!='[' or c[-1]!="]":
        raise Exception(f"Invalid syntaxe in {c}")

    #c
    c = re.split(',',c[1:-1])
    c = [coef for coef in c if c!=""]
    try:
        c = [float(coef) for coef in c]
    except ValueError:
        raise Exception(f"Invalid syntaxe in {sys.argv[1]}")

    A=None
    b=None
    c = np.array(c)
    print('c = ',c, '\n\n')

elif len(sys.argv)==3:
    A = sys.argv[1]
    c = sys.argv[2]
    if c[0]!='[' or c[-1]!="]":
        raise Exception(f"Invalid syntaxe in {c}")
    elif A[0:2]!='[[' or A[-2]+A[-1]!=']]':
        raise Exception(f"Invalid syntaxe in {A}")
    
    #c
    c = re.split(',',c[1:-1])
    c = [coef for coef in c if c!=""]
    try:
        c = [float(coef) for coef in c]
    except ValueError:
        raise Exception(f"Invalid syntaxe in {sys.argv[2]}")

    #A
    lines = re.split(r"],\[", A[2:-2])
    A = [re.split(',',line) for line in lines]
    for i,line in enumerate(A):
        try:
            A[i] = [float(coef) for coef in line]
        except ValueError:
            raise Exception(f"Invalid syntaxe in {sys.argv[1]}")
    
    for row1 in A:
        for row2 in A:
            if len(row1)!=len(row2):
                raise Exception("All rows must be of the same length")

    A = np.array(A)
    b = None
    c = np.array(c)
    print('A = ', A, '\n')
    print('c = ', c, '\n\n')

elif len(sys.argv)==4:
    A = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    if c[0]!='[' or c[-1]!="]":
        raise Exception(f"Invalid syntaxe in {c}")
    elif A[0:2]!='[[' or A[-2]+A[-1]!=']]':
        raise Exception(f"Invalid syntaxe in {A}")
    elif b[0]!='[' or b[-1]!=']':
        raise Exception(f"Invalid syntaxe in {b}")
    
    #c
    c = re.split(',',c[1:-1])
    c = [coef for coef in c if c!=""]
    try:
        c = [float(coef) for coef in c]
    except ValueError:
        raise Exception(f"Invalid syntaxe in {sys.argv[3]}")

    #A
    lines = re.split(r"],\[", A[2:-2])
    A = [re.split(',',line) for line in lines]
    for i,line in enumerate(A):
        try:
            A[i] = [float(coef) for coef in line]
        except ValueError:
            raise Exception(f"Invalid syntaxe in {sys.argv[1]}")
    
    for row1 in A:
        for row2 in A:
            if len(row1)!=len(row2):
                raise Exception("All the rows of A must be of the same length")
    
    b = re.split(',',b[1:-1])
    b = [coef for coef in b if b!=""]
    b = [float(coef) for coef in b]

    A = np.array(A)
    b = np.array(b)
    b = np.reshape(b,(len(b),1))
    c = np.array(c)
    print('A = \n', A, '\n')
    print('b = \n', b, '\n')
    print('c = \n', c, '\n\n')

else :
    raise Exception(f"Unexpected argument : {sys.argv[4]}")


if A is not None:
    iA,jA = np.shape(A)

if b is not None:
    ib,jb = np.shape(b)
    if iA!=ib:
        raise Exception("A dimension 0 must match b dimension 0")
if len(c)!=jA:
    raise Exception("A dimension 1 must match c length")


print(FourierMotzkin(A,b,c))