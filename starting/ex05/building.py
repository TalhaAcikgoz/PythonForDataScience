import sys


def main(inp):
    """ main function """
    if inp == "":
        sentence = input("Gimme the sentence: ")
    else:
        sentence = inp
    pun = "!\"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~"
    print(f'{len([i for i in sentence if i.isupper()])} upper letters')
    print(f'{len([i for i in sentence if i.islower()])} lower letters')
    print(f'{len([i for i in sentence if i in pun])} punctuation marks')
    print(f'{len([i for i in sentence if i == " "])} spaces')
    print(f'{len([i for i in sentence if i.isnumeric()])} digits')


if __name__ == "__main__":
    string = ""
    try:
        string = sys.argv[1]
        main(string)
    except EOFError:
        print("\nbye")
    except Exception as e:
        main("")
