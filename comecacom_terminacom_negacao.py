# meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# ^ = começa com
# $ = termina com
# [^a-z] = negaçao, qualquer coisa que nao a-z
import re

cpf = 'a 147.852.963-12 a'
cpf2 = '147.852.963-12 a'
cpf3 = '147.852.963-12'

print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf2))
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf3))
