class GroupSizeLimitError(Exception):
    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender} {self.age} {self.first_name} {self.last_name}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender=gender, age=age, first_name=first_name, last_name=last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupSizeLimitError("There cannot be more than 10 students in a group.")
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        stud_del = self.find_student(last_name)
        if stud_del is not None:
            self.group.remove(stud_del)

    def find_student(self, last_name):
        for stud in self.group:
            if stud.last_name == last_name:
                return stud
        return None

    def __str__(self):
        all_students = ''
        for stud in self.group:
            all_students += f'{stud.first_name} {stud.last_name}\n'
        return f'Number:{self.number}\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN143')
st3 = Student('Male', 18, 'Oleg', 'Swift', 'AN144')
st4 = Student('Female', 26, 'Olya', 'Dor', 'AN145')
st5 = Student('Male', 19, 'Dima', 'Chan', 'AN146')
st6 = Student('Female', 29, 'Yulia', 'Han', 'AN147')
st7 = Student('Male', 25, 'Nikolas', 'Gol', 'AN148')
st8 = Student('Female', 23, 'Sveta', 'Peterson', 'AN149')
st9 = Student('Male', 21, 'Sergiy', 'Kiri', 'AN141')
st10 = Student('Female', 20, 'Anna', 'Trock', 'AN140')
st11 = Student('Male', 25, 'Pedro', 'Test', 'AN1444')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

try:
    gr.add_student(st11)
except GroupSizeLimitError as e:
    print(e)

print(gr)