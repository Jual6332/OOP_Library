import matplotlib.pyplot as plt
import random

class Book():
  def __init__(self):
    self.title = ""
    self.author = ""
    self.year = 0
    self.genre = ""
    self.publisher = ""
    self.words = ""
  def set_title(self,title):
    self.title = title
  def set_author(self,author):
    self.author = author
  def set_year(self,year):
    self.year = year
  def set_genre(self,genre):
    self.genre = genre
  def set_publisher(self,publisher):
    self.publisher = publisher
  def set_words(self,words):
    self.words = words
  def get_title(self):
    return self.title
  def get_author(self):
    return self.author
  def get_year(self):
    return self.year
  def get_genre(self):
    self.genre = genre
  def get_publisher(self):
    return self.publisher
  def get_words(self):
    return self.words

class Library():
  def __init__(self):
    self.name = "" 
    self.year = 0
    self.authors = []
    self.books = []
  def add_author(self,author):
    self.authors.append(author)
  def add_book(self,book):
    self.books.append(book)
  def get_name(self):
    return self.name
  def get_year(self):
    return self.year
  def get_authors(self):
    return self.authors
  def get_books(self):
    return self.books
  def set_name(self,name):
    self.name = name
  def set_year(self,year):
    self.year = year
  def find_book(self,title):
    for book in self.books:
      if book.get_title() == title:
        return book
    return None
  def sort_by_genre(self,genre):
    sorted_books_genre = []
    for book in self.books:
      if book.get_genre() is genre:
        sorted_books_genre.append(book)
    return sorted_books_genre

# Add Example Book Data
book1 = Book()
book1.set_title("The Great Gatsby")
book1.set_author("F. Scott Fitzgerald")
book1.set_year(1925)
book1.set_genre("Historical Fiction")
book1.set_publisher("...")
book1.set_words("...")

book2 = Book()
book2.set_title("Forty Chances")
book2.set_author("Howard G. Buffett")
book2.set_year(2013)
book2.set_genre("Non-fiction")
book2.set_publisher("...")
book2.set_words("...")

book3 = Book()
book3.set_title("Along Came a Spider")
book3.set_author("James Patterson")
book3.set_year(1993)
book3.set_genre("Fiction")
book3.set_publisher("...")
book3.set_words("...")

book4 = Book()
book4.set_title("Star Wars Episode 4: A New Hope")
book4.set_author("George Lucas")
book4.set_year(2011)
book4.set_genre("Fiction")
book4.set_publisher("...")
book4.set_words("...")

# Add Example Library Data
lib = Library()
lib.set_name("Library 1")
lib.set_year(1975)

lib.add_author("F. Scott Fitzgerald")
lib.add_author("Howard G. Buffett")
lib.add_author("James Patterson")
lib.add_author("George Lucas")
lib_authors = lib.get_authors()

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)
lib_books = lib.get_books()

# Define Employee Class
class Employee():
  def __init__(self):
    self.id = 0
    self.name = ""
    self.age = 0
    self.job_title = ""
    self.salary = 0
    self.start_date = ""
    self.performance_grades = []
    self.performance_comments = []
  def set_id(self,id):
    self.id = id
  def set_name(self,name):
    self.name = name
  def set_age(self,age):
    self.age = age
  def set_job_title(self,job_title):
    self.job_title = job_title
  def set_salary(self,salary):
    self.salary = salary
  def set_start_date(self,start_date):
    self.start_date = start_date
  
  def get_id(self):
    return self.id
  def get_name(self):
    return self.name
  def get_age(self):
    return self.age
  def get_job_title(self):
    return self.job_title
  def get_salary(self):
    return self.salary
  def get_start_date(self):
    return self.start_date

# Create Employee Database
# A storage class for sensitive employee information
class EmployeeDatabase():
  def __init__(self):
    self.employees = []
    self.raise_history = []
  def add_employee(self,employee):
    self.employees.append(employee)
  def get_employees(self):
    return self.employees
  def add_raise_data(self,raise_new):
      self.raise_history.append(raise_new)

# Add Employees to the Project
emp1 = Employee()
emp1.set_id(1)
emp1.set_name("Employee One")
emp1.set_age(45)
emp1.set_job_title("Manager")
emp1.set_salary(72000)

emp2 = Employee()
emp1.set_id(2)
emp2.set_name("Employee Two")
emp2.set_age(35)
emp2.set_job_title("Supervisor")
emp2.set_salary(54000)

emp3 = Employee()
emp1.set_id(3)
emp3.set_name("Employee Three")
emp3.set_age(42)
emp3.set_job_title("Supervisor")
emp3.set_salary(48000)

emp4 = Employee()
emp1.set_id(4)
emp4.set_name("Employee Four")
emp4.set_age(33)
emp4.set_job_title("Cashier")
emp4.set_salary(36000)

emp5 = Employee()
emp1.set_id(5)
emp5.set_name("Employee Five")
emp5.set_age(40)
emp5.set_job_title("Cashier")
emp5.set_salary(30000)

