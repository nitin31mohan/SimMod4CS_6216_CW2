import copy
from strategy import Strategy

class SimpleStrat(Strategy):

    def __init__(self, effort):
        self.effort = effort

    def getEffort(self):
        return self.effort

    def equals(self, o):
        if o==self:
            return True
        if not (isinstance(o, SimpleStrat)):
            return False

        c = copy.deepcopy(SimpleStrat(o))

        return (0 if self.effort==c.effort else -1 if self.effort<c.effort else 1)==0


        

        