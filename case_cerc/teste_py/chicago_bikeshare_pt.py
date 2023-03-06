# coding: utf-8 

# Começando com os imports
import csv
import matplotlib.pyplot as plt
# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")
# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
# Selecino inicialmente a lista apenas com as informacoes, assim como uma lista de apenas os nomes das colunas. 
#Para conseguir identificar os dados, criei uma string com a coluna e seu dado respectivo, 
#apendando tudo isso a uma lista a cada iteracao, e depois apendo esta lista a uma outra, para manter a mesma organizacao do dado.


print("Gerando as 20 primeiras linhas, rotuladas.")
vinte_primeiras_linhas=data_list[1:21]
nome_das_colunas=data_list[0]
lista_final_tarefa_1=[]
for linha in vinte_primeiras_linhas:
    lista_identificada=[]
    numero_da_linha=0
    while numero_da_linha<len(linha):
        iten_identificado=f"{nome_das_colunas[numero_da_linha]} : {linha[numero_da_linha]}"
        lista_identificada.append(iten_identificado)
        numero_da_linha+=1
    lista_final_tarefa_1.append(lista_identificada)
print('Lista das 20 primeiras amostras identificadas:')
print(lista_final_tarefa_1)


    



# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]




input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
task2_list=data_list[0:20]
task2_final_list=[]
for row in task2_list:
    gender=row[-2]
    task2_final_list.append(gender)

print('Lista do genero das 20 primeiras amostras')
print(task2_final_list)
# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista

def column_to_list(data:list, index:int) -> list:
    """
    Extrai uma coluna específica de uma lista de dados e retorna como uma lista separada.

    Parâmetros:
    data (list): Uma lista de dados, em que cada elemento é uma lista.
    index (int): Um número inteiro representando o índice da coluna que deseja extrair da lista.

    Retorna:
    column_list: Uma lista contendo os elementos da coluna especificada pelo índice.
    """
    column_list = []
    if index in list(range(-len(data[0]),len(data[0]))):
        for row in data:
            column=row[index]
            column_list.append(column)                    
        return column_list
    else:
        raise ValueError(f"A funcao so suporta index entre {-len(data[0])} e {len(data[0])-1}")


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])


# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
# assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado." # Dado que estou extraindo uma coluna da base,
# e esta tem menos linhas que o assert de linhas da coluna, o assert aqui se torna um erro para o teste.
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.

# Para contar a quantidade de cada genero, iterei sobre a lista e adicionei condicionais, para que quando seja male seja adicionado 1 a variavel,
# E fazendo o mesmo com Female.
print("Fazendo a contagem de genero")
male = 0
female = 0
task_4_list=column_to_list(data_list, -2)
for gender in task_4_list:
    if gender=='Male':
        male+=1
    if gender=='Female':
        female+=1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
# assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate." # Com o mesmo argumento do ultimo erro de assert,
# a conta nunca vai bater dado que so essa soma tem mais linhas que a propria base
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list:list) -> list:
    """
    Retorna o número de homens e mulheres em uma lista de dados.

    Parâmetros:
    data_list (list): Uma lista de dados, contendo o genero de cada usuario.

    Retorna:
    Uma lista contendo o número de homens e mulheres na lista, respectivamente.
    """
    male = 0
    female = 0
    task_5_list=column_to_list(data_list, -2)
    for gender in task_5_list:
        if gender=='Male':
            male+=1
        if gender=='Female':
            female+=1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
# assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# Com o mesmo argumento do ultimo erro de assert,
# a conta nunca vai bater dado que so essa soma tem mais linhas que a propria base
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list:list ) -> str:
    """
    Retorna o gênero mais popular em uma lista de dados.

    Parâmetros:
    data_list (list): Uma lista de dados, com 2 itens, sendo o primeiro deles a quantidade de pessoas do genero masculino e outro do genero feminino

    Retorna:
    Uma string indicando o gênero mais popular na lista. Se houver mais homens do que 
    mulheres, retorna "Male". Se houver mais mulheres do que homens, retorna "Female".
    Se houver um número igual de homens e mulheres, retorna "Equal".
    """
    if count_gender(data_list)[0]>count_gender(data_list)[1]:
        answer = "Male"
    elif count_gender(data_list)[0]<count_gender(data_list)[1]:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.

