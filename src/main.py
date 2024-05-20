import PySimpleGUI as sg
import numpy as np

sg.theme('Dark')

# Janelas

def Inicial():
    layout = [
        [sg.Text('Ordem da Matriz', size=(15, 0))],
        [sg.Text('Insira apenas números', size=(30, 0))],
        [sg.Input(size=(5, 0), key='ordem')],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Ordem Matriz', layout=layout, margins=(60, 60), finalize=True)


def ordem_1():
    layout = [
        [sg.Text('A ordem precisa ser maior que 1 e menor que 10', size=(40, 0))],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Valor Inválido', layout=layout, margins=(60, 60), finalize=True)

def ordem_matriz():
    layout_linhas = []

    for i in range(int(values['ordem'])):
        linha = [sg.Input(size=(5, 1), key=(i, j)) for j in range(int(values['ordem']))]
        layout_linhas.append(linha)

    layout = [
        [sg.Text(' ~~~ Insira os valores da Matriz ~~~', size=(30, 0))],
        *layout_linhas,
        [sg.Text(' ~~~ Resultado ~~~')],
        [sg.Output(size=(100, 10))],
        [sg.Button('Voltar'), sg.Button('Confirmar')],
        [sg.Text('(Voltar) para inserir novos valores')],
    ] 
    return sg.Window('Diagonalização de Matrizes', layout=layout, margins=(60, 60), finalize=True)


janela1,janela2,janela0 = Inicial(), None, None
    
while True:
    window,event,values = sg.read_all_windows()

    #Encerrar Janelas
    if window == janela0 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela2 and event == sg.WIN_CLOSED:
        break

    # Converte ordem para inteiro    
    try:
        if window == janela1:
            ordem = int(values['ordem'])
            
    except:
        sg.popup("Insira apenas números inteiros")
        if window == janela1:
            janela1.Close()
            janela1 = Inicial()

    # Janela 0
    if window == janela0 and event == 'Voltar':
        janela0.hide()
        janela1.un_hide()

    # Janela 1
    if window == janela1 and event == 'Continuar':
        ordem = int(values['ordem'])
        janela1.hide()

        if ordem <= 1 or ordem > 10:
            janela0 = ordem_1()

        else:
            janela2 = ordem_matriz()

    # Janela 2
    try:
        if window == janela2 and event == 'Confirmar':
            matriz = []

            for i in range(ordem):
                linha = []
                for j in range(ordem):
                    linha.append(int(values[(i, j)]))
                matriz.append(linha)       
   
            matriz_array = np.array(np.round(matriz))
            determinante = np.round(np.linalg.det(matriz_array), decimals=2)
            
            print(f"Matriz Inserida: \n\n{matriz_array}") 
            print(f"\nDeterminante: {determinante}")

            if (determinante != 0):
                matriz_inversa = np.round(np.linalg.inv(matriz_array), decimals=2)
                print(f"\nMatriz Inversa: \n\n{matriz_inversa}")

                matriz_identidade_aprox = np.round(np.matmul(matriz_array, matriz_inversa), decimals=2)
                print(f"\nMatriz Identidade Aproximada: \n\n{matriz_identidade_aprox}")

                matriz_identidade_exat = np.eye(ordem, ordem)
                print(f"\nMatriz Identidade Exata: \n\n{matriz_identidade_exat}")

                print("\nÉ uma matriz Linearmente Independente")
    
            elif (determinante == 0):
                print("\nA matriz não tem como diagonalizar, o determinante é igual a 0\nPortanto é uma matriz Linearmente Dependente")
    except:
        sg.popup("Preencha todos os espaços corretamente\n\nClique em (Voltar) para inserir novos valores")

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
        values['ordem'] = []
        matriz = []   

#Nicolas Eidi Nunes Macedo