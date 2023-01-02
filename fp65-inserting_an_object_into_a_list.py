LIST = [0,1,2,3,4,5]

LIST.extend([6,7])
print(LIST)
LIST.insert(0,9)
print(LIST)
LIST.insert(2,4554)
print(LIST)

phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()

plist.pop(0)
plist.remove("'")
print(plist)
plist.extend([plist.pop(), plist.pop()])
plist.insert(2,plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)



