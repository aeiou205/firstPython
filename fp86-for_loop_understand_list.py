# paranold_android = "daniel"
# letters = list(paranold_android)
# for char in letters: # in a iteration we can put size with same varible
#     print(char) 

paranold_android = "Daniel queria un iphone pero no le alcanzo"
letters = list(paranold_android)
for char in letters[:6]: #start 0 . END 6
    print(char)

print()

for char in letters[-7:]: #start:-7 or 7 , EnD:-1
    print(char)
print()

for char in letters[12:20]: #start: 12, End 20
    print(char)
