class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    # Calcula a distância euclidiana
    def distance(self, toCity):
      return ((self.x - toCity.x) ** 2 + (self.y - toCity.y) ** 2) ** 0.5

    # Imprime as coordenadas como (x,y)
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"