class StudentDetails:
    numbers = {}

    def __init__(self, name, reg, phy, che, mat, bio, gender):
        self.name = name
        self.reg = reg
        self.phy = phy
        self.che = che
        self.mat = mat
        self.bio = bio
        self.gender = gender
        self.numbers = StudentDetails.numbers
        self.avg_marks = sum([self.phy, self.che, self.mat, self.bio])/4

        self.numbers[self.reg] = (self.avg_marks)

    def __str__(self):
        return f"{self.name}, {self.gender}, {self.reg} has the scored {self.phy} in Physics , {self.che} in Chemistry, {self.mat} in Mathematics and {self.bio} in Biology"

    @staticmethod
    def topper():
        max_num = max(StudentDetails.numbers.values())
        topper_list = [x for x in StudentDetails.numbers.keys()
                       if StudentDetails.numbers[x] == max_num]

        if len(topper_list) == 1:
            print(f"The reg. no of the topper is : {topper_list[0]}")
        else:
            print(f"The reg. no of the toppers are : ")
            for reg in topper_list:
                print(reg)


a1 = StudentDetails('Anjali', '234vd34', 90, 50, 45, 65, 'F')
a2 = StudentDetails('Shyam', '234vd33', 90, 50, 45, 65, 'M')
a3 = StudentDetails('Raju', '234vd35', 23, 45, 72, 56, 'M')
a4 = StudentDetails('Baburao', '234vd36', 45.7, 54, 23, 81, 'M')

print(a1)
print(a2)
print(a3)
print(a4)


StudentDetails.topper()
