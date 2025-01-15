# def word_mesh(words):
#     ans = ''
#     temp = ''
#     index = 0
#     for word in range(len(words)-1):
#         i = 0
#         while i < len(words[word]):
#             if words[word][i] == words[word+1][index]:
#                 temp+=words[word][i]
#                 index+=1
#                 i+=1
#             elif words[word][i] == words[word+1][0] and index != 0:
#                 temp=words[word][i]
#                 index = 1
#                 i+=1
#             else:
#                 temp = ''
#                 index = 0
#                 i+=1
        
#         if temp == '':
#             return 'failed to mesh'
            
#         ans+=temp
#         temp = ''
#         index = 0

#     return ans

def word_mesh(words):
    ans = ''
    temp = ''
    for word in range(len(words)-1):
        i = 0
        while i < len(words[word]):
            if words[word][i] == words[word+1][0] and words[word][i:] == words[word+1][:len(words[word][i:])]:
                temp+=words[word][i:]
                break
            i+=1
        
        if temp == '':
            return 'failed to mesh'
            
        ans+=temp
        temp = ''

    return ans


print(word_mesh(["beacon", "condominium", "umbilical", "california"]))
print(word_mesh(["allow", "lowering", "ringmaster", "terror"]))
print(word_mesh(["abandon", "donation", "onion", "ongoing"]))
print(word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]))
print(word_mesh(['golden', 'nebula', 'landfall', 'llama', 'amanda']))