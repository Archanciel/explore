import re


def parse(text, pattern):
    listOfParagraphs = []

    for match in re.finditer(pattern, text):
        print('groups: ', match.groups())
        print('\tsub groups ({}):'.format(len(match.groups())))
        i = 1
        for subGroup in match.groups():
            print('\t\t{}/ '.format(i), subGroup)
            i += 1
            listOfParagraphs.append(subGroup)

    return listOfParagraphs


def printList(list):
    print('list: ', end='')

    for line in list:
        print(line, end='')

    print()


txtWithAmountList = ['100usd', 's19.8usd', '0', 'chf', 'schf', 'chf.bittrex', 'schf.bittrex', '10.4chf.bittrex', 's10.4chf.bittrex']
patternWithAmount = r'(?:([sS]?)([\d\.]*)([a-zA-Z]+)(?:(?:\.)(\w+))?)|(0)'

print('patternWithAmount', patternWithAmount)
print()

for txt in txtWithAmountList:
    print(txt)
    list = parse(txt, patternWithAmount)
#    printList(list)

txtNoAmountList = ['0', 'chf', 'schf', 'chf.bittrex', 'schf.bittrex']
patternNoAmount = r'(?:([sS]?)([a-zA-Z]+)(?:(?:\.)(\w+))?)|(0)'

print('patternNoAmount ', patternNoAmount)
print()

for txt in txtNoAmountList:
    print(txt)
    list = parse(txt, patternWithAmount)
#    printList(list)
