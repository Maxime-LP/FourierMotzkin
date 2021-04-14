import numpy as np
from .miscfun import *

def FourierMotzkin(A,b,c):
    """
    Retourne une solution d'un problème de minimisation sous forme standard avec :
        A et b définissant le polyèdre de contraintes Ax<=b
        c définissant les coefficients de la fonction affine c1x1+...+cnxn
        x_i>=0 pour tout i
    """
    #nombre de variables
    q=len(c)
    ones=-1*np.eye(q)

    #Concaténation et réduction des matrices A et b + ajout des contraintes x_j>0 à la matrice A des contraintes linéaires
    if A is not None:
        p = np.shape(A)[0]
        if b is None: b = np.zeros((p,1))
        ones=np.column_stack((ones,[0 for i in range(q)]))
        A = FM1(A,b)
        A = FM2(A)
        A=np.row_stack((A,ones))

    else:
        A = ones

    #changement de variable u=f(x,y,z)
    var_changee=0
    while var_changee<q:
        if c[var_changee]!=0:
            A=ChangementDeVariable(A,c,var_changee)
            break
        var_changee+=1

    #On place la colonne correspondant à la variable u en avant-dernière colonne
    tmp = np.copy(A)
    A[:,var_changee], A[:,-2] = A[:,-2], tmp[:,var_changee]
    A = FM2(A)

    ###Descente
    BORNES=[]
    for i in range(q):
        BORNES.append(bornes(A,q))
        A=FM2(FM3(A))
    
    ###Remontée
    bornes_inf = [0 for i in range(q)]

    #On regarde dans un premier temps le minimum de u
    bornes_courantes = BORNES[q-1]
    min_possibles = bornes_courantes[0]

    #Au début de la remontée, u est minoré par des formes affines constantes. 
    #Par exemple, si on a effectué le changement de variable u=x, y=y et z=z, cela donne :
    #       u <= max ( 0*z + 0*y + 0*u + c_i) et u >=  min ( 0*z + 0*y + 0*u + c_j)

    #On obtient donc directement l'inf de u, qui est le minimum de la fonction u=f(x,y,z), il nous reste à obtenir les points pour lesquels ce minimum est atteint
    inf = max( [min_possibles[i][q] for i in range(len(min_possibles))] )
    min_f = inf
    bornes_inf[q-1]=inf

    #On continue la remontée
    for k in range(q-2,-1,-1):
        bornes_courantes = BORNES[k]

        #Si le coefficient devant x_k est positif, on prend le minimum de x_k sur P, sinon on prend son maximum
        if c[k]>0:
            extrema_possibles = bornes_courantes[0]
            inf = max( [  sum(   [ bornes_inf[j] * extrema_possibles[i][j] for j in range(q) ]  ) + extrema_possibles[i][q] for i in range(len(extrema_possibles))  ] )
        else :
            extrema_possibles = bornes_courantes[1]
            inf = min( [  sum(   [ bornes_inf[j] * extrema_possibles[i][j] for j in range(q) ]  ) + extrema_possibles[i][q] for i in range(len(extrema_possibles))  ] )
        #extrema_possibles[i][q] correspond à la constante apparaissant dans la forme affine bornant la variable
        
        bornes_inf[k] = inf

    #On a le point de minimum de toutes les variables exceptée x_{var_changee}, on peut cependant facilement le déduire des autres (cf texte),
    # à condition d'intervertir les coefficients des variables que l'on a intervertit :
    c_aux = list(np.copy(c))
    c_aux[var_changee] = c[q-1]
    c_aux[q-1] = c[var_changee]
    min_var_changee = ( bornes_inf[q-1] - sum ( [ c_aux[i]*bornes_inf[i] for i in range(q-1)]) ) / c[var_changee] 

    #Sans oublier que l'on avait échangé les places des variables u / x_{var_changee} et x_q
    #On a en effet une liste bornes_inf = [min(x_1) , ... , min(x_q) , ... , min(x_{var_changee})], on la remet donc dans l'ordre de départ
    bornes_inf[q-1] = bornes_inf[var_changee]
    bornes_inf[var_changee] = min_var_changee

    return {'optimum':min_f, 'x':bornes_inf}