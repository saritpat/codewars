def rot_90_clock(strng):
    ans = ''
    index = 0
    lst = strng.split('\n')

    while index < len(lst[0]):
        for i in range(len(lst)-1, -1, -1):
            ans+=lst[i][index]
        index+=1
        if index < len(lst[0]):
            ans+='\n'

    return ans

def diag_1_sym(strng):
    ans = ''
    index = 0
    lst = strng.split('\n')

    while index < len(lst[0]):
        for i in range(len(lst)):
            ans+=lst[i][index]
        index+=1
        if index < len(lst[0]):
            ans+='\n'

    return ans

def selfie_and_diag1(strng):
    ans = ''
    index = 0
    sel = strng.split('\n')
    diag = diag_1_sym(strng).split('\n')

    for i in range(len(sel)):
        ans+=(sel[i]+'|')
        ans+=(diag[i])
        if index < len(sel[0])-1:
            ans+='\n'
            index+=1

    return ans

def oper(fct, s):
    return fct(s)


# "Sixdvr\ndJNCGg\nmBWhca\nEYgZEv\nKDXVKc\nbORWle"
print((oper(rot_90_clock, "rgavce\nvGcEKl\ndChZVW\nxNWgXR\niJBYDO\nSdmEKb")))
# "weetvI\nuNhBWF\nUHiTNk\nyWflpG\nPxmFdj\nCwiIvZ"
print((oper(diag_1_sym, "wuUyPC\neNHWxw\nehifmi\ntBTlFI\nvWNpdv\nIFkGjZ")))
# "NJVGhr|NMtsrz\nMObsvw|JOPotj\ntPhCtl|VbhEQl\nsoEnhi|GsCnRi\nrtQRLK|hvthLW\nzjliWg|rwliKg"
print((oper(selfie_and_diag1, "NJVGhr\nMObsvw\ntPhCtl\nsoEnhi\nrtQRLK\nzjliWg")))