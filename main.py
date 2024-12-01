#import matplotlib.pyplot as plt
import random

class Book():
  def __init__(self):
    self.title = ""
    self.author = ""
    self.year = 0
    self.genre = ""
    self.publisher = ""
    self.words = ""
    self.cost = 0
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
  def set_cost(self,cost):
    self.cost = cost
  def get_title(self):
    return self.title
  def get_author(self):
    return self.author
  def get_year(self):
    return self.year
  def get_genre(self):
    return self.genre
  def get_publisher(self):
    return self.publisher
  def get_words(self):
    return self.words
  def get_cost(self):
    return self.cost
  # Method: update_title()
  # Input Parameter 1: tle, a string for the new title
  # Purpose: to change title string value to a new string value. Similar methods: set_title() is only used for the first time the title value is set - update_title() is used on other occassions to set the string value of title
  def update_title(self,tle):
    self.title = tle
  # Method: update_year() 
  # Purpose: to change year number to new number value. Similar methods: set_year() is only used for the first time the year is set, update_year() is used on other occassions to set the number value of year
  def update_year(self,yr):
    self.year = yr

class StoreItem():
  def __init__(self):
    self.name = ""
    self.details = ""
    self.price = 0
  def set_name(self,name):
    self.name = name
  def set_details(self,details):
    self.details = details
  def set_price(self,price):
    self.price = price
  def get_name(self):
    return self.name
  def get_details(self):
    return self.details
  def get_price(self):
    return self.price

class Bag(StoreItem):
  def printBagDetails(self):
    print("Bag Name: " + self.name)
    print("Bag Details: " + self.details)
    print("Bag Price: " + str(self.price))

# Does Python allow for lists to have different object types in the same list? A string and a set to exist within a list. JavaScript does. C++ does not

class StoreItemDatabase():
  def __init__(self):
    self.items = []
  def add_item(self,item):
    self.items.append(item)
  def get_iems(self):
    return self.items
  def get_item(self,itemName):
    for item in self.items:
      if item.get_name() == itemName:
        return item
  def remove_item(self,item):
    self.items.remove(item)

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
    books = []
    for book in self.books:
      if book.get_genre() == genre:
        books.append(book)
    return books
  def sort_by_author(self,author):
    authors = []
    for book in self.books:
      if book.get_author() == author:
        authors.append(book)
    return authors
  def sort_by_year(self,year):
    books = []
    for book in self.books:
      if book.get_year() == year:
        books.append(book)
    return books

# Add Example Book Data
book1 = Book()
book1.set_title("The Great Gatsby")
book1.set_author("F. Scott Fitzgerald")
book1.set_year(1925)
book1.set_genre("Historical Fiction")
book1.set_publisher("Scribner Classics")
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
book3.set_publisher("Little, Brown and Company")
book3.set_words("...")

book4 = Book()
book4.set_title("Star Wars Episode 4: A New Hope")
book4.set_author("George Lucas")
book4.set_year(2011)
book4.set_genre("Fiction")
book4.set_publisher("Ballantine Books")
book4.set_words("...")

book5 = Book()
book5.set_title("The Complete Sherlock Holmes Volume II")
book5.set_author("Arthur Conan Doyle")
book5.set_year(2003)
book5.set_genre("Fiction")
book5.set_publisher("Barnes and Noble Inc.")
book5.set_words("...")

book6 = Book()
book6.set_title("Martian")
book6.set_author("Andy Weir")
book6.set_year(2020)
book6.set_genre("Fiction")
book6.set_publisher("Crown Publishing Group")
book6.set_words("...")

book7 = Book()
book7.set_title("Star Wars Episode 5: The Empire Strikes Back")
book7.set_author("George Lucas")
book7.set_year(1985)
book7.set_genre("Fiction")
book7.set_publisher("Random House Worlds")
book7.set_words("...")

## Add Example Library Data
# Create Library Object
lib = Library()
lib.set_name("Library 1")
lib.set_year(1975)

# Add Books to Library Class
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)
lib.add_book(book5)
lib.add_book(book6)
lib.add_book(book7)
lib_books = lib.get_books() # SHort-hand

# Add Authors to Library
for book in lib_books:
  lib.add_author(book.author)
