Ultilizamos o algoritimo genético para "resolver o problema do cacheiro viajante",  que tem como objetivo determinar a menor rota para percorrer uma série de cidades, 
garantindo que todas as cidades sejam visitadas uma única vez e que no final se retorne a cidade de origem. 
É importante mencionar que não importa a ordem que as cidades são visitadas e que todas estão conectadas entre si.
O Problema do Caixeiro Viajante é um problema de otimização combinatória que pertence a categoria de problemas NP - Completos.

Conceitos gerais para os algoritmos:
Gene: uma cidade representada por coordenadas.

Indivíduo: uma rota única que satisfaz as condições do problema.

População: conjunto de indivíduos, ou seja, uma coleção de rotas possíveis.

Pais: combinação de duas rotas para criar uma rota nova.

Fitness: uma função que avalia a melhor rota (no caso, a rota que tem menor distância).

Elitismo: um fator que permite passar para próximas gerações indivíduos com melhor desempenho.

Mutação: uma forma de variar a população trocando de forma aleatória duas cidades em uma rota.

O Algoritmo
Para resolver este problema, foi escolhido um algoritmo genético.

O Algoritmo genético possui as seguintes fases:

Criação de uma população inicial
Determinação do "fitness"
Seleção dos pais para procriação
Procriação
Mutação
Repetição do ciclo por x gerações

Neste modelo foi acrescentado um fator de elitismo para a procriação e escolha do melhor indivíduo. Este fator faz com que indivíduos com melhor desempenho sejam tranferidos para as próximas gerações.

Eu separaei as fases do algoritimo em arquivos com suas seguintes fases.

Ultilizamos este código e a explicação do código: https://www.youtube.com/watch?v=M0LIXBc61W4&t=4s, para entendermos melhor.
