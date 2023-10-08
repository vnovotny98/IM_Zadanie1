# Importujeme potrebné knižnice
import csv
import math
import numpy as np
import matplotlib.pyplot as plt

# Otvoríme CSV súbor - uložený v rovnakom priečinku ako skript
with open('matlabvojta.csv', 'r') as file:
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
def spocitaj_strednu_hodnotu(list_str):
    """
    Vypočíta a vráti strednú hodnotu (priemer) listu čísel.

    Args:
        list_str: List čísel, pre ktorý chceme vypočítať strednú hodnotu.

    Returns:
        float: Stredná hodnota listu.
    """
    stredna_hodnota = 0
    suma = 0
    for i in range(len(list_str)):
        suma += list_str[i]

    stredna_hodnota = (1 / len(list_str)) * suma

    return stredna_hodnota


# Definujeme funkciu na výpočet rozptylu
def spocitaj_rozptyl(list_spr, stredna_hodnota):
    """
    Vypočíta a vráti rozptyl listu čísel.

    Args:
        list_spr: List čísel, pre ktorý chceme vypočítať rozptyl.
        stredna_hodnota: Stredná hodnota listu.

    Returns:
        float: Rozptyl listu.
    """
    rozptyl = 0
    suma = 0
    for i in range(len(list_spr)):
        suma += pow((list_spr[i] - stredna_hodnota), 2)

    rozptyl = (1 / len(list_spr)) * suma

    return rozptyl


# Definujeme funkciu na výpočet kovariáncie
def spocitaj_kovarianciu(list1, list2, stredna_hodnota1, stredna_hodnota2):
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
        suma += (list1[i] - stredna_hodnota1) * (list2[i] - stredna_hodnota2)

    kovariancia = (1 / len(list1)) * suma

    return kovariancia


# Definujeme funkciu na výpočet koeficientu korelácie
def spocitaj_koeficient_korelacie(kovariancia, smer_odchylka1, smer_odchylka2):
    """
    Vypočíta a vráti koeficient korelácie medzi dvoma listmi čísel.

    Args:
        kovariancia: Kovariácia medzi listami.
        smer_odchylka1: Smerodajná odchýlka prvého listu.
        smer_odchylka2: Smerodajná odchýlka druhého listu.

    Returns:
        float: Koeficient korelácie.
    """
    koeficient_korelacie_int = kovariancia / (smer_odchylka1 * smer_odchylka2)

    return koeficient_korelacie_int


# Definujeme funkciu na výpočet autokorelačnej funkcie
def spocitaj_autokorelacnu_funkciu(list_int):
    """
    Vypočíta a vráti autokorelačnú funkciu pre zadaný list hodnôt.

    Args:
        list_int: List hodnôt.

    Returns:
        list: Autokorelačná funkcia.
    """
    vysledok = []
    suma = 0
    maximalny_posun = int(0.1 * len(list_int))
    for i in range(maximalny_posun):
        for k in range(len(list_int) - maximalny_posun):
            suma += list_int[k] * list_int[k + i]

        suma = (1 / (len(list_int) - i)) * suma
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
            suma += list1[k] * list2[k + i]

        suma = (1 / (len(list1) - i)) * suma
        vysledok.append(suma)

    return vysledok


def plot_histogram(data, filename):
    """
    Vytvorí histogram z dát v liste a uloží ho ako obrázok.

    Args:
        data (list): List hodnôt, pre ktorý sa má vytvoriť histogram.
        filename (str): Názov súboru pre uloženie obrázku histogramu.

    Returns:
        None
    """
    # Vytvor histogram
    plt.hist(data, bins=10, edgecolor='black', alpha=0.7)

    # Pridaj popisky
    plt.xlabel('Hodnota')
    plt.ylabel('Frekvencia výskytu')
    plt.title(filename)

    # Ulož graf
    plt.savefig(f"./Plots/{filename}.png")
    plt.clf()


