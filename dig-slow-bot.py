import pyautogui
import time


def bot_start():
    print("Bot QTE por Cor de Pixel Iniciado! Velocidade máxima.")
    pyautogui.FAILSAFE = True
    
    # 'right' para minerar para direita, 'left' para esquerda, 'up' para cima, 'down' para baixo
    while True:
        time.sleep(2)
        pyautogui.press('right')
        pyautogui.press('z')
        pyautogui.press('p')
        pyautogui.press('enter')
        
if __name__ == "__main__":
    try:
        print("\nINSTRUÇÃO: Ajuste COR_AZUL_SETA e as coordenadas (X, Y) em CHECKPOINTS.")
        bot_start()
        
    except KeyboardInterrupt:
        print("\nBot Encerrado pelo usuário (Ctrl+C).")
    except pyautogui.FailSafeException:
        print("\nBot Encerrado pela função de segurança (mouse no canto superior esquerdo).")
    except Exception as e:
        print(f"\nOcorreu um erro fatal inesperado: {e}")