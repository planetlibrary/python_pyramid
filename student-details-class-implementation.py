# Define a class named StudentDetails
class StudentDetails:
    # Class-level dictionary to store registration numbers and their average marks
    numbers = {}

    # Constructor to initialize student details
    def __init__(self, name, reg, phy, che, mat, bio, gender):
        # Initialize instance variables with the provided values
        self.name = name
        self.reg = reg
        self.phy = phy
        self.che = che
        self.mat = mat
        self.bio = bio
        self.gender = gender
        # Link the instance's numbers dictionary to the class-level numbers dictionary
        self.numbers = StudentDetails.numbers
        # Calculate average marks
        self.avg_marks = sum([self.phy, self.che, self.mat, self.bio]) / 4
        # Store the average marks in the numbers dictionary using the registration number as key
        self.numbers[self.reg] = self.avg_marks

    # Method to provide a formatted string representation of the student details
    def __str__(self):
        return f"{self.name}, {self.gender}, {self.reg} has scored {self.phy} in Physics, {self.che} in Chemistry, {self.mat} in Mathematics, and {self.bio} in Biology"

    # Static method to find the topper(s) among the students
    @staticmethod
    def topper():
        # Find the maximum average marks from the numbers dictionary
        max_num = max(StudentDetails.numbers.values())
        # Create a list of registration numbers of students who scored the maximum average marks
        topper_list = [x for x in StudentDetails.numbers.keys()
                       if StudentDetails.numbers[x] == max_num]

        # Check if there's only one topper or multiple toppers
        if len(topper_list) == 1:
            print(f"The reg. no of the topper is: {topper_list[0]}")
        else:
            print(f"The reg. no of the toppers are:")
            # Print the registration numbers of all toppers
            for reg in topper_list:
                print(reg)

# Create instances of the StudentDetails class with student information
a1 = StudentDetails('Anjali', '234vd34', 90, 50, 45, 65, 'F')
a2 = StudentDetails('Shyam', '234vd33', 90, 50, 45, 65, 'M')
a3 = StudentDetails('Raju', '234vd35', 23, 45, 72, 56, 'M')
a4 = StudentDetails('Baburao', '234vd36', 45.7, 54, 23, 81, 'M')

# Print the details of the created students
print(a1)
print(a2)
print(a3)
print(a4)

# Call the topper method to find and print the topper(s)
StudentDetails.topper()
