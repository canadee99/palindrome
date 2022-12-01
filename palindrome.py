s1 = (input("please enter a word: "))
s2 = s1[::-1]
#print(s2)
if s2 == s1:
    print('this word is a palindrome')
else:
    print('this word is not a palindrome')