emp6 = Employee()
emp1.set_id(6)
emp6.set_name("Employee Six")
emp6.set_age(29)
emp6.set_job_title("Cashier")
emp4.set_salary(31000)

emp7 = Employee()
emp1.set_id(7)
emp7.set_name("Employee Seven")
emp7.set_age(25)
emp7.set_job_title("Cashier")
emp4.set_salary(27000)

emp_db = EmployeeDatabase()
emp_db.add_employee(emp1)
emp_db.add_employee(emp2)
emp_db.add_employee(emp3)
emp_db.add_employee(emp4)
emp_db.add_employee(emp5)
emp_db.add_employee(emp6)
emp_db.add_employee(emp7)
employees = emp_db.get_employees() # Store employee information objects in an easier-to-use variable

class Customer():
  def __init__(self):
    self.name = ""
    self.age = 0
    self.rewards = ""
  def set_name(self,name):
    self.name = name
  def set_age(self,age):
    self.age = age
  def set_rewards(self,rewards):
    self.rewards = rewards
  def get_name(self):
    return self.name
  def get_age(self):
    return self.age
  def get_rewards_number(self):
    return self.rewards

class CustomerDatabase():
  def __init__(self):
    self.customers = []
    self.customer_names = []
  def add_customer(self,customer):
    self.customers.append(customer)
  def get_customers(self):
    return self.customers
  def find_customer_by_name(self,name):
    for customer in self.customers:
      if customer.get_name() == name:
        return customer
    return None
  def sort_customers_lname(self):
    customers_names_reversed = []
    for customer in self.customers:
      [fname,lname] = customer.get_name().split(" ")
      name_reversed = lname + " " + fname
      customers_names_reversed.append(name_reversed)
    customers_sorted = sorted(customers_names_reversed)
    customers_sorted_rearranged = []
    for customer in customers_sorted:
      [lname,fname] = customer.split(" ")
      name = fname + " " + lname
      customers_sorted_rearranged.append(name)
    self.customers_names = customers_sorted_rearranged

# Data Input: Customer Data
cust1 = Customer()
cust1.set_name("Customer One")
cust1.set_age(34)
cust1.set_rewards("0001")

cust2 = Customer()
cust2.set_name("Customer Two")
cust2.set_age(52)
cust2.set_rewards("0002")

cust3 = Customer()
cust3.set_name("Customer Three")
cust3.set_age(41)
cust3.set_rewards("0003")

cust4 = Customer()
cust4.set_name("Customer Four")
cust4.set_age(30)
cust4.set_rewards("0004")

cust5 = Customer()
cust5.set_name("Customer Five")
cust5.set_age(46)
cust5.set_rewards("0004")

cust_db = CustomerDatabase()
cust_db.add_customer(cust1)
cust_db.add_customer(cust2)
cust_db.add_customer(cust3)
cust_db.add_customer(cust4)
cust_db.add_customer(cust5)
cust_db.sort_customers_lname()
customers = cust_db.get_customers()

# ======== Continued Development ======== #
# I would like to give a performance review (1/2 employees)
employee_review1 = emp4.get_name() # Employee under review
selling_credit_cards_grade = "A" # How well did he/she sell credit cards?
punctuality_grade = "A" # How punctual was he/she?
customer_service_grade = "B" # How was their customer service rating?
emp4.performance_grades.append(selling_credit_cards_grade+" "+punctuality_grade+" "+customer_service_grade) # Add strings

comments = "This employee is great at selling credit cards. She is never late for work. Loved by her manager. Sold 15 credit cards in the last month. Gives reliable advice to other cashiers. A great choice for a supervisor role soon. May get a raise." # Manager/supervisor comments
emp4.performance_comments.append(comments) # Store comments 

# Print Output
print(employee_review1)
print(emp4.performance_grades)
print(emp4.performance_comments)
print("\n")

# I would like to give a performance review (2/2 employees)
employee_review2 = emp5.get_name() # Employee under review
selling_credit_cards_grade = "C" # How well did he/she sell credit cards?
punctuality_grade = "B" # How punctual was he/she?
customer_service_grade = "C" # How was their customer service rating?
emp5.performance_grades.append(selling_credit_cards_grade+" "+punctuality_grade+" "+customer_service_grade) # Add strings

comments = "This employee did join the cashier squad two months ago. Her last experience as a cashier did not carry over. There is no excuses for her bad performance. She has C grades in selling credit cards and customer service. She is on-time at least 80% of the time, which grants her a B grade for punctuality. She will be let-go during next round of budget cuts." # Manager/supervisor comments
emp5.performance_comments.append(comments) # Store comments

# Print Output
print(employee_review2)
print(emp5.performance_grades)
print(emp5.performance_comments)
print("\n")

