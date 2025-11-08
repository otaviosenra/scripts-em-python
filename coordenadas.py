import pyautogui
import time

print('Mova o mouse sobre a seta azul na tela...')
# Loop para capturar a posição do mouse e a cor do pixel
try:
    while True:
        x, y = pyautogui.position()
        # Captura a cor do pixel atual
        cor_rgb = pyautogui.pixel(x, y) 
        
        # O print vai atualizando o console a cada loop
        print(f"X: {x}, Y: {y} | RGB: {cor_rgb}", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print('\nCaptura finalizada.')