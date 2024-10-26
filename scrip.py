import pyautogui as pg
import time

mensajes = int(input('¿cuantos mensajes?: '))
mensaje = input('mensaje: ')
time.sleep(3)

for i in range(mensajes):
    pg.write(f'{i+1}  {mensaje}')
    pg.press('enter')