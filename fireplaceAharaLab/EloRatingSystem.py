from utils import *
import numpy

def PCalculation(X: Agent, Y: Agent):
    X.E = 1/(1+ pow(10,(Y.rating-X.rating)/400))
    Y.E = 1/(1+ pow(10,(X.rating-Y.rating)/400))

def newRate(winner: Agent,loser : Agent):
    winner.rating = winner.rating + 100*(1 - winner.E)
    loser.rating = loser.rating + 100*(0 - loser.E)