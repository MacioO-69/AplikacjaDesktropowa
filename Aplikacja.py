import tkinter as tk

class Aplikacja:
    def __init__(self,okno):
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()
        self.text3 = tk.StringVar()
        self.text4 = tk.StringVar()
        self.text5 = tk.StringVar()
        self.text6 = tk.StringVar()
        self.text7 = tk.StringVar()
        self.text8 = tk.StringVar()

        self.tekst1 = tk.Label(okno, bg="white" ,fg="green")
        self.tekst1 = tk.Label(okno, bg="white" ,fg="green")
        self.tekst1 = tk.Label(okno, bg="white" ,fg="green")
        self.tekst1 = tk.Label(okno, bg="white" ,fg="green")
        self.tekst1 = tk.Label(okno, bg="white" ,fg="green")
        self.tekst1 = tk.Label(okno, bg="white" ,fg="green")
        self.tekst1 = tk.Label(okno, bg="white" ,fg="green")
        self.tekst1 = tk.Label(okno, bg="white" ,fg="green")




okno = tk.Tk()
okno.title("NIE UKRADNIEMY TWOICH DANYCH ;)")
okno.geometry("450x600")
okno.resizable(False, False)
okno.configure(background='black')
okno.mainloop()
