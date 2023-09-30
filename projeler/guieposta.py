from tkinter import *
from tkcalendar import DateEntry

master = Tk()

canvas = Canvas(master, height=450, width=750 )
canvas.pack()

frame_ust = Frame(master,bg ="#add8e6")
frame_ust.place(relx=0.1,rely=0.1,relwidth=0.75,relheight=0.1)

frame_alt_sol = Frame(master,bg="#add8e6")
frame_alt_sol.place(relx=0.1,rely=0.21,relheight=0.5,relwidth=0.23)

frame_alt_sag = Frame(master,bg="#add8e6")
frame_alt_sag.place(relx=0.34,rely=0.21,relwidth=0.51,relheight=0.50)

bulma_tipi_etiket = Label(frame_ust, bg="#add8e6", text="Bulma Tipi:", font="Verdana 12 bold")
bulma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

bulma_tipi_opsiyon = StringVar(frame_ust)
bulma_tipi_opsiyon.set("\t")

bulma_tipi_acilir_menu = OptionMenu(frame_ust,bulma_tipi_opsiyon,"İsim","Kelime")
bulma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)

bulma_tipi_acilir_menu = DateEntry(frame_ust, width=12, background="orange", foreground="black", borderwidth=1, locale="de_DE")
bulma_tipi_acilir_menu._top_cal.overrideredirect(False)
bulma_tipi_acilir_menu.pack(padx=10, pady=10, side=RIGHT)

Label(frame_alt_sag, text="Hatirlatma Yönetmi", bg="#add8e6", font="Verdana 10 bold").pack(padx=10, pady=10, anchor=NW)

Metin_Alani = Text(frame_alt_sag, width=50, height=9)
Metin_Alani.tag_config("style",foreground="#bfbfbf", font=("Verdana", 7, "bold"))
Metin_Alani.pack()

karsilama_metni = "Mesajını buraya gir..."
Metin_Alani.insert(END, karsilama_metni, "style")

gonder_butonu = Button(frame_alt_sag, text="Gonder", command=gonder)
gonder_butonu.pack(anchor=S)

pass



master.mainloop()