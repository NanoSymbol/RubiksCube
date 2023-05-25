# RubiksCube

# Skripta koja rješava rubikovu kocku evolucijskim algoritmom iz predefiniranih setova poteza na kocki

Simulacija kocke napravljena je u "Cube_v2.py"

Evolucijski algoritam nalazi se u "Evolucijski_v2.py"

Grafički prikaz za rješenja nalazi se u "GrafickiPrikaz.py"

Potrebne bibilioteke"matplotlib,numpy"

# Simulacija kocke
* Sastoji se od 12 poteza kocke ["U ", "R ", "L ", "D ", "F ", "B ", "U' ", "R' ", "L' ", "D' ", "F' ", "B' "]
* Slovo označava na kojem licu kocke se odvija potez, potezi bez " ' " su u smjeru kazaljke na satu, dok oni s " ' " označavaju poteze u smjeru suprotnom od kazaljke na satu
* Rotiranje kocke se odvija u 3 osi ["x", "y", "z"]
## Primjer rotacije U
'def rotacijaU(self):
        self.U = np.rot90(self.U, k=1, axes=(1, 0))
        B_vec, L_vec, R_vec, F_vec = self.B[2, :].copy(), self.L[0, :].copy(), self.R[0, :].copy(), self.F[0, :].copy()
        self.B[2, :] = L_vec[::-1]
        self.F[0, :] = R_vec
        self.L[0, :] = F_vec
        self.R[0, :] = B_vec[::-1]'
