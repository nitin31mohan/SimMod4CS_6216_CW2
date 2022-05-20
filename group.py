from student import Student 

class Group:
    def __init__(self, students: list()):
    # def __init__(self, students: list(Student)):
        self.students = students

    def getEffort(self):
        effort = 0
        for i in range(len(self.students)):
            effort+=self.students[i].getEffort()
        
        return effort

    def assignMarks(self, marks: float):
        for i in range(len(self.students)):
            self.students[i].assignMarks(marks)

        print(f"\tAssigning {round(marks, 2)} marks to all students in group.")