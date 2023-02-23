import tkinter
from tkinter import ttk

root = tkinter.Tk()

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, tkinter.END)
        self.nome_entry.delete(0, tkinter.END)
        self.telefone_entry.delete(0, tkinter.END)
        self.cidade_entry.delete(0, tkinter.END)

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()

    def tela(self):
        self.root.title("Date Calculator")
        self.root.configure(background='#1e3743')
        self.root.geometry('700x500')
    
    def frames_da_tela(self):
        self.frame_1 = tkinter.Frame(self.root, bd = 4, bg = '#dfe3ee',
                                     highlightbackground= '#759fe6', highlightthickness= 3)
        self.frame_1.place(relx = 0.01, rely = 0.03, relwidth= 0.98 , relheight = 0.47)
        self.frame_2 = tkinter.Frame(self.root, bd = 4, bg = '#dfe3ee',
                                     highlightbackground= '#759fe6', highlightthickness= 3)
        self.frame_2.place(relx = 0.01, rely = 0.51, relwidth= 0.98 , relheight = 0.47)

    def widgets_frame1(self):
        # Criação do botão Limpar:
        self.bt_limpar = tkinter.Button(self.frame_1, text = 'Limpar', bd = 2, bg= '#107db2', fg = 'white', 
                                        font = ('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        
        # Criação do botão Buscar:
        self.bt_buscar = tkinter.Button(self.frame_1, text = 'Buscar', bd = 2, bg= '#107db2', fg = 'white', 
                                        font = ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx = 0.3, rely = 0.1, relwidth = 0.1, relheight = 0.15)

        # Criação do botão Novo:
        self.bt_novo = tkinter.Button(self.frame_1, text = 'Novo', bd = 2, bg= '#107db2', fg = 'white', 
                                        font = ('verdana', 8, 'bold'))
        self.bt_novo.place(relx = 0.6, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        
        # Criação do botão Alterar:
        self.bt_alterar = tkinter.Button(self.frame_1, text = 'Alterar', bd = 2, bg= '#107db2', fg = 'white', 
                                        font = ('verdana', 8, 'bold'))
        self.bt_alterar.place(relx = 0.7, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        
        # Criação do botão Apagar:
        self.bt_apagar = tkinter.Button(self.frame_1, text = 'Apagar', bd = 2, bg= '#107db2', fg = 'white', 
                                        font = ('verdana', 8, 'bold'))
        self.bt_apagar.place(relx = 0.8, rely = 0.1, relwidth = 0.1, relheight = 0.15)

        # Criação da label e entrada do código:
        self.lb_codigo = tkinter.Label(self.frame_1, text = "Código", bg = '#dfe3ee', fg = '#107db2')
        self.lb_codigo.place(relx = 0.05, rely = 0.05)

        self.codigo_entry = tkinter.Entry(self.frame_1)
        self.codigo_entry.place(relx = 0.05, rely = 0.15, relwidth = 0.08)

        # Criação da label e entrada do nome:
        self.lb_nome = tkinter.Label(self.frame_1, text = "Nome", bg = '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx = 0.05, rely = 0.35)

        self.nome_entry = tkinter.Entry(self.frame_1)
        self.nome_entry.place(relx = 0.05, rely = 0.45, relwidth = 0.9)

        # Criação da label e entrada do telefone:
        self.lb_telefone = tkinter.Label(self.frame_1, text = "Telefone", bg = '#dfe3ee', fg = '#107db2')
        self.lb_telefone.place(relx = 0.05, rely = 0.6)

        self.telefone_entry = tkinter.Entry(self.frame_1)
        self.telefone_entry.place(relx = 0.05, rely = 0.7, relwidth = 0.4)

        # Criação da label e entrada do Cidade:
        self.lb_cidade = tkinter.Label(self.frame_1, text = "Cidade", bg = '#dfe3ee', fg = '#107db2')
        self.lb_cidade.place(relx = 0.5, rely = 0.6)

        self.cidade_entry = tkinter.Entry(self.frame_1)
        self.cidade_entry.place(relx = 0.5, rely = 0.7, relwidth = 0.45)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height = 3, column = ('col1', 'col2', 'col3', 'col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Código')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')

        self.listaCli.column('#0', width = 1)
        self.listaCli.column('#1', width = 50)
        self.listaCli.column('#2', width = 200)
        self.listaCli.column('#3', width = 125)
        self.listaCli.column('#4', width = 125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollLista = ttk.Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

Application()