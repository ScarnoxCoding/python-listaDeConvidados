# Lista de convidados que foram convidados para a festa
convidados_da_festa = ['Maria', 'João', 'Ana', 'Carlos', 'Mariana']

# Dicionário vazio para armazenar o status de presença de cada pessoa
status_presenca = {}

print("--- Verificação da Lista de Convidados ---")

# Esta é a lista de pessoas que tentaram entrar na festa
lista_de_chegadas = ['João', 'Ana', 'Pedro', 'Maria', 'Mariana']

# Usamos um laço 'for' para percorrer cada pessoa que chegou
for pessoa in lista_de_chegadas:
    # Usamos uma estrutura 'if' para checar se o nome da pessoa está na lista de convidados
    if pessoa in convidados_da_festa:
        # Se a pessoa está na lista, o status de presença é marcado como "Confirmado"
        print(f"Olá, {pessoa}! Bem-vindo(a) à festa.")
        # Adicionamos a pessoa e seu status ao dicionário
        status_presenca[pessoa] = "Confirmado"
        
    else:
        # Se a pessoa NÃO está na lista, usamos 'else' para lidar com isso
        print(f"Desculpe, {pessoa}. Seu nome não está na lista de convidados.")
        # Adicionamos a pessoa e seu status ao dicionário, mas como "Não Convidado"
        status_presenca[pessoa] = "Não Convidado"
