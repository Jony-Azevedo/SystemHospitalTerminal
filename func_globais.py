from create_db import *

# Funções CRUD para pacientes
def criar_paciente(nome, quarto_id, nascimento):
    cursor.execute("INSERT INTO pacientes (nome, quarto_id, nascimento) VALUES (%s, %s,%s)", (nome, quarto_id, nascimento))
    conn.commit()

def buscar_paciente(id):
    cursor.execute("SELECT * FROM pacientes WHERE id = %s", (id,))
    return cursor.fetchone()

def listar_pacientes():
    cursor.execute("SELECT * FROM pacientes")
    return cursor.fetchall()

def atualizar_paciente(id, nome, quarto_id, nascimento):
    cursor.execute("UPDATE pacientes SET nome = %s, quarto_id = %s, nascimento = %s WHERE id = %s", (nome, quarto_id, nascimento, id))
    conn.commit()

def excluir_paciente(id):
    # Verifica se o ID existe
    cursor.execute("SELECT id FROM pacientes WHERE id = %s", (id,))
    paciente_existente = cursor.fetchone()

    if paciente_existente:
        # O paciente existe
        cursor.execute("DELETE FROM pacientes WHERE id = %s", (id,))
        conn.commit()
        print(f"Paciente com ID {id} foi excluído com sucesso!")
    else:
        # O paciente não encontrado
        print(f"Não foi possível encontrar um paciente com ID {id}. Nenhuma exclusão foi realizada.")

# Funções CRUD para médicos
def criar_medico(nome, especialidade):
    cursor.execute("INSERT INTO medicos (nome, especialidade) VALUES (%s, %s)", (nome,especialidade))
    conn.commit()

def buscar_medico(id):
    cursor.execute("SELECT * FROM medicos WHERE id = %s", (id,))
    return cursor.fetchone()

def listar_medicos():
    cursor.execute("SELECT * FROM medicos")
    return cursor.fetchall()

def atualizar_medico(id, nome, especialidade):
    cursor.execute("UPDATE medicos SET nome = %s, especialidade = %s WHERE id = %s", (nome, especialidade, id))
    conn.commit()

def excluir_medico(id):
    cursor.execute("DELETE FROM medicos WHERE id = %s", (id,))
    conn.commit()

# Funções CRUD para consultas
def criar_consulta(paciente_id, medico_id, data_consulta):
    cursor.execute("INSERT INTO consultas (paciente_id, medico_id, data_consulta) VALUES (%s, %s, %s)", (paciente_id, medico_id, data_consulta))
    conn.commit()

def buscar_consulta(id):
    cursor.execute("SELECT * FROM consultas WHERE id = %s", (id,))
    return cursor.fetchone()

def listar_consultas():
    cursor.execute("SELECT * FROM consultas")
    return cursor.fetchall()

def atualizar_consulta(id, paciente_id, medico_id, data_consulta):
    cursor.execute("UPDATE consultas SET paciente_id = %s, medico_id = %s, data_consulta = %s WHERE id = %s", (paciente_id, medico_id, data_consulta, id))
    conn.commit()

def excluir_consulta(id):
    cursor.execute("DELETE FROM consultas WHERE id = %s", (id,))
    conn.commit()

def criar_quarto(numero, capacidade):
    cursor.execute("INSERT INTO quartos (numero, capacidade) VALUES (%s, %s)", (numero, capacidade))
    conn.commit()

# Funções para relacionamento N para N entre pacientes e quartos
def associar_paciente_quarto(paciente_id, quarto_id):
    cursor.execute("INSERT INTO pacientes_quartos (paciente_id, quarto_id) VALUES (%s, %s)", (paciente_id, quarto_id))
    conn.commit()

def desassociar_paciente_quarto(paciente_id, quarto_id):
    cursor.execute("DELETE FROM pacientes_quartos WHERE paciente_id = %s AND quarto_id = %s", (paciente_id, quarto_id))
    conn.commit()

def listar_pacientes_quarto(quarto_id):
    cursor.execute("SELECT pacientes.* FROM pacientes INNER JOIN pacientes_quartos ON pacientes.id = pacientes_quartos.paciente_id WHERE pacientes_quartos.quarto_id = %s", (quarto_id,))
    return cursor.fetchall()

def obter_informacoes_consulta():
    print("\n---- Informações Completas das Consultas ----\n")
# Consulta usando JOIN para obter informações completas sobre uma consulta
    cursor.execute("""
        SELECT consultas.*, pacientes.nome AS nome_paciente, medicos.nome AS nome_medico
        FROM consultas
        INNER JOIN pacientes ON consultas.paciente_id = pacientes.id
        INNER JOIN medicos ON consultas.medico_id = medicos.id
    """)
    consulta = cursor.fetchone()
    print(f"ID da Consulta: {consulta[0]}")
    print(f"Paciente: {consulta[4]}")
    print(f"Médico: {consulta[5]}")
    print(f"Data da Consulta: {consulta[3]}")
