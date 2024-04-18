# meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# * = 0 ou n
# + = 1 ou n
# ? = 0 ou 1
# {}  =  {n} ou {min, max}
# ex {10} 10veses {,10} de 0 a 10 {1,} de 1 a n (1,10)de 1 a 10
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

print(re.findall(r'Jo+ão+', text, re.I))
print(re.sub(r'Jo+ão+', 'Felipe', text, re.I))
print(re.findall(r'Jo{1,}ão{1,}', text, re.I))

a = 'ama amado'
print(re.findall(r'ama[od]*', a, re.I))
