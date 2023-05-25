import matplotlib.pyplot as plt
from Cube import Kocka
from GrafickiPrikaz import PrikazKocke

kocka = Kocka()
kocka.scramble()
kocka.unos_poteza("F D D R L U F F R F U L D F U F L D L F F D L L F L D D U D R L F R F F L D F U D U R D R F U D F D D R U D D F F L R U D R F R F U R D F U L D U U D U D L R L U D ")
kocka_prikaz = PrikazKocke(kocka)
kocka_prikaz.prikazi_kocku()
plt.show()
kocka.printaj_kocku()

