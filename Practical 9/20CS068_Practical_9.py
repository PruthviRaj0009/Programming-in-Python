'''
Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result.
The Student class has data members such as those representing rollNumber, Name, etc.
Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six subjects.
Derive Result from the Exam class, and it has its own fields such as total_marks.
Write an interactive program to model this relationship.
'''
# Pruthvi Raj
# 20CS068

# Creating a class Student.
class student:
    Name = ''
    Roll_no = 0

    # function to set the id & name
    def details(self, Roll_no, Name):
        self.Name = Name
        self.Roll_no = Roll_no


# Creating a class exam from class student.
class exam(student):
    marks_list = []

    # function marks to set the marks of that student.
    def marks(self, marks_list):
        self.marks_list = marks_list
        return marks_list


# Creating a class result from class exam.
class result(exam):
    marks_gain = 0

    # Function to obtain the total of the marks of a student.
    def result_of_student(self, marks_gain):
        total_marks = 0
        for item in marks_gain:
            total_marks += item
        return total_marks


# Creating an object of result class.
v = result()
student_name = input("Enter the name of the student : ")
student_id = input("Enter the Roll Number of the student : ")
subjects = int(input("Enter the no. of subjects: "))
marks = []

# Setting the details.
v.details(student_id, student_name)

print(f"Enter the marks of {student_name} in {subjects} subject : ")
for i in range(0, subjects):
    marks.append(int(input()))

# Setting the marks.
marks_obtain = v.marks(marks)
total = v.result_of_student(marks_obtain)
print(f"Total of {student_name} mark's is : {total}")
