# FourierMotzkin
Fourier Motzkin optimization method implementation

Résolution par une implémentation de la méthode de Fourier-Motzkin des problèmes d'optimisation sous forme standard i.e des problèmes de minimisation avec contrainte de positivité des variables.


Utilisation : 

  './main.py A b c'
  
où A et b sont les matrices des contraintes linéaires Ax<b et c le vecteur des coefficients de la fonction affine à minimiser.
Si omis, le vecteur b est nul. Si la matrice A est aussi omise, elle vaut -I.

Formes attendues : 

  A = [[a,b,c],[e,f,g]]
  
  b = [b1,b2]
  
  c = [c1,c2,c3]
