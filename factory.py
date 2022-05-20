from random import shuffle
import math
from typing import List

from classroom import Classroom
from group import Group
from strategy import Strategy
from student import Student
from simpleStrat import SimpleStrat

class Factory:

    def __init__(self) -> None:
        pass

    def generateSimpleClass(self, size: int, initX: float, effort1: float, effort2: float) -> Classroom:
        # print("--------------\nSemester start")
        print("\nInitiating student population...")
        efforts: float = self.getEfforts(size, initX, effort1, effort2)
        strategies: List[Strategy] = self.getStrategies(efforts)
        students: List[Student] = self.getStudents(strategies)
        classroom = Classroom(students)

        return classroom

    def makeGroups(self, students: List[Student], groupSize: int) -> List[Group]:
        print("Sorting into groups...")
        studentList = list(list(students))
        shuffle(studentList)
        numGroups = len(students)//groupSize
        groups = [] #list(Group)

        for i in range(numGroups):
            studentsForGroup = []   #list(Student)
            for j in range(groupSize):
                studentsForGroup.append(studentList[(i * groupSize) + j])

            groups.append(Group(studentsForGroup))

        return groups


    def getStudents(self, strategies: List[Strategy]) -> List[Student]:
        size: int = len(strategies)

        students = []

        for i in range(size):
            students.append(Student(strategies[i]))
        
        return students

    def getStrategies(self, efforts: float) -> List[Strategy]:
        size: int = len(efforts)
        strategies = []

        # print(f"-----SimpleStrat(efforts[0]), {SimpleStrat(efforts[0])}")

        for i in range(size):
            strategies.append(SimpleStrat(efforts[i]))
        
        return strategies

    def getEfforts(self, size: int, initX: float, effort1: float, effort2: float) -> float:
        numE1: int = int(math.ceil(size * initX))

        # print(f"numE1: {numE1}, size: {size}")
        efforts = []

        for i in range(numE1):
            efforts.append(effort1)
        
        for i in range(numE1, size):
            efforts.append(effort2)

        shuffle(efforts)

        effortArray = []

        for i in range(size):
            effortArray.append(efforts[i])

        return effortArray