def vert_mirror(strng):
    ans = ''
    count = 0
    lst = strng.split('\n')

    for word in lst:
        for i in range(len(word)-1, -1, -1):
            ans+=word[i]
        if count < len(lst)-1:
            ans+='\n'
            count+=1
    return ans
    
def hor_mirror(strng):
    ans = ''
    count = 0
    lst = strng.split('\n')

    for i in range(len(lst)-1, -1, -1):
        ans+=lst[i]
        if count < len(lst)-1:
            ans+='\n'
            count+=1

    return ans
    
def oper(fct, s):
    return fct(s)

# "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw"
print(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))
# "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP"
print(oper(vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"))
# "WQuc\nDuOx\npwZf\nxFqe"
print(oper(vert_mirror, "cuQW\nxOuD\nfZwp\neqFx"))
# "olodIGDC\ngIrfXtsU\nLWxvjqMt\nmAnCuyEB\naREEaxsx\nSZiOvsZx\nEXRBltuL\nEqbhhsxt"
print(oper(vert_mirror, "CDGIdolo\nUstXfrIg\ntMqjvxWL\nBEyuCnAm\nxsxaEERa\nxZsvOiZS\nLutlBRXE\ntxshhbqE"))

# "yeCt\nCSbg\nJVhv\nlVHt"
print(oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"))
# "cEYz\nLPKo\ndbrZ\nnjMK"
print(oper(hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz"))
# "owoq\nWLUG\ntmFe\nQMxo"
print(oper(hor_mirror, "QMxo\ntmFe\nWLUG\nowoq"))
# "QoSy\nuGef\ndZQn\nFYvi"
print(oper(hor_mirror, "FYvi\ndZQn\nuGef\nQoSy"))