class NbMaya:
    def __init__(self, largeur, hauteur, nb):
        self.repr = [['.' for _ in range(l)] for _ in range(h)]
        self.l = largeur
        self.h = hauteur
        self.nb = nb

    def update(self, ligne, str_repr):
        for i, chara in enumerate(str_repr):
            self.repr[ligne][i] = chara

    def __eq__(self, other):
        for i in range(l):
            for k in range(h):
                if self.repr[i][k] != other.repr[i][k]:
                    return False

        return True

    def print(self):
        for ligne in self.repr:
            print(''.join(ligne))


l, h = [int(i) for i in input().split()]

alphabet = [NbMaya(l, h, i) for i in range(20)]
for i in range(h):
    numeral = input()
    for j in range(0, len(numeral), l):
        lettre = alphabet[j // l]
        lettre.update(i, numeral[j:j + l])

s1 = int(input())
nb1 = [NbMaya(l, h, -1) for _ in range(0, s1, h)]

for i in range(s1):
    num_1line = input()
    nb1[i // h].update(i % h, num_1line)

for chiffre in nb1:
    for lettre in alphabet:
        if chiffre == lettre:
            chiffre.nb = lettre.nb
            break

s2 = int(input())
nb2 = [NbMaya(l, h, -1) for _ in range(0, s2, h)]

for i in range(s2):
    num_2line = input()
    nb2[i // h].update(i % h, num_2line)

for chiffre in nb2:
    for lettre in alphabet:
        if chiffre == lettre:
            chiffre.nb = lettre.nb
            break

operation = input()

nb1_int = 0
for i, chiffre in enumerate(nb1):
    nb1_int += (20 ** (len(nb1) - i - 1)) * chiffre.nb

nb2_int = 0
for i, chiffre in enumerate(nb2):
    nb2_int += (20 ** (len(nb2) - i - 1)) * chiffre.nb


if operation == "*":
    total = nb1_int * nb2_int
elif operation == "/":
    total = nb1_int / nb2_int
elif operation == "+":
    total = nb1_int + nb2_int
else:
    total = nb1_int - nb2_int

rep_total_base_20 = []
rep_puissance = []
i = 20
while i != -1:
    quot, reste = divmod(total, (20 ** i))

    if quot > 0:
        rep_total_base_20.append(quot)
        rep_puissance.append(1)
        total = reste
    else:
        if i != 0:
            rep_total_base_20.append(0)
            rep_puissance.append(0)
        else:
            rep_total_base_20.append(reste)
            rep_puissance.append(1)

    i -= 1

repr_total_maya = []
first_found = False
for i in range(len(rep_puissance)):
    if rep_puissance[i] == 1:
        first_found = True
        for lettre in alphabet:
            if lettre.nb == rep_total_base_20[i]:
                repr_total_maya.append(lettre)
                break
    elif first_found:
        repr_total_maya.append(alphabet[0])

for lettre in repr_total_maya:
    lettre.print()
