vowels = set('aeiou')
word = 'hello'


u = vowels.union(set(word))
print(u)


u_list = sorted(list(u))
print(u_list)


#diferrence tells you whatś not shared

d = vowels.difference(set(word))
print (d)


i = vowels.intersection(set(word))
print(i)