#List are great, but i sometimes need more structure in my life
#las listas son buenas , pero yo aveces necesito mas estructura in mi vida

person3 = {
            'name':'daniel',
            'gender':'Male',
            'Occupation': 'Research',
            'Home Planet': 'Betelgeuse Seven'
}

print(person3)
print(person3['Home Planet'])
print(person3['name'])

found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
print(found)

found['e'] += 1 
print(found)

for kv in found:
    print(kv)
    print(kv , 'was found', found[kv], ' time(s).')


for kv in sorted(found): # eso es una pequeño para el ciclo del codigo pero 
    print(kv , 'was found', found[kv], ' time(s).')
    # la salida esta ordenada 


#the items method passes back two loop variables
#los elementos del metodo son pasados por 2 variables del ciclo
#el metodo items devuelve dos  variables 

#we invoke the items method on the found dictionary
#inovacamos el metodo items en "found" dicionario para saber los items








#
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s)')

fruits = {}
print(fruits)
print(fruits)
fruits['aples']= 10
print(fruits)

if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1

print(fruits)

#we can asignament index in a list for search aftters

if 'pears' not in fruits:
    fruits['pears'] = 0

fruits['pears'] +=1
fruits['pears'] +=1

print(fruits)

vowels = ['a','e','i','o','u',]
word = input("provide a word to search for vowels:")

found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k,'was found', v, 'time')


vowels = ['a', 'e', 'i','o','u']
wprd = input("ingrese una palabra")
found = []
for letter in wprd:
    if letter in wprd:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)


print("---------------------")
vowelsss = {'a' , 'e' , 'e' , 'i', 'o','u','u'}
print(vowelsss)
vowelss2 = set('aeeiouu')
print(vowelss2) 


