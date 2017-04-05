#### LEGENDA: eh gordinho, tem perna curta, faz au au

# análises de dados 
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [1, 1, 1]
porco1    = [1, 1, 0]
porco2    = [0, 1, 0]
porco3    = [1, 1, 0]

# matriz de dados agrupados
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# marcações, em ordem, dos valores equivalentes a cada dado na matriz
marcacoes = [1, 1, 1, -1, -1, -1]

# importação do algoritmo de análise
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()

modelo.fit(dados, marcacoes)

# valor que deverá sofrer análise para dedução do que ele poderá "ser"
misterioso1 = [1, 1, 1] # cachorro
misterioso2 = [0, 0, 1] # cachorro
misterioso3 = [1, 0, 0] # porco

# agrupamento dos elementos misteriosos
testes = [misterioso1, misterioso2, misterioso3]

# resultado que deverá ser obtido dos elementos misteriosos
marcacoes_testes = [-1, -1, 1]

# tenta deduzir o que é o valor misterioso
resultado = modelo.predict(testes)

# faz a subtração dos dois arrays, para que o resultado fique, por exemplo:
# resultado        = [-1, 1, 1]
# marcacoes_testes = [-1, -1, 1]
#
# diferencas       = [(-1 - (-1)), (1 - (-1)), (1 - 1)], 
# resultando em    => [0, 2, 0]
# onde os valores que forem iguais a zero são os acertos da previsão
diferencas = resultado - marcacoes_testes

# seleciona apenas os acertos da previsão, ou seja, os elementos com valor zero
acertos = [d for d in diferencas if d == 0]

# faz o cálculo de percentual para mostrar o resultado ao usuário
total_de_acertos = len(acertos)
total_de_elementos = len(testes)
percentual_acertos = (total_de_acertos/total_de_elementos) * 100
margem_de_erro = 100 - percentual_acertos

print()
print("---------------Classificador de Animais---------------")
print("Quantidade de Elementos:", total_de_elementos)
print("Acertos:", total_de_acertos)
print("Percentual de acertos:", str(percentual_acertos) + "%")
print("Margem de erro:", str(margem_de_erro) + "%")
print("---------------Fim da classificação-------------------")