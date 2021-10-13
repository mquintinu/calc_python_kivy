from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Define o layout (arquivo kv)
Builder.load_file("calculadora.kv")

# Define tamanho do app
Window.size = (500, 700)


class MinhaCalculadora(App):
    def build(self):
        return MeuLayout()
        
class MeuLayout(Widget):
        
    # LIMPAR
    def limpar(self):
        self.ids.calc_tela.text = "0"

    # Apaga o último caracter
    def Apaga(self):
        prior = self.ids.calc_tela.text
        prior = prior[:-1]
        self.ids.calc_tela.text = prior

    # Deixa o número Negativo ou Positivo
    def Negativo(self):
        prior = self.ids.calc_tela.text
        if "-" in prior:
            self.ids.calc_tela.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_tela.text = f'-{prior}'


    # EVENTO DE CLICAR NOS BOTÕES
    def btnPress(self, button):
        # var
        prior = self.ids.calc_tela.text

        # Se tiver dado erro, limpa a tela
        if prior == "Número inválido":
            prior = ''

        # 
        if prior == "0":
            self.ids.calc_tela.text = ''
            self.ids.calc_tela.text = f'{button}'
        else: 
            self.ids.calc_tela.text = f'{prior}{button}'

    # SINAL MATEMÁTICO
    def Sinal_matematico(self, sinal):
        # var
        prior = self.ids.calc_tela.text
        self.ids.calc_tela.text = f'{prior}{sinal}'

    # NÚMEROS DECIMAIS
    def num_decimal(self):
        prior = self.ids.calc_tela.text
        num_list = prior.split("+")   
    
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_tela.text = prior
        elif "." in prior:
            pass
        else: 
            prior = f'{prior}.'
            self.ids.calc_tela.text = prior

    # REALIZAR O CÁLCULO 
    def Igual(self):
        # var
        prior = self.ids.calc_tela.text   
        try:
            resposta = eval(prior)
            self.ids.calc_tela.text = str(resposta)
        except:
            self.ids.calc_tela.text = "Número inválido"

        '''# Soma               
        if "+" in prior:
            resposta = 0.0
            num_list = prior.split("+")            
            for numero in num_list:
                resposta = resposta + float(numero)

        # Subtrai
        if "-" in prior:
            num_list = prior.split("-")     
            resposta = float(num_list[0])
            for n in num_list:                
                resposta = resposta - float(n)                              
            resposta = resposta + float(num_list[0])
        self.ids.calc_tela.text = str(resposta)
        '''




if __name__ == '__main__':
    MinhaCalculadora().run()