from funcao_de_download import *

limpar_tela()
print("Faça seu download de audio e video aqui\n")

print("Pode baixar audio e media")
print("1- Video mp4")
print("2- Audio mp3\n")
escolha = int(input("Qual deseja: "))
limpar_tela()

if escolha == 1:
    baixar_mp4()


elif escolha == 2:
    baixar_mp3()

