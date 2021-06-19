str = input('enter the string: ').lower()
str1 = str.replace(" ","")
str2 = str1[::-1]
if str1 == str2:
    print('This is a palindrome')
else:
    print('This is not a palindrome')
# examples of palindromes in Russian
# Лёша на полке клопа нашёл
# А роза упала на лапу Азора
# Я арка края
# О лета тело
# examples of palindromes in English
# A man, a plan, a canal-Panama 
# Was it a car or a cat I saw
# Do geese see God?
