#!/usr/bin/env python3
from tkinter import Tk, Label, Entry, Button, END, ttk, Menu
from tkinter import messagebox
from scipy.interpolate import interp1d


def main():
    genislik = Pencere.winfo_screenwidth()
    yukseklik = Pencere.winfo_screenheight()
    px = 610
    py = 180
    w = int((genislik / 2) - (px / 2))
    h = int((yukseklik / 2) - (py / 2))
    ekran = "{}x{}+{}+{}".format(px, py, w, h)
    Pencere.geometry(ekran)
    Pencere.mainloop()


def hesap(arg: str):
    x = Xinput1.get().split(",")
    y = Xinput2.get().split(",")
    x1 = []
    y1 = []
    for xx in x:
        x1.append(int(xx))
    for yy in y:
        y1.append(int(yy))
    if len(x1) != len(y1):
        messagebox.showinfo(title="uyarı", message="diziler birbirine eşit değil.")
    else:
        z = Xinput3.get()
        if arg == "x":
            intp = interp1d(x1, y1, fill_value="extrapolate")
        else:
            intp = interp1d(y1, x1, fill_value="extrapolate")
        sonuc = intp(z)
        Xinput4.delete(0, END)
        Xinput4.insert(0, str(sonuc))


def destroy_me():
    msg = messagebox.askyesno(title="Çıkış", message="Çıkmak İstiyor musunuz?")
    if msg:
        Pencere.destroy()
    else:
        pass


def hakkinda():
    messagebox.showinfo(title="Hakkında", message="interpolasyon ile ara değer hesaplama\n0x7000")


Pencere = Tk()
Pencere.title("İnterpolasyon Hesaplama")
Pencere.resizable(False, False)
Pencere.protocol('WM_DELETE_WINDOW', destroy_me)

Menubar = Menu(Pencere)
Pencere.configure(menu=Menubar)
Menubar.add_command(label="Hakkında", command=hakkinda)
Menubar.add_command(label="Çıkış", command=destroy_me)

Etiket1 = Label(Pencere, text="X :")
Etiket1.place(x=10, y=10)

Etiket2 = Label(Pencere, text="Y :")
Etiket2.place(x=10, y=50)

Etiket3 = Label(Pencere, text="Z :")
Etiket3.place(x=10, y=90)

Etiket4 = Label(Pencere, text="Sonuc: ")
Etiket4.place(x=180, y=92)

Xinput1 = Entry(Pencere, width=80)
Xinput1.place(x=30, y=9)

Xinput2 = Entry(Pencere, width=80)
Xinput2.place(x=30, y=49)

Xinput3 = Entry(Pencere)
Xinput3.place(x=30, y=90)

Xinput4 = Entry(Pencere)
Xinput4.place(x=230, y=90)

Xbuton2 = Button(Pencere, text="X", command=lambda: hesap("x"))
Xbuton2.bind_all("x", lambda x: hesap("x"))
Xbuton2.place(x=30, y=130)

Xbuton3 = Button(Pencere, text="Y", command=lambda: hesap("y"))
Xbuton3.bind_all("y", lambda x: hesap("y"))
Xbuton3.place(x=70, y=130)

# ttk içinde "from tkinter import ttk"
TSeparator1 = ttk.Separator(Pencere)
TSeparator1.place(relx=0.010, rely=0.460,  relwidth=0.97)

if __name__ == "__main__":
    main()
