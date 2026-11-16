# version 5 : interface avec tkinter (semestre 1)

import numpy as np
from tkinter import *
from tkinter import messagebox

matieres = ["R101", "R102", "R103", "R104", "R105", "R106", "R107", "R108",
            "R109", "R110", "R111", "R112", "R113", "R114", "R115",
            "SAE11", "SAE12", "SAE13", "SAE14", "SAE15", "SAE16"]

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
        return "Année non validée, passage autorisé :\nvalider l'UE en BUT 2"
    elif nb == 2:
        return "Année non validée, passage non autorisé :\nredoublement possible"
    else:
        return "Année non validée :\npassage en BUT 2 exclu"


def graphique(moyennes):
    canevas.delete("all")
    for i in range(3):
        x = 50 + i * 100
        hauteur = moyennes[i] * 10
        if moyennes[i] >= 10:
            couleur = "green"
        elif moyennes[i] >= 8:
            couleur = "orange"
        else:
            couleur = "red"
        canevas.create_rectangle(x, 220 - hauteur, x + 60, 220, fill=couleur)
        canevas.create_text(x + 30, 210 - hauteur, text=str(round(moyennes[i], 2)))
        canevas.create_text(x + 30, 235, text="UE" + str(i + 1))
    canevas.create_line(20, 120, 340, 120)


def calculer():
    notes = {}
    for m in matieres:
        texte = cases[m].get().replace(",", ".")
        if texte == "":
            messagebox.showerror("Erreur", "il manque la note de " + m)
            return
        notes[m] = float(texte)

    moyennes = [moyenne(notes, coef_ue1), moyenne(notes, coef_ue2), moyenne(notes, coef_ue3)]

    texte = ""
    for i in range(3):
        texte = texte + "UE" + str(i + 1) + " : " + str(round(moyennes[i], 2)) + "\n"
    texte = texte + "\n" + decision(moyennes)
    resultat.config(text=texte)
    graphique(moyennes)


def effacer():
    for m in matieres:
        cases[m].delete(0, END)
    resultat.config(text="")
    canevas.delete("all")


fenetre = Tk()
fenetre.title("Moyennes BUT 1")

gauche = Frame(fenetre)
gauche.grid(row=0, column=0, padx=10, pady=10)
droite = Frame(fenetre)
droite.grid(row=0, column=1, padx=10, pady=10)

cases = {}
for i in range(len(matieres)):
    Label(gauche, text=matieres[i]).grid(row=i, column=0)
    cases[matieres[i]] = Entry(gauche, width=6)
    cases[matieres[i]].grid(row=i, column=1)

Button(droite, text="Calculer", command=calculer).pack()
Button(droite, text="Effacer", command=effacer).pack()
resultat = Label(droite, text="")
resultat.pack(pady=10)
canevas = Canvas(droite, width=360, height=250, bg="white")
canevas.pack()

fenetre.mainloop()
