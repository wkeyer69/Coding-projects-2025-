

class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade 
        

    def show(self):
        return f"Student {self.name}, age {self.age}, grade {self.grade}"
    

class av_grade:
    def __init__(self, grade):
        self.grade = grade


    

class Course:
    def __init__(self, name, max_students):
        self.name = name 
        self.m_s = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) >= self.m_s:
            return False
        else:
            self.students.append(student)

    

s1 = student("Bill", 32, 92)

s2 = student("Paks", 15, 60)
course = Course("Science", 1)
course.add_students(s1)
course.add_students(s2)
print(Course.students)