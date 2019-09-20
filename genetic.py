from hill_climbing import *
import random

# gera populaçao inicial
# avaliar individuos
# enquanto não atende ao criterio de parada
#     coloca individuo mais adaptado na nova geracao
#     seleciona pais
#     realiza crossover
#     realiza mutacao
#     avalia individuos
# fim enq
# retorna mais adaptado


TIPOS = [ (1,3), (4,6), (5,7) ]

def genetic(types, max_size, n):
