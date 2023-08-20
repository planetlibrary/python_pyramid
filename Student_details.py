class Student:
    def __init__(self, name, reg_no, phy_mark, che_mark, mat_mark, bio_mark, gender):
        self.name = name
        self.reg_no = reg_no
        self.phy_mark = phy_mark
        self.che_mark = che_mark
        self.mat_mark = mat_mark
        self.bio_mark = bio_mark
        self.gender = gender
    
    def calculate_average_mark(self):
        return (self.phy_mark + self.che_mark + self.mat_mark + self.bio_mark) / 4
    
    def __str__(self):
        return f'{self.name},Registration Number: {self.reg_no} with an average score: {self.calculate_average_mark()}'
    
students = []
for i in range(5):
    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")
    phy_mark = int(input("Enter Physics marks: "))
    che_mark = int(input("Enter Chemistry marks: "))
    mat_mark = int(input("Enter Mathematics marks: "))
    bio_mark = int(input("Enter Biology marks: "))
    gender = input("Enter gender (M/F): ")
    students.append(Student(name, reg_no, phy_mark, che_mark, mat_mark, bio_mark, gender))

# Calculate average marks and find the topper
topper = None
for student in students:
    avg_mark = student.calculate_average_mark()
    print(student)
    if topper is None or avg_mark > topper.calculate_average_mark():
        topper = student

print(f"The topper among the students is: {topper}")
