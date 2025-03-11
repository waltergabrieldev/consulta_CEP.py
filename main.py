import tkinter as tk
import consultando


def entrada_cep():
        cep = caixa_entrada_cep.get()
        sinal, dados = consultando.consulta(cep)
        if sinal == 1:
            resposta_ao_cliente = f"CEP: {dados['cep']}\nRUA: {dados['logradouro']}\nBAIRRO: {dados['bairro']}\nCIDADE/UF: {dados['localidade']}/{dados['uf']}"
        elif sinal == 2:
            resposta_ao_cliente = dados
        else:
            resposta_ao_cliente = dados 
        texto_resposta.config(text=resposta_ao_cliente)
   
janela = tk.Tk()

janela.title("CONSULTAR CEP")

janela.geometry("500x400")

texto_1 = tk.Label(janela, text="Bem-vindo, consulte seu CEP!")
texto_1.place(x=173, y=35)

caixa_entrada_cep = tk.Entry(janela, width=28)
caixa_entrada_cep.place(x=170, y=100)


botao = tk.Button(janela, text="consultar", command=entrada_cep)
botao.place(x=225, y=130)

texto_resposta = tk.Label(janela, text="", justify="left", font=("Arial", 10))
texto_resposta.place(x=150, y=200)



janela.mainloop()



