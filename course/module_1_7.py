# initial data
# list of students' grade lists,
# sorted in alphabetical order by students' names
grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
# students' names
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# calculate average values of students' grades
#   using [x for x in iterable] list datatype's construction method
# print a mapping of the students to their average grades
#   using type class'es zip() transposing method
print(dict(zip(sorted(list(students)), [sum(x)/len(x) for x in grades])))