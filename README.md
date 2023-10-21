Informações sobre o Sistema Hospitalar (Conexão Saúde)

Antes de rodar o código abra o MySQL e insira o seguinte comando:
CREATE DATABASE hospital;
---------------
As tabelas tem os seguintes relacionamentos:

Quartos e Pacientes têm um relacionamento de 1:1. Isso é alcançado pela chave estrangeira única na tabela de pacientes que faz referência à tabela de quartos. Cada paciente está associado a no máximo um quarto e cada quarto está associado a no máximo um paciente.

Pacientes e Consultas têm um relacionamento de 1:N (um paciente pode ter várias consultas, mas uma consulta pertence a apenas um paciente).

Médicos e Consultas têm um relacionamento de 1:N (um médico pode ter várias consultas, mas uma consulta pertence a apenas um médico).

Pacientes e Quartos têm um relacionamento de N:N (um paciente pode estar em vários quartos e um quarto pode ter vários pacientes). Esse relacionamento é implementado por meio da tabela de junção pacientes_quartos.

Relacionamentos: 1:1 entre Quartos-Pacientes, 1:N entre Pacientes-Consultas e Médicos-Consultas, e N:N entre Pacientes-Quartos.