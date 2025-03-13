import tkinter as tk
import consultando_cep
import calculo_frete


def resposta_cliente():
    
        cep = entrada_cep.get()
        sinal, resposta = consultando_cep.consulta(cep)    
        
        if sinal == 1:
            info_endereço = f"CEP: {resposta['cep']}\nRUA: {resposta['logradouro']}\nBAIRRO: {resposta['bairro']}\nCIDADE/UF: {resposta['localidade']}/{resposta['uf']}"
            texto_info_endereço.config(text= info_endereço, bg="white")
            preço_frete = calculo_frete.frete(resposta['bairro'])
            if preço_frete == None:
                texto_info_frete.config(text= f"Endereço fora da aréa de entrega!", bg="white")
            else:
                texto_info_frete.config(text= f"FRETE: R${preço_frete}.00", bg="white")
                
        elif sinal == 2:
            info_endereço = resposta
            texto_info_endereço.config(text= info_endereço,bg="white" )
            texto_info_frete.config(text= "",bg="#155493" )
            
        else:
            info_endereço = resposta
            texto_info_endereço.config(text= info_endereço, bg="white")
            texto_info_frete.config(text= "", bg="#155493")
            
 
janela = tk.Tk()
janela.title("calcular frete")
janela.iconbitmap("icone.ico") 
janela.geometry("500x400")
janela.configure(bg="#155493")


texto_1 = tk.Label(janela, text="Bem-vindo, Digite seu CEP!")
texto_1.place(x=180, y=70)

entrada_cep = tk.Entry(janela, width=28)
entrada_cep.place(x=170, y=100)


botao = tk.Button(janela, text="calcular", command=resposta_cliente)
botao.place(x=225, y=130)

texto_info_endereço = tk.Label(janela, text="", justify="left", font=("Arial", 10),bg="#155493")
texto_info_endereço.place(x=180, y=200)

texto_info_frete = tk.Label(janela, text="", justify="left", font=("Arial", 10),bg="#155493" )
texto_info_frete.place(x=180, y=265)



janela.mainloop()



