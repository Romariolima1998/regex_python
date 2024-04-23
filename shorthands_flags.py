# \w = [a-zA-Z0-9À-ú]
# \w + re.A =[a-zA-Z0-9]
# \W = o inverso de\w [^a-zA-Z0-9À-ú] qualquer um que nao estes
# \d = [0-9]
# \D = [^0-9]
# \s = [ \r\n\f\t]
# \S = o inverso de \s
# \b = espaço vazio no começo ou no fim de cada palavra
# \B nao borda

# re.A ASCII
# re.I IGNORECASE
# re.M MULTILINE ^ $ faz ser aplicado no começo e final das linhas
# re.S DOTALL
import re


text = '''
João troxe   flores ppara sua amada namorada em 10 de janeiro 1970.
Maria era o nome dela.


Foi um ano exelente na vida de joão. Tve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de 
domingo. Também né! Sendo a boa mineira que é, nunca esqueceu do seu famoso 
pão de queijo.
não canso de ouvir a Maria:
Joooooooãooooooo, o café ta prontinho aqui. Veeemm!
'''

print(re.findall(r'[a-z]+', text, re.I))
print(re.findall(r'[a-zA-Z0-9À-ú]+', text))
print(re.findall(r'\w+', text))
print(re.findall(r'\W+', text))
print(re.findall(r'\D+', text))
print(re.findall(r'\be\w+', text))  # começa com e
print(re.findall(r'\w*e\b', text))  # termina com e
print(re.findall(r'\b\w{4}\b', text, flags=re.I | re.DOTALL))  # tem 4 letras
