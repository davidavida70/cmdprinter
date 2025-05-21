import pygetwindow as util
import time
from PIL import ImageGrab
from guizero import App, Text, PushButton, Window, Slider
import pyautogui

pyautogui.FAILSAFE = False
d = App(title='Dedetizador de cmd', height=275, width=500)
esc = Window(d, title='Seleção de método', height=100, width=300)
esc.hide()
status = Text(d, text='─ O nome da janela ser cmd.exe ou prompt de comando;\n'
                      '─ No modo printar & pausar o cmd precisa estar em\n foco para o programa conseguir pausar.\n')
status2 = Text(d)
hint = Text(d, size=8, text='|Quantidade de fotos do modo Printar & pausar|')
status2.hide()
limit = Slider(d, start=5, end=50)
nump = 0
numkill = 0


def contadork():
    global numkill
    numkill += 1
    return numkill

def contadorp():
    global nump
    nump += 1
    return nump

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
            lugar = f'fotocmd{numkill}.png'
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            contadork()
            janela.close()
        except OSError as tip:
            print(f'Erro: {tip}')

    if len(janela2):
        try:
            janela = util.getWindowsWithTitle('prompt')[0]
            lugar = f'fotoprompt{numkill}.png'
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            contadork()
            janela.close()
        except OSError as tip:
            print(f'Erro: {tip}')


def corepause():
    global limit, nump
    status.value = 'Rodando...'
    status2.show()
    status2.value = 'Modo: Printar & pausar'
    if nump >= int(limit.value)-1:
        stopcore()
    janelacheck = util.getWindowsWithTitle('cmd.exe')
    janelacheck2 = util.getWindowsWithTitle('prompt')
    if len(janelacheck):
        try:
            lugar = f'fotopcmd{nump}.png'
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            contadorp()
            pyautogui.press('pause')
            if len(janelacheck) == 1:
                time.sleep(0.1)
        except OSError as tip:
            print(f'Erro: {tip}')

    if len(janelacheck2):
        try:
            lugar = f'fotopprompt{nump}.png'
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            contadorp()
            pyautogui.press('pause')
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


fill = Text(d, align='bottom')
butao2 = PushButton(d, text='Parar', command=stopcore, align='bottom')
butao = PushButton(d, text='Começar', command=escolher, align='bottom')
fill2 = Text(d)
kill = PushButton(esc, text='Printar & exterminar', command=vaicorekill)
pause = PushButton(esc, text='Printar & pausar', command=vaicorepause)

d.display()
