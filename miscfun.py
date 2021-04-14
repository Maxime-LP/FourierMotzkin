import numpy as np

#Fonctions préliminaires
##########################################

def FM1(A,b):
    """
    Concatène verticalement les matrices A et -b
    """
    A=np.array(A,dtype=float)
    b=np.array(b)
    return np.column_stack((A,-b))

def FM2(B):
    """
    Retourne la matrice réduite associée à B
    """
    nb_lignes=np.shape(B)[0]
    for i in range(nb_lignes):
        if B[i,0]!=0 and abs(B[i,0])!=1:
            B[i] /= abs(B[i,0])
    return B

def FM3(C):
    """
    Entrée : Une matrice C_pxq réduite
    Sortie : La projection sur la première variable du système
    """
    p,q = np.shape(C)
    E = np.array([]).reshape(0,q-1)
    G = np.array([]).reshape(0,q-1)
    D = np.array([]).reshape(0,q-1)
    for i in range(p):
        ligne = np.copy(C[i][1:]).reshape(1,q-1)
        if C[i][0] > 0:
            D = np.concatenate((D,-ligne))
        elif C[i][0] < 0:
            G = np.concatenate((G,ligne))
        else:
            E = np.concatenate((E,ligne))
    for g in G:
        for d in D:
            E = np.concatenate((E,(g-d).reshape(1,q-1)))
    
    return E

def bornes(A,nb_variables):
    """
    Entrée : La matrice A réduite définissant un polyèdre et le nombre de variables du système complet (ie non projeté)

    Sortie : L'intervalle [max(formes affines), min(formes affines)] bornant la première variable du système de contraintes Ax<=0
    sous la forme d'une liste de listes de coefficients de formes affines
    """
    output=[[],[]]
    nb_lignes,q=np.shape(A)[0],np.shape(A)[1]-1
    #q est le nombre de variables du système courant et nb_variables est le nombre de variables du système complet

    for i in range(nb_lignes):
        if A[i,0]>0: # x1 + forme affine < 0
            forme_affine = [0 for k in range(nb_variables-q+1)] + list(-A[i,1::])
            output[1].append(forme_affine)

        elif A[i,0]<0: # -x1 + forme affine < 0
            forme_affine = [0 for k in range(nb_variables-q+1)] + list(A[i,1::])
            output[0].append(forme_affine)

    #On regarde si la variable est non bornée
    if output[0]==[]:
        output[0]=[[0 for i in range(nb_variables)] + [-1e16]]
    if output[1]==[]:
        output[1]=[[0 for i in range(nb_variables)] + [1e16]]

    return output

def ChangementDeVariable(A,c,i):
    """
    Changement de variable : u = c1x1 + ... + cqxq 
                             x_k = x_k pour k!=i
    """
    tmp=np.copy(A)
    nb_lignes, nb_variables = np.shape(A)[0], np.shape(A)[1]-1

    for k in range(nb_lignes):
        if A[k,i]!=0:
            for j in range(nb_variables):
                #La constante n'est pas affectée par le changement de variable, on n'a donc pas besoin d'aller jusqu'à la dernière colonne
                if j==i:
                    tmp[k,j]=A[k,i]/c[i]
                else:
                    tmp[k,j]=A[k,j]-A[k,i]*c[j]/c[i]
    return tmp