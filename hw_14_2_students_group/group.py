from exceptions import GroupSizeLimitError

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