lib_authors = lib.get_authors()

# Add other store items
bag1 = Bag()
bag1.set_name("Bag 1")
bag1.set_details("Brown leather bag with zippers. Worn. A few years old.")
bag1.set_price(12)

# Add Store Items to StoreItemDatabase
si_db = StoreItemDatabase()
si_db.add_item(bag1)

## Define Employee Class
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
  def get_performance_grades(self):
    return self.performance_grades
  def get_performance_comments(self):
    return self.performance_comments

## Create Employee Database
# A storage class for sensitive employee information
class EmployeeDatabase():
  def __init__(self):
    self.employees = []
    self.raise_history = []
  def add_employee(self,employee):
    self.employees.append(employee)
  def get_employees(self):
    return self.employees
  # Replacing total salary or adding only the difference which wuld be the raise amount per year
  def add_raise_data(self,raise_new):
      self.raise_history.append(raise_new)
  def get_raise_data(self):
    return self.raise_history

## Add Employees to the Project
emp1 = Employee()
emp1.set_id(1)
emp1.set_name("Employee One")
emp1.set_age(50)
emp1.set_job_title("Manager")
emp1.set_salary(72000)

emp2 = Employee()
emp2.set_id(2)
emp2.set_name("Employee Two")
emp2.set_age(45)
emp2.set_job_title("Supervisor")
emp2.set_salary(54000)

emp3 = Employee()
emp3.set_id(3)
emp3.set_name("Employee Three")
emp3.set_age(42)
emp3.set_job_title("Supervisor")
emp3.set_salary(48000)

emp4 = Employee()
emp4.set_id(4)
emp4.set_name("Employee Four")
emp4.set_age(33)
emp4.set_job_title("Cashier")
emp4.set_salary(40000)

emp5 = Employee()
emp5.set_id(5)
emp5.set_name("Employee Five")
emp5.set_age(40)
emp5.set_job_title("Cashier")
emp5.set_salary(39000)

emp6 = Employee()
emp6.set_id(6)
emp6.set_name("Employee Six")
emp6.set_age(29)
emp6.set_job_title("Cashier")
emp6.set_salary(31000)

emp7 = Employee()
emp7.set_id(7)
emp7.set_name("Employee Seven")
emp7.set_age(25)
emp7.set_job_title("Cashier")
emp7.set_salary(27000)

emp8 = Employee()
emp8.set_id(8)
emp8.set_name("Employee Eight")
emp8.set_age(55)
emp8.set_job_title("Manager")
emp8.set_salary(74000)

emp9 = Employee()
emp9.set_id(9)
emp9.set_name("Employee Nine")
emp9.set_age(28)
emp9.set_job_title("Bakery Cashier")
emp9.set_salary(30000)

emp10 = Employee()
emp10.set_id(10)
emp10.set_name("Employee Ten")
emp10.set_age(27)
emp10.set_job_title("Bakery Cashier")
emp10.set_salary(29000)

emp_db = EmployeeDatabase()
emp_db.add_employee(emp1)
emp_db.add_employee(emp2)
emp_db.add_employee(emp3)
emp_db.add_employee(emp4)
emp_db.add_employee(emp5)
emp_db.add_employee(emp6)
emp_db.add_employee(emp7)
emp_db.add_employee(emp8)
emp_db.add_employee(emp9)
emp_db.add_employee(emp10)
employees = emp_db.get_employees() # Store employee information objects in an easier-to-use variable

# Create Customer Class
class Customer():
  def __init__(self):
    self.name = ""
    self.age = 0
    self.rewards_number = ""
    self.previous_purchases = []
  def add_purchase(self,book,cost):
    self.previous_purchases.append("Bought {0} for ${1}.".format(book.title,cost))
  def set_name(self,name):
    self.name = name
  def set_age(self,age):
    self.age = age
  def set_rewards_number(self,rewards):
    self.rewards = rewards
  def get_name(self):
    return self.name
  def get_age(self):
    return self.age
  def get_rewards_number(self):
    return self.rewards
  def get_previous_purchases(self):
    return self.previous_purchases

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
cust1.set_rewards_number("0001")

cust2 = Customer()
cust2.set_name("Customer Two")
cust2.set_age(52)
cust2.set_rewards_number("xxxx")

