# meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# * = 0 ou n
# + = 1 ou n
# ? = 0 ou 1
#  *? 1 ou n nao gulozo, lazy
import re


text = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''
# GREEDY  vai pegar da abertura ate o ultimo fechamento
# NON GREEDY,LAZY vai pegar da abertura ate o primeiro fechamento

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', text, re.I))  # greedy
# non greedy lazy
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', text, re.I))
