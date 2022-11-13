prices = []
temps = [32.0, 212.0, 0.0, 81.6, 100.0, 45.3]
words = ['hello', 'danie', 'suarez', 'nava']
car_details = ['toyoto', 'rva4' , '2,2' , 4654654]
everything = [prices, temps, words, car_details]
odds_and_end = [[1,2,3], ['a','b', 'c'], ['one', 'two', 'three']]
vowels = ['a', 'e', 'i', 'o','u']
word = "daniel san"

print("imprimir lo que sea en una lista")
for j in range(0,len(temps)-1):
    print(temps[j])
    print(vowels[j])

print("buscar letra" )
for i in word:
    if i in vowels:
        print(i)

        # print(words[i])
        # print(car_details[i])
        # print(everything[i])
        # print(odds_and_end[i][i])
        # print(vowels[i])
        # print(word[i])

print("saber cuanto mide la listas" )
founf = []
print(len(founf))

founf.append('E')
founf.append('B')
founf.append('D')
founf.append('EC')
print(founf)

print("encontrar vocales en una palabra")
wordp = "fanielfadlksfjkñajdf"
vowelp = ['a', 'e', 'i', 'o', 'u']
foundp = [] 

for letrap in wordp:
    if letrap in vowelp:
        print(letrap)
        if letrap not in foundp:
            foundp.append(letrap)
            for vo in foundp:
                print("")             
print(foundp)
print(letrap)     

print("remove letters")
nums = [1,2,3,4,5,6] #una lista es un objeto?
nums.remove(3)
print(nums)


print("toma un valor aleaotira")
print(nums.pop(1))
print(nums)

print("insertar objetos a una lista")
nums.insert(3,"daniel")
print(nums)

print(type(nums))


