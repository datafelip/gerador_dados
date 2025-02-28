import pandas as pd
import random
from faker import Faker

fake = Faker("pt_BR")

marcas_modelos = {
    "Toyota": ["Corolla", "Hylux", "Yaris"],
    "Chevrolet": ["Onix", "S10", "Tracker"],
    "Ford": ["Ka", "Ranger", "EcoSport"],
    "Volkswagen": ["Gol", "Polo", "T-Cross"],
    "Fiat": ["Uno", "Mobi", "Argo"]
}

formas_pagamento = ["Á vista", "Consórcio", "Financiamento", "Leasing"]
cores = ["Preto", "Branco", "Cinza", "Vermelho", "Azul"]
sexo_opcoes = ["Masculino", "Feminino"]

dados = []

while True: 
    try:
        max_iteracoes = int(input("Digite a quantidade de dados que deseja ter: "))
        if max_iteracoes <= 0:
            print("Digite uma entrada válida")
        else:
            break
    except ValueError:
        print("Digite uma entrada válida.")
        
for id in range(1, max_iteracoes + 1):
    sexo = random.choice(sexo_opcoes)
    nome = fake.first_name_male() if sexo == "Masculino" else fake.first_name_female()
    sobrenome = fake.last_name()
    nome_completo = f"{nome} {sobrenome}"

    idade = random.randint(18, 20)
    cpf = fake.cpf()
    email = fake.email()
    telefone = fake.phone_number()
    cidade = fake.city()
    estado = fake.state_abbr()

    marca = random.choice(list(marcas_modelos.keys()))
    modelo = random.choice(marcas_modelos[marca])
    ano_fabricacao = random.randint(2015, 2025)
    cor = random.choice(cores)
    valor_venda = round(random.uniform(30000, 250000), 2)
    data = fake.date_between(start_date="-2y", end_date="today")
    forma_pagamento = random.choice(formas_pagamento)

    dados.append(
        [id, nome_completo, idade, cpf, sexo, email, telefone, cidade, estado,
         marca, modelo, ano_fabricacao, cor, valor_venda, data, forma_pagamento
         ]
        )
    colunas = [
        "IDCLIENTE", "NOME", "IDADE", "CPF", "SEXO", "EMAIL", "TELEFONE", "CIDADE", "ESTADO", "MARCA_VEICULO", "MODELO_VEICULO", 
        "ANO_FABRICACAO", "COR_VEICULO", "VALOR_VENDA", "DATA_COMPRA", "FORMA_PAGAMENTO"
    ]
    df_vendas = pd.DataFrame(dados, columns=colunas)
    df_vendas.head()

    df_vendas.to_json("vendas.json", orient="records", indent=4, force_ascii = False)
