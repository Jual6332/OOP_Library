# OOP_Library Project Description
An application for storing bookstore data, including customer-base, book catalog, and employee database. From a technology standpoint, written purely in Object-Oriented Python.

# Object-Oriented Approach to Development
This project relies heavily on encapsulation and abstraction. You'll notice the encapsulation technique of using getter and setter methods to modify private attributes in the various classes. 
Inheritance was also implemented in the code, such as when the bag class inherits from the StoreItem class.

# Other unique Features:
- Inventory tracking for items (using dictionaries)
- Customer rewards
- Customer leaderboard for rewards points (using dictionaries)
- Employee performance review tracking and leaderboard 

# Custom Classes: Book class.
Attributes:
1. Title - a string, title of the book
2. Author - a string, author of the book
3. Publication Year - an integer, publication year of the book 
4. Genre - a string, the genre of the book
5. Publisher - a string, the publisher for the book
6. Words - a string, the words of the book
7. Sale Cost - a double, the cost of the book

Setter Methods:
1. set_title() - Set title of the book. 1 string input param
2. set_author() - Set author of the book. 1 string input param
3. set_year() - Set year of the book. 1 integer input param
4. set_genre() - Set genre of the book. 1 string input param
5. set_publisher() - Set publisher of the book. 1 string input param
6. set_words() - Store the words of the book. 1 string input param
7. set_cost() - Set cost of the book. 1 double input param

Getter Methods:
1. get_title() - Return title of the book
2. get_author() - Return author of the book
3. get_year() - Return year of the book
4. get_genre() - Return genre of the book
5. get_publisher() - Return publisher of the book
6. get_words() - Return words of the book
7. get_cost() - Return cost of the book

# External Libraries
- import random
