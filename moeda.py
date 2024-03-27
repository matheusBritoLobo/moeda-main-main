import customtkinter
from funcao import converter
 
#FUNÇÕES
def geral():
    flag = True
    while(flag):
        tempV = entrada1.get() # Pegar o valor do ENTRY
        tempV = float(tempV) # String to float
        tempM = optionmenu.get() # Pegar valor da Opção de moeda selecionada
        # Comparar a moeda selecionada e atribuir qual o tipo de moeda usado pela API 
        if(tempM == "Dolar"):
            moeda = "USDBRL"
            flag = False
        elif(tempM == "Euro"):
            moeda = "EURBRL"
            flag = False
        elif(tempM == "Bitcoin"):
            moeda = "BTCBRL"
            flag = False
        
        result = converter(tempV,moeda) #chamar a função 
        saida1.configure(text='R$ {:.2f}'.format(result)) # Colocar a informação no Label
    
    
# Tela principal
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
janela = customtkinter.CTk()
janela.geometry("700x200")
janela.title("CONVERSOR DE MOEDAS")

#Label
titulo = customtkinter.CTkLabel(janela,text=("CONVERSOR DE MOEDAS"),font=("Arial",20))
titulo.grid(row=0, column=1,padx=10,pady=10)

texto1 = customtkinter.CTkLabel(janela,text="Digite o valor a ser convertido",font=("Arial",15))
texto1.grid(row=1, column=0,padx=10,pady=10)

texto2 = customtkinter.CTkLabel(janela,text="valor da conversão",font=("Arial",15))
texto2.grid(row=1, column=2,padx=10,pady=10)

saida1 = customtkinter.CTkLabel(janela,text="",fg_color='green',bg_color='green')
saida1.grid(row=2, column=2,padx=10,pady=10)

texto3 = customtkinter.CTkLabel(janela,text="Unidade",font=("Arial",15))
texto3.grid(row=2, column=1,padx=10,pady=10)

#entry
entrada1 = customtkinter.CTkEntry(janela,placeholder_text="Digite o valor")
entrada1.grid(row=2, column=0,padx=10,pady=10)
 
try:# Tratamento e exceção
    entrada1 = customtkinter.CTkEntry(janela,placeholder_text="Digite o valor")
    entrada1.grid(row=2, column=0,padx=10,pady=10)
    
except ValueError as Erro:
    print(Erro)
    print("Digite apenas números")

optionmenu = customtkinter.CTkOptionMenu(janela, values=["Dolar", "Euro","Bitcoin"])
optionmenu.set("Dolar")
optionmenu.grid(row=1,column=1,padx=10,pady=10)

#botão
botao1 = customtkinter.CTkButton(janela, text="CONVERTER", command=geral)
botao1.grid(row=2, column=1,padx=10,pady=10)

janela.mainloop()

print(optionmenu.get())