from tkinter import *
from tkinter import messagebox
import os

def obter_informacoes():
    def obter_dados():
        global produto, valor_min, valor_max, email
        produto = campo_nome_produto.get()
        if produto:
            try:
                valor_min = int(campo_valor_min.get())
                valor_max = int(campo_valor_max.get())
            except ValueError:
                messagebox.showwarning(title="Erro", message="Por favor, insira números inteiros para os preços.")
                return
            if "@" not in campo_email.get() or ".com" not in campo_email.get():
                messagebox.showwarning(title="Erro", message="Por favor, insira um e-mail válido.")
                return
            email = campo_email.get()
            window.destroy()
        else:
            messagebox.showwarning(title="Erro", message="Preencha os campos que estão faltando.")

    window = Tk()
    window.geometry("481x384")
    window.configure(bg = "#ffffff")
    window.title("Pesquisa de preços")

    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Caminhos das imagens
    background_path = os.path.join(dir_path, 'background.png')
    entry0_path = os.path.join(dir_path, 'img_textBox0.png')
    entry1_path = os.path.join(dir_path, 'img_textBox1.png')
    entry2_path = os.path.join(dir_path, 'img_textBox2.png')
    entry3_path = os.path.join(dir_path, 'img_textBox3.png')
    img0_path = os.path.join(dir_path, 'img0.png')

    # Carregando as imagens
    background_img = PhotoImage(file=background_path)
    entry0_img = PhotoImage(file=entry0_path)
    entry1_img = PhotoImage(file=entry1_path)
    entry2_img = PhotoImage(file=entry2_path)
    entry3_img = PhotoImage(file=entry3_path)
    img0 = PhotoImage(file=img0_path)

    canvas = Canvas(window, bg = "#ffffff", height = 384, width = 481, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)

    # Adicionando as imagens ao Canvas
    background = canvas.create_image(240.5, 192.0, image=background_img)
    entry0_bg = canvas.create_image(241.0, 109.5, image=entry0_img)
    entry1_bg = canvas.create_image(117.0, 197.5, image=entry1_img)
    entry2_bg = canvas.create_image(365.0, 197.5, image=entry2_img)
    entry3_bg = canvas.create_image(241.0, 288.5, image=entry3_img)

    # Criando os campos de entrada
    campo_nome_produto = Entry(bd = 0, bg = "#ffffff", highlightthickness = 0)
    campo_nome_produto.place(x = 67.0, y = 90, width = 348.0, height = 43)

    campo_valor_min = Entry(bd = 0, bg = "#ffffff", highlightthickness = 0)
    campo_valor_min.place(x = 67.0, y = 178, width = 100.0, height = 43)

    campo_valor_max = Entry(bd = 0, bg = "#ffffff", highlightthickness = 0)
    campo_valor_max.place(x = 315.0, y = 178, width = 100.0, height = 43)

    campo_email = Entry(bd = 0, bg = "#ffffff", highlightthickness = 0)
    campo_email.place(x = 67.0, y = 269, width = 348.0, height = 43)

    # Criando o botão
    b0 = Button(window, image=img0, borderwidth=0, highlightthickness=0, command=obter_dados, relief="flat", bg="#252525", activebackground="#252525")
    b0.place(x = 172, y = 326, width = 141, height = 51)

    window.resizable(False, False)
    window.mainloop()

    try:
        return produto, valor_min, valor_max, email
    except NameError:
        pass    

def criar_janela():
    return obter_informacoes()