# version 4 : on ajoute le graphique et la décision du jury (semestre 1)

import numpy as np
import matplotlib.pyplot as plt

notes = {"R101": 12, "R102": 9.5, "R103": 11, "R104": 8, "R105": 10,
         "R106": 13, "R107": 14, "R108": 12.5, "R109": 15, "R110": 14,
         "R111": 13, "R112": 16, "R113": 7.5, "R114": 9, "R115": 12,
         "SAE11": 13, "SAE12": 14, "SAE13": 11, "SAE14": 15, "SAE15": 12,
         "SAE16": 16}

coef_ue1 = {"R101": 10, "R102": 10, "R103": 7, "R104": 7, "R106": 5,
            "R108": 6, "R110": 5, "R111": 4, "R112": 2, "R113": 5,
            "R114": 5, "SAE11": 20, "SAE12": 20, "SAE16": 7}

coef_ue2 = {"R101": 4, "R103": 2, "R104": 8, "R105": 6, "R110": 5,
            "R111": 5, "R112": 2, "R113": 9, "R114": 9, "R115": 3,
            "SAE13": 29, "SAE16": 7}

coef_ue3 = {"R101": 4, "R103": 2, "R106": 5, "R107": 15, "R108": 6,
            "R109": 4, "R110": 5, "R111": 5, "R112": 2, "R115": 3,
            "SAE14": 20, "SAE15": 20, "SAE16": 7}


def moyenne(notes, coefs):
    liste_notes = []
    liste_coefs = []
    for m in coefs:
        liste_notes.append(notes[m])
        liste_coefs.append(coefs[m])
    return np.average(liste_notes, weights=liste_coefs)


def decision(moyennes):
    nb = 0
    for m in moyennes:
        if m >= 10:
            nb = nb + 1
    if nb == 3:
        return "Année validée : passage en BUT 2 autorisé"
    elif nb == 2 and min(moyennes) >= 8:
        return "Année non validée, passage autorisé : valider l'UE en BUT 2"
    elif nb == 2:
        return "Année non validée, passage non autorisé : redoublement possible"
    else:
        return "Année non validée : passage en BUT 2 exclu"


moyennes = [moyenne(notes, coef_ue1), moyenne(notes, coef_ue2), moyenne(notes, coef_ue3)]
commentaire = decision(moyennes)

print("UE1 :", round(moyennes[0], 2))
print("UE2 :", round(moyennes[1], 2))
print("UE3 :", round(moyennes[2], 2))
print(commentaire)

# graphique
couleurs = []
for m in moyennes:
    if m >= 10:
        couleurs.append("green")
    elif m >= 8:
        couleurs.append("orange")
    else:
        couleurs.append("red")

plt.bar(["UE1", "UE2", "UE3"], moyennes, color=couleurs)
plt.axhline(10, color="black", linestyle="--")
plt.axhline(8, color="gray", linestyle=":")
plt.ylim(0, 20)
plt.ylabel("moyenne")
plt.title("Moyennes des UE (semestre 1)")
plt.xlabel(commentaire)
plt.show()