cust3 = Customer()
cust3.set_name("Customer Three")
cust3.set_age(41)
cust3.set_rewards_number("0003")

cust4 = Customer()
cust4.set_name("Customer Four")
cust4.set_age(30)
cust4.set_rewards_number("xxxx")

cust5 = Customer()
cust5.set_name("Customer Five")
cust5.set_age(46)
cust5.set_rewards_number("0005")

cust6 = Customer()
cust6.set_name("Customer Six")
cust6.set_age(18)
cust6.set_rewards_number("0006")

cust7 = Customer()
cust7.set_name("Customer Seven")
cust7.set_age(21)
cust7.set_rewards_number("0007")

cust8 = Customer()
cust8.set_name("Customer Eight")
cust8.set_age(32)
cust8.set_rewards_number("xxxx")

cust9 = Customer()
cust9.set_name("Customer Nine")
cust9.set_age(42)
cust9.set_rewards_number("xxxx")

cust10 = Customer()
cust10.set_name("Customer Ten")
cust10.set_age(27)
cust10.set_rewards_number("0010")

cust_db = CustomerDatabase()
cust_db.add_customer(cust1)
cust_db.add_customer(cust2)
cust_db.add_customer(cust3)
cust_db.add_customer(cust4)
cust_db.add_customer(cust5)
cust_db.add_customer(cust6)
cust_db.add_customer(cust7)
cust_db.add_customer(cust8)
cust_db.add_customer(cust9)
cust_db.add_customer(cust10)
cust_db.sort_customers_lname()
customers = cust_db.get_customers()

# ======== Continued Development ======== #
# I would like to give a performance review (first employee)
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

# I would like to give a performance review (second employee)
employee_review2 = emp5.get_name() # Employee under review
selling_credit_cards_grade = "C" # How well did he/she sell credit cards?
punctuality_grade = "B" # How punctual was he/she?
customer_service_grade = "C" # How was their customer service rating?
emp5.performance_grades.append(selling_credit_cards_grade+" "+punctuality_grade+" "+customer_service_grade) # Add strings

comments = "This employee did join the cashier squad 4 months ago. Her last experience as a cashier did not carry over. There is no excuses for her bad performance. She has C grades in selling credit cards and customer service. She is on-time at least 80% of the time, which grants her a B grade for punctuality. She will be let-go during next round of budget cuts." # Manager/supervisor comments
emp5.performance_comments.append(comments) # Store comments

# Print Output
print(employee_review2)
print(emp5.performance_grades)
print(emp5.performance_comments)
print("\n")

# Write function to determine if person gets a raise next based on performance review scores

# ======== Continued Development ======== #
# Cost of a book depends on the book
def cost_of_specific_book(bought_book):
  cost = 0.00
  if bought_book == "The Great Gatsby":
    cost = 22.50
  elif bought_book == "Forty Chances":
    cost = 25.00
  elif bought_book == "Along Came a Spider":
    cost = 15.00
  elif bought_book == "Star Wars Episode 4: A New Hope":
    cost = 17.50
  elif bought_book == "Star Wars Episode 5: The Empire Strikes Back":
    cost = 7.95
  elif bought_book == "Martian":
    cost = 9.99
  elif bought_book == "The Complete Sherlock Holmes Volume II":
    cost = 9.97
  elif bought_book == "Star Wars Episode 5: The Empire Strikes Back":
    cost = 9.99
  return cost
  
# Make a purchase - Write to a file
def make_purchase(cust,lib_books,cash,emp):
  file = open("transactions.txt", "w") 
  file.write("TRANSACTION.\n")
  file.write("{0} enters checkout aisle to purchase a book.\n".format(cust.get_name()))
  pick_random_book = random.choice(lib_books)
  bought_book = pick_random_book.get_title()
  cost = cost_of_specific_book(bought_book)
  employee = emp.get_name();
  file.write(employee+" helps customer with purchase.\n")
  total_cost = 0
  if cust.rewards != "xxxx":
    # 10% discount applies
    total_cost = cash-cost*0.90
  else:
    # Discount does not apply
    total_cost = cash-cost
  file.write("The customer has ${0} in cash.\n".format(cash))
  file.write("The book costs ${0}\n".format(cost))
  file.write("Customer2 purchases {0} with ${1} remaining.\n".format(bought_book,total_cost))
  file.close()