def plot_diskr_dist_func(list_int, filename):
    """
    Vytvorí distribučnú funkciu pre diskrétne dáta a uloží ju ako obrázok.

    Args:
        list_int:
        filename (str): Názov súboru pre uloženie obrázku distribučnej funkcie.

    Returns:
        None
    """
    # Vzorové dáta
    data = list_int

    # Usporiadané dáta
    usporiadane_data = sorted(data)

    # Vytvorenie poľa s kumulatívnymi pravdepodobnosťami
    cdf = np.arange(1, len(usporiadane_data) + 1) / len(usporiadane_data)

    # Počet intervalov
    pocet_intervalov = 10

    # Rozdelenie dát do intervalov
    hist, bin_edges = np.histogram(usporiadane_data, bins=pocet_intervalov)

    # Vytvorenie poľa s kumulatívnymi pravdepodobnosťami z intervalového histogramu
    cdf_intervalov = np.cumsum(hist) / len(usporiadane_data)

    # Vytvorenie CDF grafu
    plt.step(bin_edges[:-1], cdf_intervalov, where='post')

    # Pridaj vertikalnu ciaru v x=0
    plt.axvline(x=0, color='black', linestyle=':', label='Vertical Line at 0')

    # Pridaj horizontalnu ciaru v  y=1
    plt.axhline(y=1, color='black', linestyle=':', label='Horizontal Line at 1')

    # Nastavenie popisov osí
    plt.xlabel('Hodnota')
    plt.ylabel('Kumulatívna pravdepodobnosť')
    plt.title(filename + " 10 intervalov")

    # Uloz graf
    plt.savefig(f"./Plots/{filename}.png")
    plt.clf()


def plot_priebeh_funkcie(list_int, filename, x_axis_label, y_axis_label):
    """
    Vytvorí graf priebehu funkcie z dát a uloží ho ako obrázok.

    Args:
        list_int:
        filename (str): Názov súboru pre uloženie obrázku grafu.
        x_axis_label (str): Popis osi x.
        y_axis_label (str): Popis osi y.

    Returns:
        None
    """
    # Vzorové dáta
    data = list_int

    # Vytvorenie grafu
    plt.plot(data)

    # Nastavenie popisov osí
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.title(filename)

    # Zobrazenie grafu
    plt.savefig(f"./Plots/{filename}.png")
    plt.clf()


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
kovariancia_u_y = spocitaj_kovarianciu(list_u, list_y, stredna_hodnota_u, stredna_hodnota_y)

# Spočítame koeficient korelácie
koeficient_korelacie = spocitaj_koeficient_korelacie(kovariancia_u_y, smer_odchylka_u, smer_odchylka_y)

# Vypíšeme výsledky
print("Střední hodnota - vstup        :", stredna_hodnota_u)
print("Střední hodnota - výstup        :", stredna_hodnota_y)

print("Rozptyl - vstup        :", rozptyl_u)
print("Rozptyl - výstup        :",rozptyl_y)

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

plot_histogram(list_u, "Vojta - Histogram - vstup ")
plot_histogram(list_y, "Vojta - Histogram - výstup ")

plot_diskr_dist_func(list_u, "Vojta - Diskrétní distribuční funkce - vstup")
plot_diskr_dist_func(list_u, "Vojta - Diskrétní distribuční funkce - výstup")

plot_priebeh_funkcie(list_u, "Vojta - Průběh - vstup", "Iterace", "Hodnota")
plot_priebeh_funkcie(list_y, "Vojta - Průběh - výstup", "Iterace", "Hodnota")

plot_priebeh_funkcie(autokorelacna_func_u, "Vojta - Autokorelační funkce - vstup", "Prvek", "Hodnota")
plot_priebeh_funkcie(autokorelacna_func_y, "Vojta - Autokorelační funkce - výstup", "Prvek", "Hodnota")
plot_priebeh_funkcie(vzajomne_korelacna_func_u_y, " Vojta - Vzájemné korelační funkce", "Prvek", "Hodnota")
