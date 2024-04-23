import re

senha = 'v2Ts7<o9T~}Y'

password_reg = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@[-`{-~]).{12,}$', re.M
)

print(password_reg.findall(senha))
