import customtkinter;



root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=30, padx=60, fill="both", expand=True)

def Calculate():

    deep=int(Depositentry.get())
    raate=int(Interest_rateentry.get())
    yrrs=int(Yearsentry.get())
    amount=(deep*raate*yrrs)/100

    label = customtkinter.CTkLabel(master=frame, text=f"{amount}").pack(pady=13, padx=50)
    


label=customtkinter.CTkLabel(master=frame,text="Simple Interest").pack(pady=13, padx=50)
Deposit=customtkinter.CTkLabel(master=frame,text="Deposit:").pack(pady=13, padx=50)
Depositentry=customtkinter.CTkEntry(master=frame, placeholder_text="Enter deposit").pack(pady=13, padx=50)
Interest_rate=customtkinter.CTkLabel(master=frame,text="Interest rate:").pack(pady=13, padx=50)
Interest_rateentry=customtkinter.CTkEntry(master=frame, placeholder_text="Enter rate").pack(pady=13, padx=50)
Years=customtkinter.CTkLabel(master=frame,text="Years:").pack(pady=13, padx=50)
Yearsentry=customtkinter.CTkEntry(master=frame, placeholder_text="Enter years").pack(pady=13, padx=50)

btn = customtkinter.CTkButton(master=frame,text="C@lculate",command=Calculate).pack(pady=13, padx=50)

Button = customtkinter.CTkButton(master=frame, text="Calculate", command=Calculate)
Button.pack(pady=13, padx=50)

emptylabel = customtkinter.CTkLabel(master=frame)
emptylabel.pack(pady=13, padx=11)




root.mainloop()