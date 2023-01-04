
import pprint



people = {}
people['suarez'] = {'name':'suarez',
         'gender': 'male',
         'ocupation':'researcher',
         'home planet':'planeta tierra'}
print(people['suarez'])



#A dictionary of dictionaries (a.k.a.a table)

people['Nava'] = {'name':'suarez',
         'gender': 'male',
         'ocupation':'researcher',
         'home planet':'planeta tierra'}
print(people['suarez'])

people['dann'] = {'name':'suarez',
         'gender': 'male',
         'ocupation':'researcher',
         'home planet':'planeta tierra'}

people['dancito'] = {'name':'suarez',
         'gender': 'male',
         'ocupation':'researcher',
         'home planet':'planeta tierra'}


pprint.pprint(people)