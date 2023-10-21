import mysql.connector


db_config = {
    "host":"localhost",
    "user":"root",
    "password":"1234",
    "database":"hospital"
}
# Conecta ao banco de dados
def conecta():
    return mysql.connector.connect(**db_config)