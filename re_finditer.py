import re


def parse(text, pattern):
    listOfParagraphs = []

    for match in re.finditer(pattern, text):
        print('groups: ', match.groups())
        print('\tsub groups:')
        for subGroup in match.groups():
            print('\t\t', subGroup)
            listOfParagraphs.append(subGroup)

    return listOfParagraphs


def printList(list):
    print('list: ', end='')

    for line in list:
        print(line, end='')

    print()


text = "Hello world 475 times you said that for 2 people"
pattern = r'(\D+)(\d+|.*)'

print(text)
print(pattern)
print()

list = parse(text, pattern)
printList(list)
