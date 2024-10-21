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

# for latest python versions, where sets are ordered collections
# print(dict(zip([x for x in students], [sum(x)/len(x) for x in grades])))
# end of program

# for older python versions

# calculate average values of students' grades
# using [x for x in iterable] list datatype's construction method
grades = [sum(x)/len(x) for x in grades]

# make students an ordered collection
students = list(students)
# sort students using list datatype's sort() method
students.sort()

# print a mapping of the students to their average grades
# using type class'es zip() transposing method
print(dict(zip(students, grades)))
