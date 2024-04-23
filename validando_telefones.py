import re

numbers = '''
(21) 9 8852-5214
(11)9955- 1231
(35) 9 9975-2587
9 8571-5213
1234 5647
'''

number_reg = re.compile(
    r'^((?:\(\d{2}\)\s)(?:9\s)(?:\d{4}-\d{4}$))', re.MULTILINE)

print(number_reg.findall(numbers))