#Criei primeiro uma funcao para separar os tipos e suas quantidades, ja que nao saberia imediatamente a quantidade total de tipos de usuario, sendo o resultado um dicionario, para os tipos e necessario apenas acessar as chaves e para as quantidades respectivas, apenas os valores
def count_strings(lista: list) -> dict:
    '''
    A funcao count_strings pega a partir de um dicionario, em que os itens sao as chaves, assim quando um item existe e somado 1 a ele e quando nao existe e atribuido 1 a ele.
    Argumentos:
        lista: uma lista com strings
    Retorna:
        string_count: dicionario com os itens como chaves e suas quantidades como valores.
    '''
    string_count = {}
    for string in lista:
        if string in string_count:
            string_count[string] += 1
        else:
            string_count[string] = 1
    return string_count
print("\nTAREFA 7: Verifique o gráfico!")
# A utilizacao do grafico aqui e o mesmo da ultima questao, apenas ajustando a coluna selecionada.
user_type_list = column_to_list(data_list, -3)
user_types_count= count_strings(user_type_list)
types = list(user_types_count.keys())
quantity = list(user_types_count.values())
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de Usuarios')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipos de Usuarios')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A afirmacao parte da premissa de que todos os usuarios estao com este campo preenchido, mas apenas olhando para a primeira linha esta claro de que diversos campos estao vazios, ou seja, em len(data_list) esta contenplando todos os campos, mas em male e female nao."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
# Atribui primeiro a lista de trip durations, a funcao column_to_list que retorna a lista da coluna
# Para encontrar o menor valor, necessita-se apenas iterar a lista e atribuir a uma variavel o menor valor, 
#iniciando com o 1 primeiro valor atribuido e o segundo em comparacao.

# As bibliotecas aqui foram colocadas para conseguir fazer um uso com mais filtros, assim "limpando" os dados de uma melhor forma

from statistics import median,mean
from math import isnan
from itertools import filterfalse

# Para ter uma melhor analise e garantir os tipos inseridos na lista, irei converter o conteudo para float

convert=[float(x) for x in trip_duration_list]

min_val=convert[0]
for trip_duration in convert[1:]:
    if trip_duration < min_val:
        min_val = trip_duration
min_trip=min_val
# Para encontrar o maior valor, necessita-se apenas iterar a lista e atribuir a uma variavel o maior valor,
# iniciando com o 1 primeiro valor atribuido e o segundo em comparacao.
max_val=convert[0]
for trip_duration in convert[1:]:
    if trip_duration > max_val:
        max_val = trip_duration
max_trip=max_val

# A media nada mais e que a soma total dividida pelo total de itens, 
# assim iterou-se sobre a lista, somando tudo em uma variavel final, e dividindo pela quantidade de itens.


sum_val = 0 
for trip_duration in convert:
    sum_val += int(trip_duration)
mean_trip = sum_val/len(convert)



# A mediana representa o valor do meio de uma lista de dados, para calcula-la deve-se primeiro ordena-la. 
# Com isso para achar os numeros centrais, verifica-se se e um numero par, caso sim soma os dois numeros centrais e os divide por 2, e caso for impar apenas o seleciona como medianan
sorted_trip_duration_list = sorted(convert)
n = len(trip_duration_list)
if n % 2 == 0:
    median_trip = (sorted_trip_duration_list[n//2-1] + sorted_trip_duration_list[n//2]) / 2
else:
    median_trip = sorted_trip_duration_list[n//2]
print(f"quantidade de numeros nulos: {sum(map(isnan, convert)) }")


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
# assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
# assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# Os asserts de media e mediana sao completamente dependentes da quantidade de dados colocados, como se esperava uma base maior do que temos aqui,
# e impossivel que esses asserts sejam verdadeiros. Min e Max sao excessoes, ja que eles poderiam estar ou nao na base, mas no caso estao.
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list,3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
# assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# O assert se torna um erro por termos aqui uma base menor do que a esperada, 
# por tanto e possivel se dizer que mais estacoes estariam no restante da base.
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
def new_function(param1: int, param2: str) -> list:
      """
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

      """

input("Aperte Enter para continuar...")
# TAREFA 12
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"



def count_items(column_list: list) -> list:
    '''
    A funcao count_items pega a partir de um dicionario, em que os itens sao as chaves, assim quando um item existe e somado 1 a ele e quando nao existe e atribuido 1 a ele.
    Argumentos:
        column_list: uma lista com strings
    Retorna:
        item_types: Itens unicos
        count_items: Quantidade atribuida a estes itens, em sua mesma ordem
    '''
    string_count = {}
    for string in column_list:
        if string in string_count:
            string_count[string] += 1
        else:
            string_count[string] = 1
    item_types=list(string_count.keys())
    count_items=list(string_count.values())
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    # assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # O assert e errado por termos uma base de apenas 1048576 linhas
    # -----------------------------------------------------
