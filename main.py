from tkinter import *
from tkinter import messagebox  #para importar popup
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():   
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #compreção de lista: [new item for item in list]
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers #junta as 3 listas em uma variavel só
    shuffle(password_list) #embaralha a lista 

    password = "".join(password_list)  #juntar toda a lista e transformar em uma única string
    password_entry.insert(0, password) #para preencher o imput de password com a password gerada com a função.
    pyperclip.copy(password)  #essa biblioteca fará a mesma função de um ctrl+c e então é só colar onde o usuário quiser.
   

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get() #para apanhar a informação digitada pelo usuário utilizamos o .get
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Por favor, certifique-se de que não deixou nenhum campo em branco.") #para apresentar uma menssagem caso tenha campos em branco e não deixe salvar.
    
    else:  #e para não deixar continuar o código caso tenha campos em branco.
        is_ok = messagebox.askokcancel(title= website, message= f"Esses são os dados inseridos: \nWebsite: {website} \nE-mail: {email} \nPassword: {password} \nVocê deseja salvar?") #adionar pup up de cancelamento ou não.
        

        if is_ok:
            with open("data.txt", "a") as data_file: #"a" refere-se a append que é acrescentar 
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END) #apaga oque foi digitado no campo do caracter 0 até o final. Para receber uma nova entrada sem que o usuário precise apagar.
                password_entry.delete(0,END)
                messagebox.showinfo(title="Password Manager", message="Salvo com sucesso.")  #para adionar popup informando o salvamento.


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
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save) #command para adiconar ação do botão
add_button.grid(row=4, column=1, columnspan= 2)



window.mainloop()