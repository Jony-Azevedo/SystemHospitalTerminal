from func_globais import *
from time import sleep

def menu_paciente():
    print("\n---- Menu Paciente ----\n")
    print("1. Criar Paciente")# Para criar um paciente, deve-se primeiro ter quartos disponiveis
    print("2. Buscar Paciente")
    print("3. Listar Pacientes")
    print("4. Atualizar Paciente") # O quarto deve existir, senão não funcionará
    print("5. Excluir Paciente")
    print("0. Sair")

def loop_paciente():
    while True:
        menu_paciente()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            print("\n---- Novo Paciente ----\n")
            nome = input("Nome do paciente: ")
            quarto_id = input("ID do quarto do paciente: ")
            nascimento = input("Data de nascimento (aaaa/mm/dd):")
            criar_paciente(nome, quarto_id, nascimento)
            print("Paciente criado com sucesso!")

        elif escolha == "2":
            print("\n---- Busca Paciente ----\n")
            id = input("Digite o ID do paciente que deseja buscar: ")
            paciente = buscar_paciente(id)
            if paciente:
                print(f"ID: {paciente[0]}")
                print(f"Nome: {paciente[1]}")
                print(f"Quarto ID: {paciente[2]}")
                print(f"Nasimento: {paciente[3]}")
            else:
                print("Paciente não encontrado.")
        
        elif escolha == "3":
            pacientes = listar_pacientes()
            if pacientes:
                print("\n---- Lista de Paciente ----\n")
                for paciente in pacientes:
                    print(f"ID: {paciente[0]}, Nome: {paciente[1]}, Quarto ID: {paciente[2]}, Data de Nascimento: {paciente[3]}")
                    print("\n")
            else:
                print("Não há pacientes cadastrados.")

        elif escolha == "4":
            print("\n---- Atualiza Paciente ----\n")
            id_paciente_a_atualizar = input("Digite o ID do paciente que deseja atualizar: ")
            novo_nome = input("Novo nome: ")
            novo_quarto_id = input("Novo ID do quarto: ")
            novo_nascimento = input("Nova data nascimento aaaa/mm/dd: ")
            atualizar_paciente(id_paciente_a_atualizar, novo_nome, novo_quarto_id, novo_nascimento)
        
        elif escolha == "5":
            print("\n---- Deleta Paciente ----\n")
            id_paciente_a_excluir = input("Digite o ID do paciente que deseja excluír: ")
            excluir_paciente(id_paciente_a_excluir)

        elif escolha == "0":
            print("Redirecionando para o menu principal...")
            sleep(2)
            print("Por favor aguarde...")
            sleep(3)
            break