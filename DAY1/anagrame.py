def anagram(str1, str2):
    temp_str1 = sorted(str1)
    temp_str2 = sorted(str2)
    count = 0
    for i in range(len(temp_str1)):
        if temp_str1[i] == temp_str2[i]:
            continue
        else:
            count += 1
            break
    if count == 0:
        print('Anagram')
    else:
        print('Not Anagram')


str1 = input("enter string 1st")
str2 = input("enter string 2nd")
anagram(str1, str2)