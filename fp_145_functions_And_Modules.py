def search3vowels():

    vowels = set('aeiou')
    word = input('provides a word to search for vowels:')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


def main():
    print("hola")
    search3vowels()

if __name__ == "__main__" :
    main()
