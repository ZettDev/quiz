import customtkinter as ctk

janela = ctk.CTk()
janela.title("tela Quiz")
janela.geometry("700x400")

score = 0

def clicabotao(n,r):
    global score
    if n == int(r):
        score += 1
        print(score)
    else:
        pass

var = ctk.BooleanVar()

perguntas = [
    ["Qual é a capital do Brasil?", "a) São Paulo", "b) Rio de Janeiro", "c) Brasília", "d) Salvador", "3"],
    ["Qual é o maior planeta do sistema solar?", "a) Júpiter", "b) Marte", "c) Terra", "d) Saturno", "1"],
    ["Qual é o país com a maior população do mundo?", "a) Estados Unidos", "b) Rússia", "c) China", "d) Índia", "3"],
    ["Quem pintou a Mona Lisa?", "a) Leonardo da Vinci", "b) Pablo Picasso", "c) Vincent van Gogh", "d) Salvador Dalí", "1"]
    #...
    # Puxar essas perguntas do bd
]

for x in perguntas:
    pergunta= ctk.CTkLabel(janela, text=x[0],font=("arial bold", 20))
    pergunta.place(x=250, y=200)
    for i in range(1,5):
        match i:
            case 1:
                botao = ctk.CTkButton(janela, text=x[i],command=lambda : [var.set(1), clicabotao(1,x[-1])])
                botao.place(x=160, y=250)
            case 2:
                botao = ctk.CTkButton(janela, text=x[i],command=lambda : [var.set(1), clicabotao(2,x[-1])])
                botao.place(x=160, y=300)
            case 3:
                botao = ctk.CTkButton(janela, text=x[i],command=lambda : [var.set(1), clicabotao(3,x[-1])])
                botao.place(x=330, y=250)
            case 4:
                botao = ctk.CTkButton(janela, text=x[i],command=lambda : [var.set(1), clicabotao(4,x[-1])])
                botao.place(x=330, y=300)
    janela.update()
    botao.wait_variable(var)
    pergunta.destroy()

# quantidade e existencia dos botões pode mudar dependendo das perguntas (alternativas, multiplas alternativas, verdadeiro ou falso, texto)

janela.mainloop()