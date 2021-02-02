a, t = '<svg fill="none" viewBox="0 0 800 400" width="800" height="400" xmlns="http://www.w3.org/2000/svg"><defs>', input("Give me a string consists of at least five latin letters where no letter repearts:\n")[::-1]
assert len(set(t.lower())) == len(list(t.lower()))
assert len(t) >= 5
for i in range(len(t)):
    assert t[i] in [chr(j) for j in list(range(65, 91)) + list(range(97, 123))]
    a += f'<pattern id="{t[i]}" width="20" height="20" patternUnits="userSpaceOnUse" patternTransform="scale(0.5,0.5)">'
    for j in range(len(t)): a += f'<rect width="20" height="20" fill="url(#{t[i + 1]})"/>' if i + 1 != len(t) else '<rect width="20" height="20" fill="none"/>'
    a += '</pattern>'
print(a + f'</defs><ellipse fill="url(#{t[0]})" stroke="black" stroke-width="5" cx="400" cy="200" rx="350" ry="150"/></svg>')
# The svg file was generated using this code with this input: abcdefghiz
