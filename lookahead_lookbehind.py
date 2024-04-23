import re
from pprint import pprint

text = '''
online 192.168.0.1 ghijk active
online 192.168.0.2 ghijk active
offline 192.168.0.3 ghijk inactive
online 192.168.0.4 ghijk active
online 192.168.0.5 ghijk inactive
offline 192.168.0.6 ghijk active
'''

# positive lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', text))
# negative lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', text))
# positive lookbehind
pprint(re.findall(r'\w+(?<=online)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w', text))
# negative lookbehind
pprint(re.findall(r'\w+(?<!online)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w', text))
