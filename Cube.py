import numpy as np
import random

# pocetno stanje kocke

poz_L = [['O', 'O', 'O'],
         ['O', 'O', 'O'],
         ['O', 'O', 'O']]

poz_R = [['R', 'R', 'R'],
         ['R', 'R', 'R'],
         ['R', 'R', 'R']]

poz_U = [['Y', 'Y', 'Y'],
         ['Y', 'Y', 'Y'],
         ['Y', 'Y', 'Y']]

poz_D = [['W', 'W', 'W'],
         ['W', 'W', 'W'],
         ['W', 'W', 'W']]

poz_F = [['B', 'B', 'B'],
         ['B', 'B', 'B'],
         ['B', 'B', 'B']]

poz_B = [['G', 'G', 'G'],
         ['G', 'G', 'G'],
         ['G', 'G', 'G']]


class Kocka:

    # Inicializacija kocke

    def __init__(self):
        self.U = np.copy(poz_U)
        self.L = np.copy(poz_L)
        self.F = np.copy(poz_F)
        self.R = np.copy(poz_R)
        self.D = np.copy(poz_D)
        self.B = np.copy(poz_B)

    # Rotacije kocke | Dodati i counterclockwise rotacije kasnije

    def rotacijaU(self):
        self.U = np.rot90(self.U, k=1, axes=(1, 0))
        B_vec = [['', '', '']]
        L_vec = [['', '', '']]
        R_vec = [['', '', '']]
        F_vec = [['', '', '']]
        for i in range(3):
            B_vec[0][i] = self.B[2][i]
            L_vec[0][i] = self.L[0][i]
            F_vec[0][i] = self.F[0][i]
            R_vec[0][i] = self.R[0][i]
        for i in range(3):
            self.B[2][i] = L_vec[0][2 - i]
            self.F[0][i] = R_vec[0][i]
            self.L[0][i] = F_vec[0][i]
            self.R[0][i] = B_vec[0][2 - i]

    def rotacijaD(self):
        self.D = np.rot90(self.D, k=1, axes=(1, 0))
        F_vec = [['', '', '']]
        R_vec = [['', '', '']]
        L_vec = [['', '', '']]
        B_vec = [['', '', '']]
        for i in range(3):
            B_vec[0][i] = self.B[0][i]
            L_vec[0][i] = self.L[2][i]
            F_vec[0][i] = self.F[2][i]
            R_vec[0][i] = self.R[2][i]
        for i in range(3):
            self.B[0][i] = R_vec[0][2 - i]
            self.F[2][i] = L_vec[0][i]
            self.L[2][i] = B_vec[0][2 - i]
            self.R[2][i] = F_vec[0][i]

    def rotacijaR(self):
        self.R = np.rot90(self.R, k=1, axes=(1, 0))
        B_vec = [['', '', '']]
        D_vec = [['', '', '']]
        U_vec = [['', '', '']]
        F_vec = [['', '', '']]
        for i in range(3):
            B_vec[0][i] = self.B[i][2]
            D_vec[0][i] = self.D[i][2]
            F_vec[0][i] = self.F[i][2]
            U_vec[0][i] = self.U[i][2]
        for i in range(3):
            self.B[i][2] = U_vec[0][i]
            self.U[i][2] = F_vec[0][i]
            self.F[i][2] = D_vec[0][i]
            self.D[i][2] = B_vec[0][i]

    def rotacijaL(self):
        self.L = np.rot90(self.L, k=1, axes=(1, 0))
        B_vec = [['', '', '']]
        D_vec = [['', '', '']]
        U_vec = [['', '', '']]
        F_vec = [['', '', '']]
        for i in range(3):
            B_vec[0][i] = self.B[i][0]
            D_vec[0][i] = self.D[i][0]
            F_vec[0][i] = self.F[i][0]
            U_vec[0][i] = self.U[i][0]
        for i in range(3):
            self.B[i][0] = D_vec[0][i]
            self.U[i][0] = B_vec[0][i]
            self.F[i][0] = U_vec[0][i]
            self.D[i][0] = F_vec[0][i]

    def rotacijaF(self):
        self.F = np.rot90(self.F, k=1, axes=(1, 0))
        L_vec = [['', '', '']]
        R_vec = [['', '', '']]
        U_vec = [['', '', '']]
        D_vec = [['', '', '']]
        for i in range(3):
            L_vec[0][i] = self.L[i][2]
            D_vec[0][i] = self.D[0][i]
            R_vec[0][i] = self.R[i][0]
            U_vec[0][i] = self.U[2][i]
        for i in range(3):
            self.L[i][2] = D_vec[0][i]
            self.U[2][i] = L_vec[0][2 - i]
            self.R[i][0] = U_vec[0][i]
            self.D[0][i] = R_vec[0][2 - i]

    def rotacijaB(self):
        self.B = np.rot90(self.B, k=1, axes=(1, 0))
        U_vec = [['', '', '']]
        R_vec = [['', '', '']]
        L_vec = [['', '', '']]
        D_vec = [['', '', '']]
        for i in range(3):
            L_vec[0][i] = self.L[i][0]
            D_vec[0][i] = self.D[2][i]
            R_vec[0][i] = self.R[i][2]
            U_vec[0][i] = self.U[0][i]
        for i in range(3):
            self.L[i][0] = U_vec[0][2 - i]
            self.U[0][i] = R_vec[0][i]
            self.R[i][2] = D_vec[0][2 - i]
            self.D[2][i] = L_vec[0][i]

    # Printa kocku u konzoli za jednostavno iscitavanje

    def printaj_kocku(self):
        matrices = [self.U, self.L, self.F, self.R, self.D, self.B]
        for i in range(3):
            print('   ' + ''.join(matrices[0][i]))
        for i in range(3):
            print(''.join(matrices[1][i]) + ''.join(matrices[2][i]) + ''.join(matrices[3][i]))
        for i in range(3):
            print('   ' + ''.join(matrices[4][i]))
        for i in range(3):
            print('   ' + ''.join(matrices[5][i]))

    # Pozvati funciju za ocitavanje stanja rjesenosti kocke (true/false)

    def rjesenakocka(self):
        global poz_F, poz_R, poz_L, poz_B, poz_D, poz_U
        return (np.array_equal(self.F, poz_F) and
                np.array_equal(self.R, poz_R) and
                np.array_equal(self.L, poz_L) and
                np.array_equal(self.B, poz_B) and
                np.array_equal(self.D, poz_D) and
                np.array_equal(self.U, poz_U))

    # Unos poteza kao string npr. |kocka.unos_poteza("URRFBDDL")|

    def unos_poteza(self, potezi):
        for move in potezi:
            if move == 'U':
                self.rotacijaU()
            elif move == 'L':
                self.rotacijaL()
            elif move == 'F':
                self.rotacijaF()
            elif move == 'R':
                self.rotacijaR()
            elif move == 'B':
                self.rotacijaB()
            elif move == 'D':
                self.rotacijaD()

    # Provodi nasumicne poteze na kocki da ju izmjesa

    def scramble(self):
        moves = ''.join(random.choices("ULFRBD", k=random.randint(100, 200)))
        self.unos_poteza(moves)


