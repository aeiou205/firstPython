found = ['a','e']

if 'u' not in found:
    found.append('el burro sabe mas que tu')
print(found)

vowels = ['a','e','i','o','u']
word = input("ingrese una cadena:   ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

    