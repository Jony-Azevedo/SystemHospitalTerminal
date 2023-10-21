from func_globais import *
from time import sleep

def menu_consulta():
    print("\n---- Menu Consulta ----\n")
    print("1. Criar Consulta")
    print("2. Buscar Consulta")
    print("3. Listar Consultas")
    print("4. Atualizar Consulta") 
    print("5. Excluir Consulta")
    print("6. Obter Informações completas de Consultas")
    print("0. Sair")

def loop_consulta():
    while True:
        menu_consulta()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            print("\n--- Nova consulta ----\n")
            paciente_id = input("ID paciente: ")
            medico_id = input("ID medico: ")
            data_consulta = input("Data consulta (aaaa/mm/dd): ")
            criar_consulta(paciente_id, medico_id, data_consulta)
            print("Consulta cruiada com sucesso!")

        elif escolha == "2":
            print("\n---- Busca Consulta ----\n")
            id = input("Digite o ID da consulta que deseja buscar: ")
            consulta = buscar_consulta(id)
            if consulta:
                print(f"ID consulta: {consulta[0]}")
                print(f"Id paciente: {consulta[1]}")
                print(f"ID medico: {consulta[2]}")
                print(f"data da consulta: {consulta[3]}")
            else:
                print("Consulta não encontrada.")

        elif escolha == "3":
            consultas = listar_consultas()
            if consultas:
                print("\n---- Lista de Consultas ----\n")
                for consulta in consultas:
                    print(f"ID consulta: {consulta[0]}, ID paciente: {consulta[1]}, ID medico: {consulta[2]}, data da consulta: {consulta[3]}")
                    print("\n")
            else:
                print("Não há consultas agendadas.")

        elif escolha == "4":
            print("\n---- Atualiza Consulta ----\n")
            id_consulta = input("ID da consulta que deseja atualizar: ")
            novo_paciente_id = input("Novo ID do paciente: ")
            novo_medico_id = input("Novo ID do médico: ")
            nova_data_consulta = input("Nova data da consulta (aaaa/mm/dd): ")
            atualizar_consulta(id_consulta, novo_paciente_id, novo_medico_id, nova_data_consulta)
            print("Consulta atualizada com sucesso!")

        elif escolha == "5":
            print("\n---- Deleta Consulta ----\n")
            id_consulta_a_excluir = input("Digite o ID do médico que deseja excluír: ")
            excluir_consulta(id_consulta_a_excluir)
        
        elif escolha == "6":
            obter_informacoes_consulta()

        elif escolha == "0":
            print("Redirecionando para o menu principal...")
            sleep(2)
            print("Por favor aguarde...")
            sleep(3)
            break