from func_globais import *
from time import sleep

def menu_medico():
    print("\n---- Menu Médico ----\n")
    print("1. Criar Médico")
    print("2. Buscar Médico")
    print("3. Listar Médico")
    print("4. Atualizar Médico")
    print("5. Excluir Médico")
    print("0. Sair")

def loop_medico():
    while True:
        menu_medico()
        escolha = input("Digite o número da opção desejada: ")
        if escolha == "1":
            print("\n---- Novo Médico ----\n")
            medico = input("Nome do médico: ")
            especialidade = input("Especialidade do médico: ")
            criar_medico(medico, especialidade)
            print("Médico criado com sucesso!")

        elif escolha == "2":
            print("\n---- Busca Médico ----\n")
            id = input("Digite o ID do paciente que deseja buscar: ")
            medico = buscar_medico(id)
            if medico:
                print(f"ID: {medico[0]}")
                print(f"Nome: {medico[1]}")
                print(f"Especialidade: {medico[2]}")
            else:
                print("Paciente não encontrado.")

        elif escolha == "3":
            medicos = listar_medicos()
            if medicos:
                print("\n---- Lista de Médico ----\n")
                for medico in medicos:
                    print(f"ID: {medico[0]}, Nome: {medico[1]}, Especialidade: {medico[2]}")
                    print("\n")
            else:
                print("Não há medicos cadastrados.")

        elif escolha == "4":
            print("\n---- Atualiza Medico ----\n")
            id_medico_a_atualizar = input("Digite o ID do medico que deseja atualizar: ")
            novo_nome = input("Novo nome: ")
            nova_especialidade = input("Nova especialidade: ")
            atualizar_medico(id_medico_a_atualizar, novo_nome, nova_especialidade)

        elif escolha == "5":
            print("\n---- Deleta Médico ----\n")
            id_medico_a_excluir = input("Digite o ID do médico que deseja excluír: ")
            excluir_medico(id_medico_a_excluir)
        
        elif escolha == "0":
            print("Redirecionando para o menu principal...")
            sleep(2)
            print("Por favor aguarde...")
            sleep(3)
            break