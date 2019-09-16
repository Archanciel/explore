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


txtList = ['100usd', 's19.8usd', '0', 'chf', 'schf', 'chf.bittrex', 'schf.bittrex', '10.4chf.bittrex', 's10.4chf.bittrex']
patternWithAmount = r'(?:([sS]?)([\d\.]*)([a-zA-Z]+)(?:(?:\.)(\w+))?)|(0)'

print(patternWithAmount)
print()

for txt in txtList:
    print(txt)
    list = parse(txt, patternWithAmount)
#    printList(list)