# ======== Continued Development ======== #
# Organized genres into a list
# Bug Fixed: The number of books for Histrocial fiction, non-fiction, and fiction were incorrect but that's fixed
# 2/2/24 Justin
genres = []
for book in lib_books:
  genres.append(book.get_genre())
  print(book.get_genre())
print(genres)

# Old code - Broken, deprecated at this point
#for index in range(0,len(genres)):
#  chosen_genre = genres[index]
#  numBooksInThisGenre = 0
#  for genre in genres[index:len(genres)]:
#    if genre == chosen_genre:
#      print("Index: "+str(index))
#      print("Genre: "+genre)
#      print("Chosen genre: "+chosen_genre)
#      numBooksInThisGenre+=1
#      print("Number of Books in this Genre: "+str(numBooksInThisGenre))
  #print("Chosen Genre {0} has {1} duplicates in the library of books.".format(chosen_genre,duplicates))
#genres_books[chosen_genre] = numBooksInThisGenre

# Key on genre, value is how mnay times that author appears in library
genres_dictionary = {}

# Store genre of books, count how many books per genre
for genre in genres:
  if (genre in genres_dictionary): # If the genre is already in the dictionary, increment the number of occurrences of this genre 
    genres_dictionary[genre] += 1
  else:
    genres_dictionary[genre] = 1

# ======== Continued Development ======== # 
# Key on author, value is how mnay times that author appears in library 
authors_dictionary = {};

for author in lib_authors:
  if (author in authors_dictionary): # If the author is already in the dictionary, increment the number of occurrences of this author
    authors_dictionary[author] += 1
  else:
    authors_dictionary[author] = 1

# ======== Continued Development ======== #
# See how many of each employees have each job
job_titles = []
for employee in employees:
  job_titles.append(employee.get_job_title())
  print(employee.get_job_title())
print(job_titles)

job_titles_dict = {}
job_titles_dict["Manager"] = job_titles.count("Manager")
job_titles_dict["Supervisor"] = job_titles.count("Supervisor")
job_titles_dict["Cashier"] = job_titles.count("Cashier")
job_titles_dict["Bakery Cashier"] = job_titles.count("Bakery Cashier")

print(job_titles_dict)
print("\n")
  
# ======== Testing ======== #
# Print the Name of Each Book
print("Books in Library:")
for book in lib_books:
  print(book.get_title())
print("\n")

# Print the Name of Each Author
print("Authors in Library:")
for author in lib_authors:
  print(author)
print("\n")

# Print the Name of Each Employee
print("Employees at Bookstore:")
for employee in employees:
  print(employee.get_name())
print("\n")

# Print the Name of Each Employee
print("Previous Customers:")
for customer in customers:
  print(customer.get_name())
print("\n")

# Print the Number of times each  shows up in the library
# There was a Bug here. Found 2/4/24, fixed 2/4/24, documented 11/16/24,  - Justin
print(genres_dictionary)
print("\n")

# Print the Number of times each author shows up in the library
print(authors_dictionary)
print("\n")

# ======== Testing ======== #
# Unit Tests for finding a customer in the customer database
# Unit Tests for using cust_db.find_customer() method
customer_example1 = "Customer One"
customer_example2 = "Customer Two"
customer_example3 = "Customer Three"
customer_exampleF = "Fake Customer"
customer_example4 = "Customer Four"
customer_example5 = "Customer Five"
customer_example6 = "Customer Six"
customer_example7 = "Customer Seven"

# If Customer name is in the list of usual customers, then the customer is "found" by our database
def find_customer_by_name_unittest(customer_example):
  found_customer = cust_db.find_customer_by_name(customer_example)
  if found_customer is None:
    print("Failure.")
    print(customer_example + " was not found.")
  else:
    print("Success!")
    print(customer_example + " was found!")

# Unit Test 1
print("Test1 for cust_db.find_customer_by_name():")
find_customer_by_name_unittest(customer_example1)

# Unit Test 2
print("Test2 for cust_db.find_customer_by_name():")
find_customer_by_name_unittest(customer_example2)

