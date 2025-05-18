import pygetwindow as util
import time
from PIL import ImageGrab
from guizero import App, Text, PushButton

d = App(title='Dedetizador de cmd')
status = Text(d, text='Requisitos: o nome da janela ser cmd.exe ou prompt de comando\n')
num = 0
def contador():
    global num
    num += 1
    return num


def core():

    status.value = 'Rodando...'
    ##while True:
    janela = util.getWindowsWithTitle('cmd.exe')
    janela2 = util.getWindowsWithTitle('prompt de comando')
    if len(janela):
        try:
            print(janela)
            print(janela2)
            janela = util.getWindowsWithTitle('cmd.exe')[0]
            print(janela, '1')
            lugar = f'foto{num}.png'
            ##time.sleep(0.5)
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            print(f'contador: {num}')
            contador()
            janela.close()
        except:
            print('nada')

    if len(janela2):
        try:
            print(janela2)
            janela = util.getWindowsWithTitle('prompt de comando')[0]
            print(janela, '2')
            lugar = f'foto{num}.png'
            ##time.sleep(0.5)
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            print(f'contador: {num}')
            contador()
            janela.close()
        except:
            print('nada')


def vaicore():
    d.repeat(100, core)
def stopcore():
    status.value = 'Pausado...'
    d.cancel(core)


butao = PushButton(d, text='Começar', command=vaicore)
butao2 = PushButton(d, text='Pausar', command=stopcore)

d.display()
