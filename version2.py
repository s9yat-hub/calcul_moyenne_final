# version 2 : avec des listes
# test avec R101 et R102 seulement

matieres = ["R101", "R102"]
notes = [12, 9.5]

coef_ue1 = [10, 10]
coef_ue2 = [4, 0]
coef_ue3 = [4, 0]


def moyenne(notes, coefs):
    somme = 0
    total_coef = 0
    for i in range(len(notes)):
        somme = somme + notes[i] * coefs[i]
        total_coef = total_coef + coefs[i]
    return somme / total_coef


print("UE1 :", round(moyenne(notes, coef_ue1), 2))
print("UE2 :", round(moyenne(notes, coef_ue2), 2))
print("UE3 :", round(moyenne(notes, coef_ue3), 2))
