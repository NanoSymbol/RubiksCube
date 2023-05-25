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
* Primjer rotacije U
![RotacijaU](https://github.com/NanoSymbol/RubiksCube/blob/main/rotacijaU.jpg)

# Evolucijski algoritam
* Rješava kocku iz seta predefiniranih poteza na kocki
* Dio najboljih rješenja ide u sljedeću generaciju bez modifikacija (elitizam osigurava održavanje najboljeg mogućeg rješenja, inače može algoritam nazadovati)
* Križanje se odvija na svim članovima osim najboljih rješenja
* Svaki član mutira na bazi šanse iz seta predodređenih mutacija (npr. nasumična rotacija i nasumični potez ili nasumična rotacija i 3 nasumična poteza)
* Fitness se određuje brojanjem točno pozicioniranih boja na licu
* Najbolji fitness iz generacije se ispisiva u konzolu i prikazuje vizualno
* Kada je fitness jednak 54 kocka je rješena
* Parametri (populacija:200, generacije:500, min/max potezi(pri generiranju prve populacije): 2/4, postotak elitizma - 6%)

# Pokretanje algoritma
* Staviti u isti folder Cube_v2.py, Evolucijski_v2.py, GrafickiPrikaz.py
* Instalirati potrebne bibioteke ako je potrebno ('pip install matplotlib' i 'pip install numpy')
* Pogram pokrenuti s (>'python Evolucijski_v2.py') 

# Poznati bug-ovi
* U rjetkim slučajevima dogodi se nepoznat ilegalan potez i kocka postane nerješiva(treba ponovo pokrenuti program)
* 3d vizualizacija precrtava elemente jedna preko druge pa mogu biti par pogrešno prikazanih elemenata
* 3d vizualizacija zatvara i otvara prozor umjesto updejtanja novog stanja
* Nije poznato postoje li slučajevi pri kojima se kocka ne može rješiti(fali neki određen algoritam)
