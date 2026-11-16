# version 1 : notes et coefficients saisis au clavier
# je teste avec seulement R101 et R102

note1 = float(input("note de R101 : "))
note2 = float(input("note de R102 : "))

# UE1
coef1 = float(input("coef de R101 dans UE1 : "))
coef2 = float(input("coef de R102 dans UE1 : "))
moy_ue1 = (note1 * coef1 + note2 * coef2) / (coef1 + coef2)
print("moyenne UE1 :", round(moy_ue1, 2))

# UE2
coef1 = float(input("coef de R101 dans UE2 : "))
coef2 = float(input("coef de R102 dans UE2 : "))
moy_ue2 = (note1 * coef1 + note2 * coef2) / (coef1 + coef2)
print("moyenne UE2 :", round(moy_ue2, 2))

# UE3
coef1 = float(input("coef de R101 dans UE3 : "))
coef2 = float(input("coef de R102 dans UE3 : "))
moy_ue3 = (note1 * coef1 + note2 * coef2) / (coef1 + coef2)
print("moyenne UE3 :", round(moy_ue3, 2))
