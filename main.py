#!/usr/bin/env python3
from tkinter import Tk, Label, Entry, Button, END
from tkinter import messagebox
from scipy.interpolate import interp1d
# import matplotlib.pyplot as plt


def main():
    genislik = Pencere.winfo_screenwidth()
    yukseklik = Pencere.winfo_screenheight()
    px = 610
    py = 200
    w = int((genislik / 2) - (px / 2))
    h = int((yukseklik / 2) - (py / 2))
    ekran = "{}x{}+{}+{}".format(px, py, w, h)
    Pencere.geometry(ekran)
    Pencere.mainloop()


def hesap(arg: str):
    x = xinput1.get().split(",")
    y = xinput2.get().split(",")
    x1 = []
    y1 = []
    for xx in x:
        x1.append(int(xx))
    for yy in y:
        y1.append(int(yy))
    if len(x1) != len(y1):
        messagebox.showinfo(title="uyarı", message="diziler birbirine eşit değil.")
    else:
        z = xinput3.get()
        if arg == "x":
            intp = interp1d(x1, y1, fill_value="extrapolate")
        else:
            intp = interp1d(y1, x1, fill_value="extrapolate")
        sonuc = intp(z)
        print(intp.y, intp.x)
        xinput4.delete(0, END)
        xinput4.insert(0, str(sonuc))


def destroy_me():
    msg = messagebox.askyesno(title="Çıkış", message="Çıkmak İstiyor musunuz?")
    if msg:
        Pencere.destroy()
    else:
        pass


Pencere = Tk()
Pencere.title("İnterpolasyon Hesaplama")
Pencere.resizable(False, False)
Pencere.protocol('WM_DELETE_WINDOW', destroy_me)

Etiket1 = Label(Pencere, text="X :")
Etiket1.place(x=10, y=10)

Etiket2 = Label(Pencere, text="Y :")
Etiket2.place(x=10, y=50)

Etiket3 = Label(Pencere, text="Z :")
Etiket3.place(x=10, y=90)

Etiket4 = Label(Pencere, text="Sonuc: ")
Etiket4.place(x=180, y=92)

xinput1 = Entry(Pencere, width=80)
xinput1.place(x=30, y=9)

xinput2 = Entry(Pencere, width=80)
xinput2.place(x=30, y=49)

xinput3 = Entry(Pencere)
xinput3.place(x=30, y=90)

xinput4 = Entry(Pencere)
xinput4.place(x=230, y=90)

xbuton2 = Button(Pencere, text="X", command=lambda: hesap("x"))
xbuton2.bind_all("x", lambda x: hesap("x"))
xbuton2.place(x=30, y=130)

xbuton3 = Button(Pencere, text="Y", command=lambda: hesap("y"))
xbuton3.bind_all("y", lambda x: hesap("y"))
xbuton3.place(x=70, y=130)

XORY = 0

if __name__ == "__main__":
    main()
