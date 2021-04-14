import numpy as np
from src.FourierMotzkin import FourierMotzkin

###############
#Tests
#A=[[-5,2,5]]
A=[[-1.,0,0],[1,0,0],[0,1,0],[0,0,1]]
#b=[6]
b=[-0.5,1,1,4]
print(FourierMotzkin(A,b,[1,-1,1]))