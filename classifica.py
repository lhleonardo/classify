#### LEGENDA: eh gordinho, tem perna curta, faz au au

# análises de dados 
cachorro1 = [1, 1, 1]
cachorro2 = [0, 0, 1]
cachorro3 = [1, 0, 1]
porco1    = [1, 1, 0]
porco2    = [0, 1, 0]
porco3    = [1, 0, 0]

# matriz de dados agrupados
dados = [cachorro1, cachorro2, cachorro3,
        porco1, porco2, porco3]

# marcações, em ordem, dos valores equivalentes a cada dado na matriz
marcacoes = [1, 1, 1, -1, -1, -1]

# valor que deverá sofrer análise para dedução do que ele poderá "ser"
misterioso = [1, 0, 1]

# importação do algoritmo de análise
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()

modelo.fit(dados, marcacoes)
