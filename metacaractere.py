# meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | = ou
# . = qualquer caractere, com exessao a quebra de linha
# []  = conjuntos de caracteres
import re


text = '''
João troxe   flores ppara sua amada namorada em 10 de janeiro 1970.
Maria era o nome dela.


Foi um ano exelente na vida de joão. Tve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de 
domingo. Também né! Sendo a boa mineira que é, nunca esqueceu do seu famoso 
pão de queijo.
não canso de ouvir a Maria:
Joooooooãooooooo, o café te prontinho aqui. Veeemm!
'''

print(re.findall(r'João|Maria', text))
print(re.findall(r'.oão', text))
print(re.findall(r'[jJ]oão', text))
# qualquer coisa entre a e z e 0 a 9
print(re.findall(r'[A-Z a-z 0-9]oão', text))
print(re.findall(r'JoãO|MariA', text, flags=re.I))
