import tkinter as tk
import consultando
import calculo_frete


def resposta_cliente():
        cep = caixa_entrada_cep.get()
        sinal, dados = consultando.consulta(cep)    
        if sinal == 1:
            resposta_ao_cliente = f"CEP: {dados['cep']}\nRUA: {dados['logradouro']}\nBAIRRO: {dados['bairro']}\nCIDADE/UF: {dados['localidade']}/{dados['uf']}"
            texto_resposta.config(text= resposta_ao_cliente, bg="white")
            if cep[0] == "6":
                preco = calculo_frete.frete(dados['bairro'])
                texto_preco_frete.config(text= f"FRETE: R${preco}.00", bg="white")
            else:
                texto_preco_frete.config(text= f"Endereço fora da aréa de entrega!",)
                
        elif sinal == 2:
            resposta_ao_cliente = dados
            texto_resposta.config(text= resposta_ao_cliente)
            
        else:
            resposta_ao_cliente = dados
            texto_resposta.config(text= resposta_ao_cliente)
            

    
janela = tk.Tk()
janela.title("calcular frete")
janela.iconbitmap("icone.ico")
janela.geometry("500x400")
janela.configure(bg="#155493")


texto_1 = tk.Label(janela, text="Bem-vindo, Digite seu CEP!")
texto_1.place(x=180, y=70)

caixa_entrada_cep = tk.Entry(janela, width=28)
caixa_entrada_cep.place(x=170, y=100)


botao = tk.Button(janela, text="calcular", command=resposta_cliente)
botao.place(x=225, y=130)

texto_resposta = tk.Label(janela, text="", justify="left", font=("Arial", 10),bg="#155493")
texto_resposta.place(x=180, y=200)

texto_preco_frete = tk.Label(janela, text="", justify="left", font=("Arial", 10),bg="#155493" )
texto_preco_frete.place(x=180, y=265)



janela.mainloop()



