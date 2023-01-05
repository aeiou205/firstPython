def search4vowels(phrase:str)-> set:
    """return any vowels found in a supplied phrase"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def serch4letter(phrase:str, letters:str) -> set:
    return set(letters).intersection(set(phrase))


def main():
    v1=serch4letter("daniel","suartez")
    print(v1)
    
    v2=search4vowels("usraezoo")
    print(v2)

if __name__ == "__main__":
    main()