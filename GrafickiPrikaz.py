from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import mpl_toolkits.mplot3d.art3d as art3d

# Definiranje boja za svaku stranu kocke
boje = {
    'W': 'white',
    'O': 'orange',
    'G': 'green',
    'R': 'red',
    'Y': 'yellow',
    'B': 'blue',
}


class PrikazKocke:
    def __init__(self, kocka):
        self.kocka = kocka

    def prikazi_kocku(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Postavljanje parametara osi
        ax.set_xlim(0, 3)
        ax.set_ylim(0, 3)
        ax.set_zlim(0, 3)

        # Prikazivanje svake strane kocke
        for x in range(3):
            for y in range(3):
                # Prikazivanje gornje strane
                self.prikazi_kvadar(ax, x, y, 0, self.kocka.R[y][x], 'y')  # Adjusted indices

                # Prikazivanje lijeve, prednje, desne i donje strane
                self.prikazi_kvadar(ax, x, y, 0, self.kocka.F[y][x], 'x')  # Adjusted indices
                self.prikazi_kvadar(ax, x, y, 3, self.kocka.L[y][x], 'y')  # Adjusted indices
                self.prikazi_kvadar(ax, x, y, 3, self.kocka.U[y][x], 'z')  # Adjusted indices
                self.prikazi_kvadar(ax, x, y, 3, self.kocka.B[y][x], 'x')  # Adjusted indices

                # Prikazivanje stražnje strane
                self.prikazi_kvadar(ax, x, y, 0, self.kocka.D[y][x], 'z')  # Adjusted indices

        plt.draw()
    def prikazi_kvadar(self, ax, x, y, z, boja, axis):
        # Postavljanje položaja i dimenzija kvadra
        color = boje[boja]
        facecolor = 'none'  # Default facecolor
        if axis == 'x':
            facecolor = color
        elif axis == 'y':
            facecolor = color
        elif axis == 'z':
            facecolor = color

        side = Rectangle((x, y), 1, 1, facecolor=facecolor)
        ax.add_patch(side)
        art3d.pathpatch_2d_to_3d(side, z=z, zdir=axis)

