#Primeiro passo foi importar a biblioteca Random
#criar uma classe e atribuir
#referenciar os atributos que usarei nessa função
#primeiro a pergunta que irá iniciar nossa função
#a resposta que será referenciada com a pergunta
#se a pessoa responder sim ou S imprimimos o valor
#se a resposta for não ou n imprimimos agradecemos sua participação
# se for colocado outra informação que nã seja as relacionadas acima responder, favor digitar sim ou não
#se não obedecer a nenhuma dessas questões imprimir, "ocorreu um erro ao receber sua resposta"
#por último a função para gerar o bolão

import random
class SimuladorMegaSena:
    def __init__(self):
        self.mensagem = "Você gostaria de gerar um novo bolão?"

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == "sim" or resposta =="s":
                self.GerarBolaoDaMega()
                print("Boa sorte e seja mais um Milionário!")
            elif resposta == "nao" or resposta == "n":
                 print("agradecemos a sua participação!")
            else:
                 print("favor digitar sim ou nao")
        except:
            print("ocorreu um erro ao receber sua resposta")

    def GerarBolaoDaMega(self):
        print(random.sample(range(1,60),6))
        print(random.sample(range(1,60),6))
        print(random.sample(range(1,60),6))

loteria = SimuladorMegaSena()
loteria.Iniciar()
