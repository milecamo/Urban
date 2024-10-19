# Dictionary of relative's names (keys) and their birth years (values)
my_dict = {'Olga'   :1963,
           'Valery' :1957,
           'Oksana' :1985,
           'Roman'  :1983}
print("The dictionary:", my_dict)

print("Father's birth year:",
      my_dict['Valery'])
print("Dmitry's birth year:",
      my_dict.get('Dmitry', 'there is no such an entry'))

# Add some friends's birth years
my_dict.update({'Dmitry'    :1982,
                'Blanca'    :1980})

print("Sister's birth year, poped from the dictionary:",
      my_dict.pop('Oksana'))
print("Resulted dictionary, after updates:",
      my_dict)

my_set = {'You', 'me', 'me', False, 1, 3, 3, 4, 'You', True, 0, False, 2.4}
print( "My set:", my_set )

# add some hashable data
my_set.add(('George',0))
my_set.add(1+4j)
# and
my_set.discard(0)
print( "Updated set:", my_set )