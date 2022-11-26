from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get() #para apanhar a informação digitada pelo musuário utilizamos o .get
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file: #"a" refere-se a append que é acrescentar 
        data_file.write(f"{website} | {email} | {password}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40) #acochoamento de 20px

canvas = Canvas(height=200, width=200)  #criar tela
logo_image = PhotoImage(file="logo.png") #importa imagem para dentro da variavel
canvas.create_image(100,100 ,image=logo_image) #cria dentro do canvas uma imagem agora chamando a variavel com a imagem dentro. IMPORTANTE = sempre colocar a posição x e y no tuple.
canvas.grid(row=0, column=1)

#Etiquetas/Labels:
website_label = Label(text="Website:") #é necessário colocar de mod "text=" para poder colocar a str.
website_label.grid(row=1 , column=0)
email_label = Label(text="E-mail/Username:")
email_label.grid(row=2 , column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#ENTRADAS/Entrys:
website_entry = Entry(width=52) #tamanho da janela do imput/entrada
website_entry.grid(row=1, column=1, columnspan= 2)  #COLUMNSPAN= define até qual coluna vai a a linha
website_entry.focus()  #para cursor aparecer piscando dentro do campo de entrada de website
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan= 2)
email_entry.insert(0, "brunomart@gmail.com") #quando inicia o programa oq está inserido nesse campo já aparece previamente(talvez a última informação atualizada)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

#Botoões/Buttons:
generate_password = Button(text="Generate Password")
generate_password.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save) #command para adiconar ação do botão
add_button.grid(row=4, column=1, columnspan= 2)






window.mainloop()