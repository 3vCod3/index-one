# 1. Variable and Data types
name = "Ever Hernandez"
age = 37
ai_course = True

print("Name:", name)
print("Age in 5 years:", age + 5)
print("Is enrolled in CS 335 course?" , ai_course)

# 2. List and Loops
topics = ["Logic", "Search", "NLP", "ML", "Bayesian Inference", "Perception", "Natural Interaction"]
print ("We will study:")
for i, topic in enumerate(topics, start=1):
  print(f"{i}.{topic}")

# 3.Dictionaries and Conditionals
student = {"name": "Ever" , "score": 98 }

if student["score"] >= 95:
  grade = "A+"
elif student["score"] >= 90:
  grade = "A"
elif student ["score"] >= 80:
  grade = "B"
else:
  grade = "C or below"

print(f"{student['name']} received a grade of {grade}.")

# 4.Functions
def greet_student(name):
  return f"Welcome to class, {name}!"
#Test
print(greet_student(name))

def square_number(num):
  return f"The square of {num} is {num ** 2}."
#Test
print(square_number(5))
print(square_number(20))
print(square_number(10))
