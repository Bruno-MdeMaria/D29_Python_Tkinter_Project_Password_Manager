from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20) #acochoamento de 20px

canvas = Canvas(height=200, width=200)  #criar tela
logo_image = PhotoImage(file="logo.png") #importa imagem para dentro da variavel
canvas.create_image(100,100 ,image=logo_image) #cria dentro do canvas uma imagem agora chamando a variavel com a imagem dentro. IMPORTANTE = sempre colocar a posição x e y no tuple.
canvas.grid(row=0, column=1)

#Etiquetas/Labels:
website_label = Label(text="Website") #é necessário colocar de mod "text=" para poder colocar a str.
website_label.grid(row=1 , column=0)
email_label = Label(text="E-mail/Username")
email_label.grid(row=2 , column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)


window.mainloop()