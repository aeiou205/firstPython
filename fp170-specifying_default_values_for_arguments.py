def search4leteers(phrase:str, letters:str= 'aeiou')-> set:
    """return any vowels found in a supplied phrase"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def main():
    v1=search4leteers("life, the universe, and everything")
    print(v1)

if __name__ == "__main__":
    main()






