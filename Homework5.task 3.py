s1 = input()
s2 = input()
def check_Anagram(s1, s2):
    return sorted(s1) == sorted(s2)
if check_Anagram(s1,s2):
    print('Являются анаграммами')
else:
    print('Не являются анаграммами')