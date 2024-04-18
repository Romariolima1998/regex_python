# meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# (grupo) deve ser encontrado exatamente o conteudo
# pode ser acessado como uma variavel ex
# () \1,  () () \1 \2, (()) \1de fora e \2 de dentro
# (?: na frente) nao salva e nao retorna o grupo
import re


text = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''

print(re.findall(r'(<([pdiv]{1,3})>(.*?)<\/\2>)', text, re.I))
print(re.sub(r'(<(.+?)>)(.*?)(</\2>)', r'\1"\3"\4', text))
