import pyautogui
import time
from collections import namedtuple

# Use o valor RGB exato que você encontrou na seta azul
COR_AZUL_SETA = (65, 0, 144) # Exemplo: Ajuste este valor!
TOLERANCIA_COR = 25           # Tolerância de 0 a 255. 5-10 é um bom valor para jogos.
INTERVALO_BUSCA = 0.01        # Mais rápido que a busca por imagem (10 milissegundos)

PixelCheck = namedtuple('PixelCheck', ['x', 'y', 'tecla'])

# --- Mapeamento de Coordenada (X, Y) para Tecla de Ação ---
# Você precisa encontrar 4 coordenadas, uma para cada direção,
# onde a cor azul aparece APENAS para aquela direção.
CHECKPOINTS = [
    # Coordenada (X, Y) | Tecla a pressionar ('right', 'left', 'up', 'down')
    PixelCheck(x=1011, y=550, tecla='right'), # Exemplo: Pixel para a Direita
    PixelCheck(x=912, y=551, tecla='left'),  # Exemplo: Pixel para a Esquerda
    PixelCheck(x=973, y=483, tecla='up'),    # Exemplo: Pixel para Cima
    PixelCheck(x=945, y=584, tecla='down'),  # Exemplo: Pixel para Baixo
]


def bot_qte_pixel_color():
    print("Bot QTE por Cor de Pixel Iniciado! Velocidade máxima.")
    pyautogui.FAILSAFE = True
    
    while True:
        tecla_pressionada = False
        
        for check in CHECKPOINTS:
            # Verifica se o pixel na coordenada (x, y) corresponde à COR_AZUL_SETA
            # dentro da tolerância definida.
            if pyautogui.pixelMatchesColor(check.x, check.y, COR_AZUL_SETA, tolerance=TOLERANCIA_COR):
                
                print(f"Cor AZUL encontrada em ({check.x}, {check.y}). Pressionando: {check.tecla.upper()}")
                pyautogui.press(check.tecla)
                
                tecla_pressionada = True
                
                # Pausa para dar tempo do jogo processar o comando e a seta sumir
                time.sleep(0.3) 
                break # Sai do loop de verificação para começar um novo ciclo
        
        # Pausa antes da próxima varredura de tela
        time.sleep(INTERVALO_BUSCA)

if __name__ == "__main__":
    try:
        print("\nINSTRUÇÃO: Ajuste COR_AZUL_SETA e as coordenadas (X, Y) em CHECKPOINTS.")
        bot_qte_pixel_color()
        
    except KeyboardInterrupt:
        print("\nBot Encerrado pelo usuário (Ctrl+C).")
    except pyautogui.FailSafeException:
        print("\nBot Encerrado pela função de segurança (mouse no canto superior esquerdo).")
    except Exception as e:
        print(f"\nOcorreu um erro fatal inesperado: {e}")