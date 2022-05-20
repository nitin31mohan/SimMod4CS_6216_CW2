# from collections.abc import Sequence, Iterable
# from typing import Mapping, Generic

from random import shuffle
from typing import List


from student import Student
from strategy import Strategy

class Classroom:
    # def __init__(self, students: list()):
    def __init__(self, students: List[Student]):
    # def __init__(self):
        # self.students = List[Student]
        self.students = students
    
    def updateStrategies(self):
        opponents = list(list(self.students))

        count: int = 0

        print("\n")

        for i in range(len(self.students)):
            shuffle(opponents)
            opponent = opponents[0]
            print(f"Student {i+1}")
            if self.students[i].updateStrategy(opponent.payOff, opponent.strategy):
                count+=1
        
        print(f"\n{count}/{len(self.students)} students updated their strategies.\n")
        # print("\Semester end.")

    def getConcentration(self, S: Strategy) -> float:
        count: float = 0

        for i in range(len(self.students)):
            if S == self.students[i].strategy:
                count+=1
        
        return count/len(self.students)

# students = list(Student)