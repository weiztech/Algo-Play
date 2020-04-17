'''
Scanning Technique

2 input:

string data: abracadabra28891kaggletor9912121212
blacklist data: ['abra', 'abracada', 'kaggle', 'kabra', 'tadabra', '771', '28891', '21212', 'telolet']

find blacklist data from string data expected result 
['abra', 'abracada', '28891', 'kaggle', 'kabra', 'tabracadabra', '21212']
'''

string = 'abracadabra28891kaggletor9912121212'
blacklist = ['abra', 'abracada', 'kaggle', '771',
             '28891', '21212', 'telolet', 'kabra', 'tabracadabra']


start_idx = 0
match = []
while start_idx <= len(string)-1:
    check_string = ''
    for char in string[start_idx:]:
        check_string += char
        if check_string in blacklist and check_string not in match:
            match.append(check_string)

    check_string = string[start_idx]
    for char in string:
        check_string += char
        if check_string in blacklist and check_string not in match:
            match.append(check_string)

    start_idx += 1

print('Match string: {}'.format(match))
print(match == ['abra', 'abracada', '28891',
                'kaggle', 'kabra', 'tabracadabra', '21212'])
