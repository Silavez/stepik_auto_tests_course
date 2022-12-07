s = input()
counter = 0
text = s.split()
for i in text:
    if i.lower() in ('a', 'an', 'the'):
        counter += 1
print('Общее количество артиклей:', counter)

#  s = input().split().lower()
#  print('Общее количество артиклей:', s.count('a') + s.count('an') + s.count('the'))