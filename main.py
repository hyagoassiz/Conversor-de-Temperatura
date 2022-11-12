import PySimpleGUI as sg
from funcoes import converter_para
from funcoes import conversor

sg.theme('LightBlue') 

layout = [

    [sg.Text('<<Bem Vindo ao Conversor de Escalas de Temperatura>>',
             text_color='Black')],
    [sg.Text('')],
    [sg.Text('Converter', size=(7, 1)), sg.Combo(['Kelvin (K)', 'Celsius (C)', 'Fahrenheit (F)'], size=(13, 1), default_value='Celsius (C)'),
     sg.Text('Para'), sg.Combo(['Kelvin (K)', 'Celsius (C)', 'Fahrenheit (F)'], size=(13, 1), default_value='Fahrenheit (F)')],
    [sg.Text('')],
    [sg.Text('Insira o valor para converter:'),
     sg.InputText(key='graus', size=(10, 5))],
    [sg.Button('Converter'), sg.Button('Cancelar')],
    [sg.Text('', key='resultado', text_color='white')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('Developed by hyagoassiz', text_color='blue')]

]

window = sg.Window('Conversor', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel') or event in 'Cancelar':
        break

    resposta_1 = values[0]
    resposta_2 = values[1]
    graus = values['graus']

    if resposta_1 == '' or resposta_2 == '' or graus == '':
        window['resultado'].update(
            'AVISO: Preencha todos os campos', text_color='red')
    else:
        if resposta_1 == resposta_2:
            window['resultado'].update(
                'AVISO: "Converter" e "Para" precisam ser diferentes', text_color='red')
        else:
            try:
                graus = float(values['graus'])
                resp = converter_para(resposta_1, resposta_2)
                resp_2 = conversor(graus, resp)
                window['resultado'].update('{} {} em {} equivale a: {:.2f} '.format(
                    graus, resposta_1, resposta_2, resp_2), text_color='green')
            except:
                window['resultado'].update(
                    'AVISO: Em "Insira o valor para converter:" digite apenas números', text_color='red')


window.close()
