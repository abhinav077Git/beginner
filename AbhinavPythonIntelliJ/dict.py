problem_dictionary={
    "Name":"Abhinav",
    "Age": 32,
    "Occupation": "IT Sector",
    "Sex":"Male"
}

# print(problem_dictionary)
# print(problem_dictionary["Name"])
# problem_dictionary["Status"]="Married"
# print(problem_dictionary)
# problem_dictionary["Name"]="vaishali"
# problem_dictionary["Sex"]="Female"
# print(problem_dictionary)

# for key in problem_dictionary:
#     print(key)
#     print(problem_dictionary[key])
##########converting score to grades dictionary#####
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key]="Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key]="Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key]="Acceptable"
    else:
        student_grades[key]="Fail"

# print(student_grades)

#######################################################

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

#Nesting Dictionary in a Dictionary

# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
def add_new_country(country_visited, times_visited, cities_visited):
  dictionary_new_country={}
  dictionary_new_country["country"]=country_visited
  dictionary_new_country["visits"]=times_visited
  dictionary_new_country["cities"]=cities_visited
  travel_log.append(dictionary_new_country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

