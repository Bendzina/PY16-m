# დავალება 1.

# შეიმუშავეთ საბანკო ანგარიშის ძირითადი სისტემა. შექმენით კლასი სახელწოდებით BankAccount, 
# ისეთი ატრიბუტებით, როგორიცაა account_number, account_holder და balance. აღწერეთ ფულის 
# ჩარიცხვის და გამოტანის მეთოდები. შექმენით რამდენიმე ობიექტი და განახორციელეთ რამდენიმე ტრანზაქცია.

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}."
        return "Deposit amount must be positive."
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}."
            return "Insufficient funds."
        return "Withdrawal amount must be positive."
    
    def display_balance(self):
        return f"Account balance for {self.account_holder}: ${self.balance:.2f}"
    
    def __repr__(self):
        return f"BankAccount(account_number='{self.account_number}', account_holder='{self.account_holder}', balance={self.balance:.2f})"


account1 = BankAccount("123456789", "John Doe", 500.0)
account2 = BankAccount("987654321", "Jane Smith", 1000.0)


print(account1.deposit(150.0))
print(account1.withdraw(50.0))
print(account1.display_balance())

print(account2.deposit(300.0))
print(account2.withdraw(1500.0))  
print(account2.display_balance())


# დავალება 2.

# შექმენით კლასი სახელწოდებით Student ატრიბუტებით, როგორიცაა name, student_id და 
# courses(კურსების სია, რომელშიც სტუდენტი არის ჩარიცხული). აღწერეთ სტუდენტის ინფორმაციის და 
# კურსების ჩვენების მეთოდები. შექმენით რამდენიმე ობიექტი და დაარეგისტრირეთ სხვადასხვა კურსებზე.

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
    
    def register_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            return f"{self.name} has been registered for the course: {course}."
        return f"{self.name} is already registered for the course: {course}."
    
    def display_info(self):
        course_list = ", ".join(self.courses) if self.courses else "No courses registered."
        return f"Student Name: {self.name}\nStudent ID: {self.student_id}\nCourses: {course_list}"
    
    def __repr__(self):
        return f"Student(name='{self.name}', student_id='{self.student_id}', courses={self.courses})"


student1 = Student("Alice Johnson", "S001")
student2 = Student("Bob Smith", "S002")

print(student1.register_course("Math"))
print(student1.register_course("Physics"))
print(student1.register_course("Math"))  

print(student2.register_course("Chemistry"))
print(student2.register_course("Biology"))

print("\nStudent 1 Info:")
print(student1.display_info())

print("\nStudent 2 Info:")
print(student2.display_info())
