#!usr/bin/env python

# dictionaries for the students data
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# composite functions to find averages

# standard find average function
def average(numbers):
  total = float(sum(numbers))
  return total / len(numbers)
  
# find average of each element of dictionary and weight averages accordingly
def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  
  return homework * 0.1 + quizzes * 0.3 + tests * 0.6

# get letter grade based on average 
def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80 and score < 90:
    return "B"
  elif score >= 70 and score < 80:
    return "C"
  elif score >= 60 and score < 70:
    return "D"
  else:
    return "F"
  
# print the letter grade results
print "Lloyd's Grade:", get_letter_grade(get_average(lloyd)), "\nAlice's Grade:", get_letter_grade(get_average(alice)), \
"\nTyler's Grade:", get_letter_grade(get_average(tyler))


# get class average by using for loop to get individual averages and append onto a list of averages. Then get the average of the list
def get_class_average(class_list):
  results = []
  
  for student in class_list:
    avg = get_average(student)
    results.append(avg)
  
  return average(results)

# make list of the students dictionaries to run the averaging functions on the class together
students = [lloyd, alice, tyler]

# present class results
print "Class avg grade:", get_class_average(students)

print "Class letter grade:", get_letter_grade(get_class_average(students))
