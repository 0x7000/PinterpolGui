#!/usr/bin/env python3
from tkinter import Tk, Label, Entry, Button
from tkinter import messagebox
from scipy.interpolate import interp1d


def main():
    genislik = Pencere.winfo_screenwidth()
    yukseklik = Pencere.winfo_screenheight()
    px = 700
    py = 200
    w = int((genislik / 2) - (px / 2))
    h = int((yukseklik / 2) - (py / 2))
    ekran = "{}x{}+{}+{}".format(px, py, w, h)
    Pencere.geometry(ekran)
    Pencere.mainloop()


def hesapx():
    x = xinput1.get().split(",")
    y = xinput2.get().split(",")
    x1 = []
    y1 = []
    for xx in x:
        x1.append(int(xx))
    for yy in y:
        y1.append(int(yy))
    z = xinput3.get()
    intp = interp1d(x1, y1, fill_value="extrapolate")
    sonuc = intp(z)
    print(intp.y, intp.x)
    Etiket4.config(text=sonuc)


def hesapy():
    x = xinput1.get().split(",")
    y = xinput2.get().split(",")
    x1 = []
    y1 = []
    for xx in x:
        x1.append(int(xx))
    for yy in y:
        y1.append(int(yy))
    z = xinput3.get()
    intp = interp1d(y1, x1, fill_value="extrapolate")
    sonuc = intp(z)
    print(intp.y, intp.x)
    Etiket4.config(text=sonuc)


def destroy_me():
    msg = messagebox.askyesno("Çıkış", "Çıkmak İstiyor musunuz?")
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
Etiket4.place(x=200, y=92)

xinput1 = Entry(Pencere, width=80)
xinput1.place(x=30, y=9)

xinput2 = Entry(Pencere, width=80)
xinput2.place(x=30, y=49)

xinput3 = Entry(Pencere)
xinput3.place(x=30, y=90)

xbuton2 = Button(Pencere, text="X", command=hesapx)
xbuton2.place(x=20, y=130)

xbuton2 = Button(Pencere, text="Y", command=hesapy)
xbuton2.place(x=60, y=130)


if __name__ == "__main__":
    main()
