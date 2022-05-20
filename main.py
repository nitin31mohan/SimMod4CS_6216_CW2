from typing import List
import sys

from classroom import Classroom
from group import Group
from params import Params
from simpleStrat import SimpleStrat
from factory import Factory


class Main:

    def run(self, numCourses: int):
        
        self.prms = Params()
        self.fctry = Factory()
        self.classroom = self.fctry.generateSimpleClass(size=self.prms.numGroups * self.prms.groupSize, 
                                                        initX=self.prms.initX, 
                                                        effort1=self.prms.H, 
                                                        effort2=self.prms.L)

        for i in range(numCourses):
            self.groups = self.fctry.makeGroups(self.classroom.students, 
                                                self.prms.groupSize)
            self.assignMarks(self.groups)

            H = SimpleStrat(self.prms.H)
            L = SimpleStrat(self.prms.L)

            self.classroom.updateStrategies()


    def assignMarks(self, groups: List[Group]):

        for i in range(len(groups)):
            print(f"For Group {i+1},")
            self.effort = groups[i].getEffort()
            self.groupSize = len(groups[i].students)
            self.marks = self.effort/self.groupSize
            self.groups[i].assignMarks(self.marks)


    def main(self):
        sys.stdout = open("log.txt", "w")
        xs = []
        for i in range(1, 5):
            print(f"Year {i},")
            for j in range(0, 2):
                self.run(i)
                S = SimpleStrat(self.prms.H)
                x = self.classroom.getConcentration(S)
                xs.append(x)

        sys.stdout.close()


if __name__ == "__main__":
    Main().main()