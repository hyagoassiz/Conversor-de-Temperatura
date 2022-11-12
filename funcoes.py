def conversor(graus, converter):
    if converter == '1':
        resultado = graus - 273.15
        return resultado
    if converter == '2':
        resultado = (graus - 273.15) * 9/5 + 32
        return resultado

    if converter == '3':
        resultado = graus + 273.15
        return resultado

    if converter == '4':
        resultado = (graus * 9/5) + 32
        return resultado

    if converter == '5':
        resultado = (graus - 32) * 5/9 + 273.15
        return resultado

    if converter == '6':
        resultado = (graus - 32) * 5/9
        return resultado


def converter_para(resposta_1, resposta_2):
    if resposta_1 == 'Kelvin (K)' and resposta_2 == 'Celsius (C)':
        return '1'

    if resposta_1 == 'Kelvin (K)' and resposta_2 == 'Fahrenheit (F)':
        return '2'

    if resposta_1 == 'Celsius (C)' and resposta_2 == 'Kelvin (K)':
        return '3'

    if resposta_1 == 'Celsius (C)' and resposta_2 == 'Fahrenheit (F)':
        return '4'

    if resposta_1 == 'Fahrenheit (F)' and resposta_2 == 'Kelvin (K)':
        return '5'

    if resposta_1 == 'Fahrenheit (F)' and resposta_2 == 'Celsius (C)':
        return '6'


