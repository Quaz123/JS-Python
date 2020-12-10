import re

pattern_1 = re.compile('Niebieski')
result_1 = pattern_1.finditer('bridge_of_death')
print(type(result_1))

for substring in result_1:
    print(substring)

s1 = 'Blue Berries'
pattern = 'Blue Berries'
for match in re.finditer(pattern, s1):
    s = match.start()
    e = match.end()
    print('String match "%s" at %d:%d' % (s1[s:e], s, e))
