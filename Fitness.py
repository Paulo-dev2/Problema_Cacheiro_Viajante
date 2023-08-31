class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0 
    
    def routeDistance(self):
        if self.distance ==0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                toCity = None
                
                # precisa terminar na cidade onde começou, então faz essa verificação
                # se não for o último nó, adiciona a próxima "cidade" a ser visitada
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                # caso contrário, é o último nó e atribui o primeiro nó visitado
                else:
                    toCity = self.route[0]
                
                # calcula a distância entre a cidade inicial e a próxima 
                pathDistance += fromCity.distance(toCity)

            self.distance = pathDistance
        return self.distance
    
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness