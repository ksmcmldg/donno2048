from os import system, name
a, t = '<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">\n\t<defs>', input("Give me a string consists of at least five Latin letters in which no letter repeats:\n")
assert len(set(t.lower())) == len(list(t.lower())) >= 5
for i in range(len(t)):
    assert t[i] in [chr(j) for j in list(range(65, 91)) + list(range(97, 123))]
    a += f'\n\t\t<pattern id="{t[i]}" width="{i + 1}" height="{i + 1}">'
    for j in range(len(t)): a += f'\n\t\t\t<rect width="{j + 1}" height="{j + 1}" fill="url(#{t[i + 1]})"/>' if i + 1 != len(t) else f'\n\t\t\t<rect width="{j + 1}" height="{j + 1}" fill="none"/>'
    a += '\n\t\t</pattern>'
system('cls' if name == 'nt' else 'clear')
print(a + f'\n\t</defs>\n\t<ellipse fill="url(#{t[0]})" cx="{i + 1}" cy="{i + 1}" rx="{i}" ry="{i}"/>\n</svg>')
input("Press any key to continue...")
