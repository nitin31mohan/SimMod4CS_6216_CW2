from random import random

from strategy import Strategy
from params import Params

class Student:

    def __init__(self, strategy: Strategy):
        self.strategy = strategy
    
    def getEffort(self):
        return self.strategy.getEffort()

    def assignMarks(self, marks: float):
        self.marks = marks
        self.payOff = self.marks - (Params().a * self.getEffort())
        print(f"\tPayoff assigned to student: {round(self.payOff, 2)}")

    def updateStrategy(self, oppPayOff: float, oppStrategy: Strategy):
        oldStrat = self.strategy
        prob = (oppPayOff - self.payOff)
        rand = random()
        strategy = oppStrategy if (prob>0 and prob>rand) else self.strategy

        old_strat = "CONTRIBUTOR" if oldStrat.getEffort()==1.0 else "LAZY"
        new_strat = "CONTRIBUTOR" if strategy.getEffort()==1.0 else "LAZY"

        print(f"\tStrategy_OLD: {old_strat}")
        print(f"\tStrategy_UPDATED: {new_strat}")

        return not (oldStrat == strategy)
