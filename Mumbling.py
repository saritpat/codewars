def accum(st):
    ans = ''
    for i in range(len(st)):
        ans += st[i].upper()
        ans += st[i].lower()*i

        if i < len(st)-1:
            ans += '-'
        
    return ans

print(accum('ZpglnRxqenU'))
print(accum('NyffsGeyylB'))
print(accum('MjtkuBovqrU'))
print(accum('EvidjUnokmM'))
print(accum('HbideVbxncC'))