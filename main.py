import pygetwindow as util
import time
from PIL import ImageGrab
from guizero import App, Text, PushButton, Window, Slider, MenuBar, TextBox
import pyautogui

pyautogui.FAILSAFE = False
d = App(title='Dedetizador de cmd', height=275, width=500)
esc = Window(d, title='Seleção de método', height=100, width=300)
esc.hide()
escms = Window(d, title='Escolha de delay', height=150, width=300)
escms.hide()
msbox = TextBox(escms, text='0.0')
msboxp = TextBox(escms, text='0.1')
status = Text(d, text='─ O nome da janela precisa ser cmd.exe ou prompt de comando;\n'
                      '─ No modo printar & pausar o cmd precisa estar em foco para o \n'
                      'programa conseguir pausar.                                                         \n')
status2 = Text(d)
hint = Text(d, size=8, text='|Quantidade de fotos do modo Printar & pausar|')
status2.hide()
hint2 = Text(escms, size=10, text='Padrões:', align='top', height=1)
deschint2 = Text(escms, size=10, text='Printar & exterminar: 0s                              \n'
                                      'Printar & pausar: 0.1s (após a primeira print)', height=2)
limit = Slider(d, start=5, end=50)
nump = numkill = nump2 = idcore = jascolhi = 0
lugar = path = ''


def contadork():
    global numkill
    numkill += 1
    return numkill


def contadorp():
    global nump, nump2
    nump += 1
    nump2 += 1


def pasta():
    global path, jascolhi
    path = d.select_folder()
    jascolhi = 1


def escolher():
    if jascolhi == 0:
        pasta()
    if path:
        esc.show(wait=True)


def corekill():
    global lugar, idcore
    idcore = 1
    status.value = 'Rodando...'
    status2.show()
    status2.value = 'Modo: Printar & exterminar'
    janela = util.getWindowsWithTitle('cmd.exe')
    janela2 = util.getWindowsWithTitle('prompt')
    if len(janela):
        try:
            janela = util.getWindowsWithTitle('cmd.exe')[0]
            lugar = f'{path}/fotocmd{numkill}.png'
            time.sleep(int(msbox.value))
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            print(lugar)
            contadork()
            janela.close()
        except OSError as tip:
            print(f'Erro: {tip}')
            exit(0)
        except ValueError as tip:
            print(f'Erro: {tip}')
            stopcore()
            d.error('Erro', 'Escolha um delay válido! (exemplo: 0.7)')

    if len(janela2):
        try:
            janela = util.getWindowsWithTitle('prompt')[0]
            lugar = f'{path}/fotoprompt{numkill}.png'
            time.sleep(int(msbox.value))
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            print(lugar)
            contadork()
            janela.close()
        except OSError as tip:
            print(f'Erro: {tip}')
            exit(0)
        except ValueError as tip:
            print(f'Erro: {tip}')
            stopcore()
            d.error('Erro', 'Escolha um delay válido! (exemplo: 0.7)')

def corepause():
    global limit, nump, nump2, lugar, idcore
    idcore = 2
    status.value = 'Rodando...'
    status2.show()
    status2.value = 'Modo: Printar & pausar'
    if nump2 >= int(limit.value) - 1:
        nump2 = -1
        stopcore()
    janelacheck = util.getWindowsWithTitle('cmd.exe')
    janelacheck2 = util.getWindowsWithTitle('prompt')
    if len(janelacheck):
        try:
            lugar = f'{path}/fotopcmd{nump}.png'
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            print(lugar)
            contadorp()
            pyautogui.press('pause')
            if len(janelacheck) == 1:
                time.sleep(int(msboxp.value))
        except OSError as tip:
            print(f'Erro: {tip}')
            exit(0)
        except ValueError as tip:
            print(f'Erro: {tip}')
            stopcore()
            d.error('Erro', 'Escolha um delay válido! (exemplo: 0.7)')

    if len(janelacheck2):
        try:
            lugar = f'{path}/fotopprompt{nump}.png'
            screenshot = ImageGrab.grab()
            screenshot.save(lugar)
            contadorp()
            pyautogui.press('pause')
            if len(janelacheck2) == 1:
                time.sleep(int(msboxp.value))
        except OSError as tip:
            print(f'Erro: {tip}')
            exit(0)
        except ValueError as tip:
            print(f'Erro: {tip}')
            stopcore()
            d.error('Erro', 'Escolha um delay válido! (exemplo: 0.7)')


def vaicorekill():
    d.repeat(100, corekill)
    esc.hide()


def mschoice():
    escms.show()


def autor():
    d.info(text='Feito por Davidavida70\n=)', title='Sobre')


def vaicorepause():
    d.repeat(100, corepause)
    esc.hide()

def linguagem():
    exit(0)

def stopcore():
    status.value = 'Pausado...'
    d.cancel(corekill)
    d.cancel(corepause)


menus = MenuBar(d, toplevel=['Opções', 'Ajuda'],
                options=[
                    [['Selecionar pasta', pasta], ['Selecionar delay (s)', mschoice]],
                    [['Sobre', autor], ['Select language (em breve)', linguagem]]
                ])
fill = Text(d, align='bottom')
butao2 = PushButton(d, text='Parar', command=stopcore, align='bottom')
butao = PushButton(d, text='Começar', command=escolher, align='bottom')
fill2 = Text(d)
kill = PushButton(esc, text='Printar & exterminar', command=vaicorekill)
pause = PushButton(esc, text='Printar & pausar', command=vaicorepause)

d.display()
