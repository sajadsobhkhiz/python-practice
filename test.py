# tasks = ["Take a nap"]

# new_tasks = ["Go for a walk", "Read a book"]
# tasks.extend(new_tasks)
# print('Task extended: ', tasks)

# new_tasks = "do the dishes"
# tasks.append(new_tasks)
# print('Task appende: ', tasks)

# student = {
#     'name' : 'sajad',
#     'age' : 40,
#     'city' : 'vancouver',
#     'birthdate' : '1986-09-23'
# }


# print(student.keys())
# print(student.values())
# print(student.items())


# students_grade ={
#     'Alice' : 'A',
#     'Bob' : 'B+',
#     'Charlie' : 'C'
# }

# students ={
#     'stud1' : {'name':'Ali', 'courses' : ["Math", "Science", "History"]},
#     'stud2' : {'name':'Asghar', 'courses' : ['Math', 'Art']},
# }

# list = [ 3 ,5 , 'Math', 'Physics', 'Ali', True, 123, '123']

# list[2:5]=[12,3]
# list.extend("1234567")
# list.append("1234567")
# list.extend({1,3,4,56,7, False, 'a'})
# list.append({1,3,4,56,7, False, 'a'})
# a=list.pop()
# list.pop()
# print(a)

# print(list)
# print(list[:3])

# students = {
#     "STU1": {"name": "sajad", "id": "20261"},
#     "STU2": {"name": "ali", "id": "20262"},
#     "STU3": {"name": "reza", "id": "20263"}
# }

# print(students)
# students["STU4"] = {"name": "jim", "id": "20265"}
# print(students)

# list = [1,2,5,3,2,6,5,1,3]
# list_to_set = set(list)
# print(list_to_set)

# from collections import deque
# tasks = deque()
# tasks.append("Task 1")
# tasks.append("Task 2")
# tasks.append("Task 3")

# next_task_pop = tasks.pop()
# next_task_popleft = tasks.popleft()

# print(next_task_pop)
# print(next_task_popleft)

# print(list(tasks))
# list = [1,2,5,1,3,5,8]
# print(list.pop())
# list.clear()

# print(list)

# # from collections import Counter

# # def update_trends(incoming_hashtags):
# #     # Step 1: incoming_hashtags is a list
# #     # Step 2: remove duplicates (optional but useful)
# #     unique = set(incoming_hashtags)

# #     # Step 3: count popularity
# #     counts = Counter(incoming_hashtags)
# #     print (counts)
# #     # Step 4: sort by count (highest first)
# #     trending = sorted(counts.items(), key=lambda x: x[1], reverse=True)

# #     return trending

# data = ["#ai", "#coding", "#social", "#python","#ai", "#fun", "#python", "#coding", "#fun", "#python"]
# print(update_trends(data))

# import timeit

# list_data = list(range(9000000))
# dict_data = {i: i for i in range(9000000)}

# lookup_value = 12
# list_time = timeit.timeit(lambda: lookup_value in list_data, number=1000)
# dict_time = timeit.timeit(lambda: lookup_value in dict_data, number=1000)

# print("List lookup time:", list_time)
# print("Dictionary lookup time:", dict_time)





# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Error divided by zero")

# def calculate_area(length, width): 
#     if not isinstance(length, (int, float)) or not isinstance(width, (int, float)): 
#         return "You must insert only numbers!"
        
#     return length * width

# print(calculate_area(5, 8.5)) # TypeError: Length and width must be numbers.

# import logging

# my_dict = {"a": 1, "b": 2}
# try:
#     print(my_dict["c"])
# except KeyError as e:
#     logging.error(f"KeyError encountered: {e}")
#     # Handle the error or provide a fallback mechanism





# def get_city_population(populations, city):
#     try:
#         return populations[city]
#     except KeyError:
#         raise KeyError(f"City '{city}' not found in the dictionary.") from None

# city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

# print(get_city_population(city_populations, "New York"))


# def calculate_average(numbers):
#     print("Input numbers:", numbers)
#     total = sum(numbers)
#     print("Total:", total)
#     count = len(numbers)
#     print("Count:", count)
#     average = total / count
#     print("Average:", average)
#     return average

# calculate_average([10,20,30,50,80])


# def calculate_area(length, width):
#     assert length > 0, "Length must be positive"
#     assert width > 0, "Width must be positive"
#     return length * width

# L = int(input("Enter length: "))
# W = int(input("Enter width: "))
# print(calculate_area(L, W))






# Write your Python program below
def read_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("Error: File not found -", file_path)

read_file_contents("/Users/Example/Documents/my_file.txt")



