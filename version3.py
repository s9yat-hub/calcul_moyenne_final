# version 3 : avec des dictionnaires
# test avec R101 et R102 seulement

notes = {"R101": 12, "R102": 9.5}

coef_ue1 = {"R101": 10, "R102": 10}
coef_ue2 = {"R101": 4}
coef_ue3 = {"R101": 4}


def moyenne(notes, coefs):
    somme = 0
    total_coef = 0
    for m in coefs:
        somme = somme + notes[m] * coefs[m]
        total_coef = total_coef + coefs[m]
    return somme / total_coef


print("UE1 :", round(moyenne(notes, coef_ue1), 2))
print("UE2 :", round(moyenne(notes, coef_ue2), 2))
print("UE3 :", round(moyenne(notes, coef_ue3), 2))
