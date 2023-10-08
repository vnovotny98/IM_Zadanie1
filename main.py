# Importujeme potrebné knižnice
import csv
import math
import numpy as np

# Otvoríme CSV súbor - uložený v rovnakom priečinku ako skript
with open('matlabmja.csv', 'r') as file:
    # Vytvoríme inštanciu čítača, ktorý vytvorí "list listov" s ; ako oddeľovačom
    reader = csv.reader(file, delimiter=';')
    # Uložíme dáta
    data_list = list(reader)
    # Odstránime prvý "riadok" (u , y)
    data_list = data_list[1:]

# Súbor sa uzavrie automaticky pri opustení bloku 'with'

# Vytvoríme listy pre údaje 'u' a 'y'
list_u = [float(sublist[0]) for sublist in data_list]
list_y = [float(sublist[1]) for sublist in data_list]


# Definujeme funkciu na výpočet strednej hodnoty
def spocitaj_strednu_hodnotu(list):
    """
    Vypočíta a vráti strednú hodnotu (priemer) listu čísel.

    Args:
        list: List čísel, pre ktorý chceme vypočítať strednú hodnotu.

    Returns:
        float: Stredná hodnota listu.
    """
    stredna_hodnota = 0
    suma = 0
    for i in range(len(list)):
        suma += float(list[i])

    stredna_hodnota = (1 / len(list)) * suma

    return stredna_hodnota


# Definujeme funkciu na výpočet rozptylu
def spocitaj_rozptyl(list, stredna_hodnota):
    """
    Vypočíta a vráti rozptyl listu čísel.

    Args:
        list: List čísel, pre ktorý chceme vypočítať rozptyl.
        stredna_hodnota: Stredná hodnota listu.

    Returns:
        float: Rozptyl listu.
    """
    rozptyl = 0
    suma = 0
    for i in range(len(list)):
        suma += pow((float(list[i]) - stredna_hodnota), 2)

    rozptyl = (1 / len(list)) * suma

    return rozptyl


# Definujeme funkciu na výpočet kovariácie
def spocitaj_kovariaciu(list1, list2, stredna_hodnota1, stredna_hodnota2):
    """
    Vypočíta a vráti kovariáciu medzi dvoma listami čísel.

    Args:
        list1: Prvý list čísel.
        list2: Druhý list čísel.
        stredna_hodnota1: Stredná hodnota prvého listu.
        stredna_hodnota2: Stredná hodnota druhého listu.

    Returns:
        float: Kovariácia medzi listami.
    """
    suma = 0
    for i in range(len(list1)):
        suma += ((float(list1[i]) - stredna_hodnota1) * (float(list2[i]) - stredna_hodnota2))

    kovariacia = (1 / len(list1)) * suma

    return kovariacia


# Definujeme funkciu na výpočet koeficientu korelácie
def spocitaj_koeficient_korelacie(kovariacia, smer_odchylka1, smer_odchylka2):
    """
    Vypočíta a vráti koeficient korelácie medzi dvoma listmi čísel.

    Args:
        kovariacia: Kovariácia medzi listami.
        smer_odchylka1: Smerodajná odchýlka prvého listu.
        smer_odchylka2: Smerodajná odchýlka druhého listu.

    Returns:
        float: Koeficient korelácie.
    """
    koeficient_korelacie = kovariacia / (smer_odchylka1 * smer_odchylka2)

    return koeficient_korelacie


# Definujeme funkciu na výpočet autokorelačnej funkcie
def spocitaj_autokorelacnu_funkciu(list):
    """
    Vypočíta a vráti autokorelačnú funkciu pre zadaný list hodnôt.

    Args:
        list: List hodnôt.

    Returns:
        list: Autokorelačná funkcia.
    """
    vysledok = []
    suma = 0
    maximalny_posun = int(0.1 * len(list))
    for i in range(maximalny_posun):
        for k in range(len(list) - maximalny_posun):
            suma += float(list[k] * list[k + i])

        suma = (1 / (len(list) - i)) * suma
        vysledok.append(suma)

    return vysledok


# Definujeme funkciu na výpočet vzájomnej korelacnej funkcie
def spocitaj_vzajomne_korelacnu_funkciu(list1, list2):
    """
    Vypočíta a vráti vzájomnú korelačnú funkciu medzi dvoma listami hodnôt.

    Args:
        list1: Prvý list hodnôt.
        list2: Druhý list hodnôt.

    Returns:
        list: Vzájomne korelačná funkcia.
    """
    vysledok = []
    suma = 0
    maximalny_posun = int(0.1 * len(list1))
    for i in range(maximalny_posun):
        for k in range(len(list1) - maximalny_posun):
            suma += float(list1[k] * list2[k + i])

        suma = (1 / (len(list1) - i)) * suma
        vysledok.append(suma)

    return vysledok


# Spočítame stredné hodnoty pre 'u' a 'y'
stredna_hodnota_u = spocitaj_strednu_hodnotu(list_u)
stredna_hodnota_y = spocitaj_strednu_hodnotu(list_y)

# Spočítame rozptyly pre 'u' a 'y'
rozptyl_u = spocitaj_rozptyl(list_u, stredna_hodnota_u)
rozptyl_y = spocitaj_rozptyl(list_y, stredna_hodnota_y)

# Spočítame smerodajné odchýlky pre 'u' a 'y'
smer_odchylka_u = math.sqrt(rozptyl_u)
smer_odchylka_y = math.sqrt(rozptyl_y)

# Spočítame kovariáciu medzi 'u' a 'y'
kovariacia_u_y = spocitaj_kovariaciu(list_u, list_y, stredna_hodnota_u, stredna_hodnota_y)

# Spočítame koeficient korelácie
koeficient_korelacie = spocitaj_koeficient_korelacie(kovariacia_u_y, smer_odchylka_u, smer_odchylka_y)

# Vypíšeme výsledky
print("Korelačný koeficient - Spočítaný        :", koeficient_korelacie)

# Porovnáme so vstavanou funkciou
correlation_coefficient = np.corrcoef(list_u, list_y)[0, 1]
print("Korelačný koeficient - Vstavaná Funkcia :", correlation_coefficient)

autokorelacna_func_u = spocitaj_autokorelacnu_funkciu(list_u)
autokorelacna_func_y = spocitaj_autokorelacnu_funkciu(list_y)

print("Autokorelačná funkcia - u :", autokorelacna_func_u)
print("Autokorelačná funkcia - y :", autokorelacna_func_y)

vzajomne_korelacna_func_u_y = spocitaj_vzajomne_korelacnu_funkciu(list_u, list_y)

print("Vzájomne korelačná funkcia:", vzajomne_korelacna_func_u_y)
