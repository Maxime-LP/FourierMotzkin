# FourierMotzkin
Fourier Motzkin optimization method implementation

Résolution des problèmes d'optimisation sous forme standard par une implémentation de la méthode de Fourier-Motzkin


Utilisation : 

  'python main.py A b c'
  
où A et b sont les matrices des contraintes linéaires Ax<b et c le vecteur des coefficients de la fonction affine à minimiser.
Par défaut, les matrices A et b sont nulles

Forme attendue : 

  A = [[a,b,c],[e,f,g]]
  
  b = [b1,b2]
  
  c = [c1,c2,c3]
