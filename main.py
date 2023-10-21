from func_globais import *
from paciente import *
from medico import *
from quarto import *
from consulta import *

# Função para exibir o menu
def exibir_menu():
    print("\n----- CONEXÃO SAÚDE -----\n")
    print("Selecione uma opção:")
    print("1. Exibir opções de Quarto")
    print("2. Exibir opções de Paciente")
    print("3. Exibir opções de Médico")
    print("4. Exibir opções de Consulta")
    print("0. Sair")

# Loop principal
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "0":
        print("Validando Alterações ...")  
        sleep(3) 
        print("Salvando dados ...")
        sleep(2)
        print("Programa Finalizdo, Obrigado!")
        break
    elif escolha == "1":
        loop_quarto()

    elif escolha == "2":
        loop_paciente()
    
    elif escolha == "3":
        loop_medico()

    elif escolha == "4":
        loop_consulta()


# Fechar conexão
conn.close()