# Unit Test 3
print("Test3 for cust_db.find_customer_by_name():")
find_customer_by_name_unittest(customer_example3)

# Unit Test 4
print("Test4 for cust_db.find_customer_by_name():")
find_customer_by_name_unittest(customer_exampleF)

print("Test5 for cust_db.find_customer_by_name():")
find_customer_by_name_unittest(customer_example4)

print("Test6 for cust_db.find_customer_by_name():")
find_customer_by_name_unittest(customer_example5)

print("Test7 for cust_db.find_customer_by_name():")
find_customer_by_name_unittest(customer_example6)

print("Test8 for cust_db.find_customer_by_name():")
find_customer_by_name_unittest(customer_example7)

print("\n")

# ======== Testing ======== #
# Unit Test for finding a book in the library
# Unit Tests for using lib.find_book() method
book_example1 = "The Great Gatsby"
book_example2 = "Forty Chances"
book_example3 = "..."
book_example4 = "Along Came a Spider"
book_example5 = "Star Wars Episode 4: A New Hope"
book_example6 = "Star Wars Episode 5: The Empire Strikes Back"
book_example7 = "Martian"
book_example8 = "The Complete Sherlock Holmes Volume II"

# If the book name is in the list of books in the database, then the book requested is "found" by our database
def find_book_by_name_unittest(book_example):
  found_book = lib.find_book(book_example)
  if found_book is None:
    print("Failure.")
    print(book_example + " was not found.")
  else:
    print("Success!")
    print(book_example + " was found!")

# Unit Test 1
print("Test1 for lib.find_book():")
find_book_by_name_unittest(book_example1)

# Unit Test 2
print("Test2 for lib.find_book():")
find_book_by_name_unittest(book_example2)

# Unit Test 3
print("Test3 for lib.find_book():")
find_book_by_name_unittest(book_example3)

# Unit Test 4
print("Test4 for lib.find_book():")
find_book_by_name_unittest(book_example4)

# Unit Test 5
print("Test5 for lib.find_book():")
find_book_by_name_unittest(book_example5)

# Unit Test 6
print("Test6 for lib.find_book():")
find_book_by_name_unittest(book_example6)

# Unit Test 7
print("Test7 for lib.find_book():")
find_book_by_name_unittest(book_example7)

# Unit Test 8
print("Test8 for lib.find_book():")
find_book_by_name_unittest(book_example8)

# ======== Plotting ======== #
name_data = []; salary_data = [];
for employee in employees:
  salary = employee.get_salary()
  name = employee.get_name()
  name_data.append(name)
  salary_data.append(salary)

#plt.bar([1,2,3],salary_data[0:3])
#plt.bar(name_data[0:5],salary_data[0:5])
#plt.show

# Unit Test for Transactions
make_purchase(cust1,lib_books,50.00,emp4)
make_purchase(cust2,lib_books,40.00,emp4)
make_purchase(cust3,lib_books,30.00,emp4)

# 1.)  Unit Test for sort_by_genre() method for Library class
print("\n")
print("Test 1 for lib.sort_by_genre()")
fiction_books = lib.sort_by_genre("Fiction")
if fiction_books is None:
  print("No Fiction books in the library.")
else:
  for book in fiction_books:
    print(book.get_title())
print("\n")

# 1.)  Unit Test for sort_by_author() method for Library class
print("Test 1 for lib.sort_by_author()")
authored_books = lib.sort_by_author("James Patterson")
if authored_books is None:
  print("No books by James Patterson.")
else:
  for book in authored_books:
    print(book.get_title())
print("\n")

# 1.) Unit Test for sort_by_year() method for Library class
print("Test 1 for lib.sort_by_year()")
old_books = lib.sort_by_year(1925)
if old_books is None:
  print("No books for the year {0}.".format(1925))
else:
  for book in old_books:
    print(book.get_title())
print("\n")

# Todos:
# Data
# 1. 

# Supervisor has different duties, like setting hours and delegating. Needs to have a working relationship with the cashiers

# The book array needs to check for repeats somehow. 

# Add database for "other items" like satchel, backpack, clickers, flashdrives that can be sold
# Database exists but needs some work - Justin 11/24/24



