def huszonegyes():
    jatekosL = [5, 12, 15]
    gepL = [8, 14]
 # megoldás
    def osszegzes(lista):
        osszeg = 0
        for i in range(0, len(lista), 1):
            osszeg += lista[i]
        return osszeg

    jatekosL_Osszege = osszegzes(jatekosL)
    gepL_Osszege = osszegzes(gepL)

    # esetek
    if jatekosL_Osszege > 21:
        print("Gép nyert")
    elif gepL_Osszege > 21:
        print("Játékos nyert!")
    elif jatekosL_Osszege > gepL_Osszege:
        print("Játékos nyert")
    elif jatekosL_Osszege < gepL_Osszege:
        print("Gép nyert")
    elif jatekosL_Osszege == gepL_Osszege:
        if len(jatekosL) < len(gepL):
            print("Játékos nyert")
        elif len(jatekosL) > len(gepL):
            print("Gép nyert")
        else:
            print("Döntetlen")
    else:
        print("Valami nem jól sikerült!")