from tkinter import *

def zapisz_dane():
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    wiek = entry_wiek.get()
    pesel = entry_pesel.get()
    plec = var_plec.get()
    wojewodztwo = listbox_wojewodztwo.get(ACTIVE)
    miasto = entry_miasto.get()
    ulica = entry_ulica.get()

    with open('dane.txt', 'a') as plik:
        plik.write(f"Imię: {imie}\n")
        plik.write(f"Nazwisko: {nazwisko}\n")
        plik.write(f"Wiek: {wiek}\n")
        plik.write(f"PESEL: {pesel}\n")
        plik.write(f"Płeć: {plec}\n")
        plik.write(f"Województwo: {wojewodztwo}\n")
        plik.write(f"Miasto: {miasto}\n")
        plik.write(f"Ulica: {ulica}\n")
        plik.write("\n")
    
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_wiek.delete(0, END)
    entry_pesel.delete(0, END)
    var_plec.set(0)
    listbox_wojewodztwo.selection_clear(0, END)
    entry_miasto.delete(0, END)
    entry_ulica.delete(0, END)

root = Tk()
root.title("Formularz nieresponsywny")

Label(root, text="Imię:").grid(row=0, sticky=W)
Label(root, text="Nazwisko:").grid(row=1, sticky=W)
Label(root, text="Wiek:").grid(row=2, sticky=W)
Label(root, text="PESEL:").grid(row=3, sticky=W)
Label(root, text="Płeć:").grid(row=4, sticky=W)
Label(root, text="Województwo:").grid(row=5, sticky=W)
Label(root, text="Miasto:").grid(row=6, sticky=W)
Label(root, text="Ulica:").grid(row=7, sticky=W)

entry_imie = Entry(root)
entry_imie.grid(row=0, column=1)
entry_nazwisko = Entry(root)
entry_nazwisko.grid(row=1, column=1)
entry_wiek = Entry(root)
entry_wiek.grid(row=2, column=1)
entry_pesel = Entry(root)
entry_pesel.grid(row=3, column=1)
var_plec = StringVar()
Radiobutton(root, text="Mężczyzna", variable=var_plec, value="Mężczyzna").grid(row=4, column=1, sticky=W)
Radiobutton(root, text="Kobieta", variable=var_plec, value="Kobieta").grid(row=4, column=1, sticky=E)
listbox_wojewodztwo = Listbox(root)
listbox_wojewodztwo.grid(row=5, column=1)
wojewodztwa = ["Dolnośląskie", "Kujawsko-pomorskie", "Lubelskie", "Lubuskie", "Łódzkie", "Małopolskie", "Mazowieckie",
               "Opolskie", "Podkarpackie", "Podlaskie", "Pomorskie", "Śląskie", "Świętokrzyskie", "Warmińsko-mazurskie",
               "Wielkopolskie", "Zachodniopomorskie"]

for wojewodztwo in wojewodztwa:
    listbox_wojewodztwo.insert(END, wojewodztwo)

entry_miasto = Entry(root)
entry_miasto.grid(row=6, column=1)
entry_ulica = Entry(root)
entry_ulica.grid(row=7, column=1)

Button(root, text="Zapisz", command=zapisz_dane).grid(row=8, column=0, columnspan=2)

root.mainloop()
