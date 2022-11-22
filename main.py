import pandas as pd

#pd.Series([LISTA DE VALORES], [LISTA DE ÍNDICES], nome)

lista = ('João', 'Carlos', 'Henrique', 'Davi', 'Joana')
s1 = pd.Series(lista, name = 'nomes')

nomes = ('Ana', 'Carlos', 'Henrique', 'Davi', 'Joana')
s1 = pd.Series(lista, ['A', 'C', 'H', 'D', 'J'])
print(s1)

s1 = pd.Series(4, range(10))
print(s1)

numeros = pd.Series([11, 27, 10, 77, 83, 104, 2.4])
print('Média:',numeros.mean())
print('Máximo:',numeros.max())
print('Mínimo',numeros.min())
print('Desvio padrão:',numeros.std())

print(f'Descrição\n',numeros.describe())

cadastro = {
    'Nome': ['Joana', 'Patricia', 'Paulo'],
    'Idade': [35, 21, 44],
    'Estado': ['SP', 'SC', 'PE']
}

cadastro_df = pd.DataFrame(cadastro)
print(cadastro_df)

#display(cadastro_df)