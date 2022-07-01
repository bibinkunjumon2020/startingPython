name='luminartechnolab'
vowel='aeiou'

#for element in name:
 #       print([element if element==vowel[i] for i in range(0,5) ])


lst=[i for i in name if i in vowel]
print(lst)