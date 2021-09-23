from typing import KeysView, Sized
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Radio
import os
import pandas as pd

sg.change_look_and_feel('DarkGreen5')

class Tela():
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Número:'),sg.Input(size=(3,0), key='numero')],
            [sg.Radio('Macho', 'cartoes', key='ehMacho'),sg.Radio('Femea', 'cartoes',key='ehFemea')],
            [sg.Text('Pai'),sg.Input(size=(10,0), key='pai')],
            [sg.Text('Mae'),sg.Input(size=(3,0), key='mae')],
            [sg.Button('Cadastrar')]
        ]

        #janela
        janela = sg.Window('Cadastro de Ovinos').layout(layout)
        #extrair dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        sg.popup('Cadastro feito com sucesso!')
        numero = self.values['numero']
        pai = self.values['pai']
        mae = self.values['mae']
        ehMacho = self.values['ehMacho']
        ehFemea = self.values['ehFemea']
        print(f'Número: {numero}')

        if ehMacho == True:
            print(f'Sexo: Macho')
        else:
            print(f'Sexo: Femea')

        print(f'Pai: {pai}')
        print(f'Mae: {mae}')

        #arquivo = open('cadastro.txt')
        #arquivo.write('')

tela = Tela()
tela.Iniciar()
