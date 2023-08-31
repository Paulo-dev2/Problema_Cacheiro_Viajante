from Fitness import Fitness

import numpy as np, random, operator, pandas as pd

def rankRoutes(population):
    fitnessResults = {}
    for i in range(0,len(population)): 
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)

# A função de seleção recebe como primeiro parâmetro a saída da função rankRoutes
# para determinar qual rota utilizar
def selection(popRanked, eliteSize):
    selectionResults = []
    # Aqui é feito o cálculo de peso relativo de aptidão para cada indivíduo
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    # Adição do elitismo
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    # Aqui é feita a comparação de um número aleatório com esses pesos relativos
    # de aptidão para selecionar os indivíduos para a etapa de "Procriação"
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

# Essa função pega o resultado da nossa seleção anterior e busca estes indivíduos
# da nossa população
def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool

def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    # Aqui é feita a escolha do subconjunto aleatório do primeiro pai
    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    # Se o gene não existe no primeiro pai, então pega do segundo pai
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child

def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    # Aqui novamente usamos o elitismo para manter as melhores rotas/indivíduos 
    for i in range(0,eliteSize):
        children.append(matingpool[i])
    # Aqui utilizamos a função de breed mencionada acima para preencher o resto
    # dos indivíduos
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children

def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

# Aqui a mutação é aplicada na população
def mutatePopulation(population, mutationRate):
    mutatedPop = []
    
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop
    