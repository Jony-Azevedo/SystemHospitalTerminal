from conecta import conecta
conn = conecta()
cursor = conn.cursor()

# Criação das tabelas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS quartos (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        numero INT,
        capacidade INT
    )
""")
#UNIQUE -> Chave estrangeira unica
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        nome VARCHAR(50),
        quarto_id INT UNIQUE, 
        nascimento DATE,
        FOREIGN KEY (quarto_id) REFERENCES quartos(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicos (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        nome VARCHAR(255),
        especialidade VARCHAR(50)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS consultas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        paciente_id INT,
        medico_id INT,
        data_consulta DATE,
        FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
        FOREIGN KEY (medico_id) REFERENCES medicos(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes_quartos (
        paciente_id INT,
        quarto_id INT,
        FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
        FOREIGN KEY (quarto_id) REFERENCES quartos(id),
        PRIMARY KEY (paciente_id, quarto_id)
    )
""")

conn.commit()