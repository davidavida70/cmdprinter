import pygetwindow as util
import time
from PIL import ImageGrab
from guizero import App, Text, PushButton, Window
import pyautogui

pyautogui.FAILSAFE = False
d = App(title='Dedetizador de cmd', height=200, width=500)
esc = Window(d, title='Seleção de método', height=100, width=300)
esc.hide()
status = Text(d, text='─ O nome da janela ser cmd.exe ou prompt de comando;\n'
                      '─ No modo printar & pausar o cmd precisa estar em\n foco para o programa conseguir pausar.')
status2 = Text(d)
status2.hide()
num = 0


def contador():
    global num
    num += 1
    return num

def escolher():
    esc.show(wait=True)

def corekill():
    status.value = 'Rodando...'
    status2.show()
    status2.value = 'Modo: Printar & exterminar'
    janela = util.getWindowsWithTitle('cmd.exe')
    janela2 = util.getWindowsWithTitle('prompt')
    if len(janela):
        try:
            janela = util.getWindowsWithTitle('cmd.exe')[0]
            lugar = f'foto{num}.png'
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            contador()
            janela.close()
        except OSError as tip:
            print(f'Erro: {tip}')

    if len(janela2):
        try:
            janela = util.getWindowsWithTitle('prompt')[0]
            lugar = f'foto{num}.png'
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            contador()
            janela.close()
        except OSError as tip:
            print(f'Erro: {tip}')


def corepause():
    status.value = 'Rodando...'
    status2.show()
    status2.value = 'Modo: Printar & pausar'
    janelacheck = util.getWindowsWithTitle('cmd.exe')
    janelacheck2 = util.getWindowsWithTitle('prompt')
    if len(janelacheck):
        try:
            n = 0
            lugar = f'fotop{num}.png'
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)

            pyautogui.press('pause')
            if len(janelacheck) > 1:
                n += 1
            if len(janelacheck) == 1:
                time.sleep(0.1)
        except OSError as tip:
            print(f'Erro: {tip}')

    if len(janelacheck2):
        try:
            n = 0
            lugar = f'fotop{num}.png'
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            contador()

            pyautogui.press('pause')
            if len(janelacheck2) > 1:
                n += 1
            if len(janelacheck2) == 1:
                time.sleep(0.1)
        except OSError as tip:
            print(f'Erro: {tip}')


def vaicorekill():
    d.repeat(100, corekill)
    esc.hide()

def vaicorepause():
    d.repeat(100, corepause)
    esc.hide()

def stopcore():
    status.value = 'Pausado...'
    d.cancel(corekill)
    d.cancel(corepause)


butao = PushButton(d, text='Começar', command=escolher)
butao2 = PushButton(d, text='Parar', command=stopcore)
kill = PushButton(esc, text='Printar & exterminar', command=vaicorekill)
pause = PushButton(esc, text='Printar & pausar', command=vaicorepause)

d.display()
