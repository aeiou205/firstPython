#Function_Return_a_result

#python come with a built-in function called bool that, when provided with any value, tells
#tells you whether the value evaluates to true or fals

#python comenzar con una funcion construida llamadas bool que cuando provee un valor 
# llamas el valor de valores verdadero o falsoo

print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(None))

print(bool(1))
print(bool(-1))
print(bool(42))
print(bool(0.00000000000000000000000000000000001))
print(bool('panic'))
print(bool([42,34.32]))
print(bool({'a': 42, 'b': 23}))

def search3vowels(word):
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        return bool(vowel)

def main():
    vowel = search3vowels('daniel')
    print ("true or false :",vowel)

if __name__ == "__main__" :
    main()

