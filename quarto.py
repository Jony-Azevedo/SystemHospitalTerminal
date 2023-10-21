from func_globais import *
from time import sleep

def menu_quarto():
    print("\n---- Menu Quarto ----\n")
    print("1. Criar Quarto")# Para criar um paciente, deve-se primeiro ter quartos disponiveis
    print("2. Associa paciente ao Quarto")
    print("3. Desassocia paciente a quarto")
    print("4. Lista Pacientes no Quarto") # O quarto deve existir, senão não funcionará
    print("5. Excluir Quarto")
    print("0. Sair")

def loop_quarto():
    while True:
        menu_quarto()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            print("\n---- Novo Quarto ----\n")
            numero_quarto = input("Número do quarto: ")
            capacidade_quarto = input("Capacidade do quarto: ")
            criar_quarto(numero_quarto, capacidade_quarto)


        elif escolha == "2":
            print("---- Associa Paciente ao Quarto ----\n")
            paciente_id = input("ID do paciente: ")
            quarto_id = input("ID do quarto: ")
            associar_paciente_quarto(paciente_id, quarto_id)
            print("Paciente associado ao quarto com sucesso!")
        
        elif escolha == "3":
            print("\n---- Desassocia Paciente e Quarto ----\n")
            paciente_id = input("ID do paciente: ")
            quarto_id = input("ID do quarto: ")
            desassociar_paciente_quarto(paciente_id, quarto_id)
            print("Paciente desassociado do quarto com sucesso!")

        elif escolha == "4":
            print("\n---- Lista de pacientes no quarto ----\n")
            # Solicita ao usuário o ID do quarto para listar os pacientes associados a ele.
            quarto_id = input("ID do quarto: ")
            pacientes_associados = listar_pacientes_quarto(quarto_id)
            if pacientes_associados:
                print("Pacientes associados ao quarto:")
                for paciente in pacientes_associados:
                    print(f"ID: {paciente[0]}, Nome: {paciente[1]}, Data de Nascimento: {paciente[3]}")
            else:
                print("Nenhum paciente associado a este quarto.")

        elif escolha == "0":
            print("Redirecionando para o menu principal...")
            sleep(2)
            print("Por favor aguarde...")
            sleep(3)
            break