# ======== Continued Development ======== #
# Make a purchase
print("TRANSACTION.")
print("cust1 enters to purchase a book.")
pick_random_book = random.choice(lib_books)
bought_book1 = pick_random_book.get_title()
#print(bought_book1)
cash = 50.00
cost = 0.00

if bought_book1 == "The Great Gatsby":
  cost = 22.50
elif bought_book1 == "Forty Chances":
  cost = 25.00
elif bought_book1 == "Along Came a Spider":
  cost = 15.00
elif bought_book1 == "Star Wars Episode 4: A New Hope":
  cost = 17.50

print("The customer has ${0} in cash.".format(cash))
print("The book costs ${0}".format(cost))
print("Customer1 purchases {0} with ${1} remaining.".format(bought_book1,cash-cost))
print("\n")

## Write to file the books purchased from each transaction



# Write function to determine if person gets a raise next based on performance review scores

# ======== Testing ======== #
# Print the Name of Each Book
print("Books:")
for book in lib_books:
  print(book.get_title())
print("\n")

# Print the Name of Each Employee
print("Employees:")
for employee in employees:
  print(employee.get_name())
print("\n")

# Print the Name of Each Employee
print("Customers:")
for customer in customers:
  print(customer.get_name())
print("\n")

# Unit Test for finding a customer in the customer database
# Unit Test for using cust_db.find_customer() method
customer_example1 = "Customer One"
customer_example2 = "Customer Two"
customer_example3 = "Customer Three"
customer_exampleF = "Fake Customer"
found_customer1 = cust_db.find_customer_by_name(customer_example1)
found_customer2 = cust_db.find_customer_by_name(customer_example2)
found_customer3 = cust_db.find_customer_by_name(customer_example3)
found_customerF = cust_db.find_customer_by_name(customer_exampleF)
print("Test1 for cust_db.find_customer_by_name():")
if found_customer1 is None:
  print("Failure.")
  print(customer_example1 + " was not found.")
else:
  print("Success!")
  print(customer_example1 + " was found!")
print("\n")

print("Test2 for cust_db.find_customer_by_name():")
if found_customer2 is None:
  print("Failure.")
  print(customer_example2 + " was not found.")
else:
  print("Success!")
  print(customer_example2 + " was found!")
print("\n")

print("Test3 for cust_db.find_customer_by_name():")
if found_customer3 is None:
  print("Failure.")
  print(customer_example3 + " was not found.")
else:
  print("Success!")
  print(customer_example3 + " was found!")
print("\n")

print("TestF for cust_db.find_customer_by_name():")
if found_customerF is None:
  print("Failure.")
  print(customer_exampleF + " was not found.")
else:
  print("Success!")
  print(customer_exampleF + " was found!")
print("\n")

# Unit Test for finding a book in the library
# Unit Tests for using lib.find_book() method
book_example1 = "The Great Gatsby"
book_example2 = "Forty Chances"
book_example3 = "..."
book_example4 = "Along Came a Spider"
book_example5 = "Star Wars Episode 4: A New Hope"
found_book = lib.find_book(book_example1)
found_book2 = lib.find_book(book_example2)
found_book3 = lib.find_book(book_example3)
found_book4 = lib.find_book(book_example4)
found_book5 = lib.find_book(book_example5)

print("Test1 for lib.find_book():")
if found_book is None:
  print("Failure.")
  print(book_example1 + " was not found.")
else:
  print("Success!")
  print(book_example1 + " was found!")

print("Test2 for lib.find_book():")
if found_book2 is None:
  print("Failure.")
  print(book_example2 + " was not found.")
else:
  print("Success!")
  print(book_example2 + " was found!")

print("Test3 for lib.find_book():")
if found_book3 is None:
  print(book_example3 + " was not found.")
else:
  print("Success!")
  print(book_example3 + " was found!")

print("Test4 for lib.find_book():")
if found_book4 is None:
  print("Failure.")
  print(book_example4 + " was not found.")
else:
  print("Success!")
  print(book_example4 + " was found!")
#print("\n")

print("Test5 for lib.find_book():")
if found_book5 is None:
  print("Failure.")
  print(book_example5 + " was not found.")
else:
  print("Success!")
  print(book_example5 + " was found!")
print("\n")

# ======== Plotting ======== #
name_data = []; salary_data = [];
for employee in employees:
  salary = employee.get_salary()
  name = employee.get_name()
  name_data.append(name)
  salary_data.append(salary)

#plt.bar([1,2,3],salary_data[0:3])
#plt.bar(name_data[0:5],salary_data[0:5])
#plt.show()

# Todos:
# 1.) Write set_salary() and give_bonus() methods for Employee/EmployeeDB classes
#     - Bonuses will be based on a few factors. 
#     - Can a cashier give themselves a bonus? No. Obviously not. 
# Let's make a check for this

# 2.) Write test for sort by genre method for library class
# 3.) Add book sorting method for Library 
# 4.) find_customer() method in customer database
# 5.) More advanced unit testing

# Data
# 1. Add more customers to the customers list