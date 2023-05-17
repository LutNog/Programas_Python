# Import

import random
from os import system, name

# Função para limpar a tela a cada execução

def limpa_tela():
    # Windows
    if name == "nt":
        _ = system('cls')
    # Mac ou Linux
    else:
        _ =system('clear')
        
        
# Função que desenha a forca na tela
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

# Função
def game():
    
    limpa_tela()
    
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")
    
    # Lista de palavras para o jogo
    palavras = ["ferrari", "palmeiras", 'abacaxi', 'abelha', 'ovelha', 'internet', 'nuvem', 'castelo', 'paris', 'roma', 'queijo']
    
    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)
    
    # List comprehension
    letras_descobertas = ['_' for letra in palavra]
    
    # Números de chances
    chances = 6
    
    # Lista para letras erradas
    letras_erradas = []
    
    # Loop enquanto o número de chances for maior que zero
    while chances > 0:
        
        print("\n")
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))
        print(display_hangman(chances))
        
        # Tentativa
        tentativa = input('\nDigite uma letra: ').lower()
        
        # Condicional
        if tentativa in palavra:
            index = 0
            
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
        # Condicional
        if "_" not in letras_descobertas:
            print("\n Você venceu, a palavra era:", palavra)
            break
      
    
    # Condicional
    if "_" in letras_descobertas:
        print("\n Você perdeu, a palavra era:", palavra)
    
# Bloco main
if __name__ == "__main__":
    game()
  
    