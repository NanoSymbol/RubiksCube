import copy

import numpy as np
import random

# pocetno stanje kocke

poz_L = [['O', 'O', 'O'],
         ['O', 'O', 'O'],
         ['O', 'O', 'O']]

poz_R = [['R', 'R', 'R'],
         ['R', 'R', 'R'],
         ['R', 'R', 'R']]

poz_D = [['Y', 'Y', 'Y'],
         ['Y', 'Y', 'Y'],
         ['Y', 'Y', 'Y']]

poz_U = [['W', 'W', 'W'],
         ['W', 'W', 'W'],
         ['W', 'W', 'W']]

poz_B = [['B', 'B', 'B'],
         ['B', 'B', 'B'],
         ['B', 'B', 'B']]

poz_F = [['G', 'G', 'G'],
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

    def rotacijaU_inv(self):
        self.U = np.rot90(self.U, k=1, axes=(0, 1))
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
            self.B[2][i] = R_vec[0][2 - i]
            self.F[0][i] = L_vec[0][i]
            self.L[0][i] = B_vec[0][2 - i]
            self.R[0][i] = F_vec[0][i]


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

    def rotacijaD_inv(self):
        self.D = np.rot90(self.D, k=1, axes=(0, 1))
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
            self.B[0][i] = L_vec[0][2 - i]
            self.F[2][i] = R_vec[0][i]
            self.L[2][i] = F_vec[0][i]
            self.R[2][i] = B_vec[0][2 - i]

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

    def rotacijaR_inv(self):
        self.R = np.rot90(self.R, k=1, axes=(0, 1))
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
            self.B[i][2] = D_vec[0][i]
            self.U[i][2] = B_vec[0][i]
            self.F[i][2] = U_vec[0][i]
            self.D[i][2] = F_vec[0][i]

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

    def rotacijaL_inv(self):
        self.L = np.rot90(self.L, k=1, axes=(0, 1))
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
            self.B[i][0] = U_vec[0][i]
            self.U[i][0] = F_vec[0][i]
            self.F[i][0] = D_vec[0][i]
            self.D[i][0] = B_vec[0][i]

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

    def rotacijaF_inv(self):
        self.F = np.rot90(self.F, k=1, axes=(0, 1))
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
            self.L[i][2] = U_vec[0][2 - i]
            self.U[2][i] = R_vec[0][i]
            self.R[i][0] = D_vec[0][2 - i]
            self.D[0][i] = L_vec[0][i]

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

    def rotacijaB_inv(self):
        self.B = np.rot90(self.B, k=1, axes=(0, 1))
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
            self.L[i][0] = D_vec[0][i]
            self.U[0][i] = L_vec[0][2 - i]
            self.R[i][2] = U_vec[0][i]
            self.D[2][i] = R_vec[0][2 - i]

    # Printa kocku u konzoli za jednostavno iscitavanje
    def rot_x(self):
        U = copy.deepcopy(self.U)
        F = copy.deepcopy(self.F)
        D = copy.deepcopy(self.D)
        B = copy.deepcopy(self.B)
        self.F = D
        self.D = B
        self.U = F
        self.B = U
        self.R = np.rot90(self.R, k=3, axes=(0, 1))
        self.L = np.rot90(self.L, k=1, axes=(0, 1))
    def rot_y_inv(self):
        L = copy.deepcopy(self.L)
        R = copy.deepcopy(self.R)
        F = copy.deepcopy(self.F)
        B = copy.deepcopy(self.B)
        self.F = L
        self.R = F
        self.L = np.rot90(B, k=2, axes=(0, 1))
        self.B = np.rot90(R, k=2, axes=(0, 1))
        self.U = np.rot90(self.U, k=1, axes=(0, 1))
        self.D = np.rot90(self.D, k=3, axes=(0, 1))

    def rot_z(self):
        self.F = np.rot90(self.F, k=1, axes=(0, 1))
        self.B = np.rot90(self.B, k=3, axes=(0, 1))
        L = copy.deepcopy(self.L)
        R = copy.deepcopy(self.R)
        D = copy.deepcopy(self.D)
        U = copy.deepcopy(self.U)
        self.U = R
        self.L = U
        self.D = np.rot90(L, k=2, axes=(0, 1))
        self.R = np.rot90(D, k=2, axes=(0, 1))


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

    # Pozvati funciju za ocitavanje stanja kocke (true/false)

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
        moves_dict = {
            'U': self.rotacijaU,
            "U'": self.rotacijaU_inv,
            'L': self.rotacijaL,
            "L'": self.rotacijaL_inv,
            'F': self.rotacijaF,
            "F'": self.rotacijaF_inv,
            'R': self.rotacijaR,
            "R'": self.rotacijaR_inv,
            'B': self.rotacijaB,
            "B'": self.rotacijaB_inv,
            'D': self.rotacijaD,
            "D'": self.rotacijaD_inv,
            "x": self.rot_x,
            "y'": self.rot_y_inv,
            "z": self.rot_z
        }

        for block in potezi:
            i = 0
            while i < len(block):
                move = block[i]
                if i < len(block) - 1 and block[i + 1] == "'":
                    move += "'"
                    i += 1
                if move in moves_dict:
                    moves_dict[move]()
                i += 1




    # Provodi nasumicne poteze na kocki da ju izmjesa

    def scramble(self):
        moves = ''.join(random.choices("ULFRBD", k=random.randint(100, 200)))
        print(moves)
        self.unos_poteza(moves)


