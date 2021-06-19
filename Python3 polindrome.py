str = input('enter thee string: ').lower()
str1 = str.replace(" ","")
l = len(str1)
one = str1[:l//2]
two = str1[l//2:]
if l % 2 != 0:
    one += (str1[l//2])
two = two[::-1]
if one == two:
    print('this is a palindrome')
else:
    print('this is not a palindrome')
# examples of palindromes in Russian
# Лёша на полке клопа нашёл
# А роза упала на лапу Азора
# Я арка края
# О лета тело
# examples of palindromes in English
# A man, a plan, a canal-Panama 
# Was it a car or a cat I saw
# Do geese see God?
