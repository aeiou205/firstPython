def serarch4vowels(word:str)-> set: #
    """returno any vowels found found in a supplied word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

def main():
    a = serarch4vowels("daniel suarez nava")
    print(a)

if __name__ == "__main__":
    main()

    