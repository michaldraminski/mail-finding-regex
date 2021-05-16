# Michał Dramiński, 176093
import re

print("\nZnalezione maile:")
with open("tekst.txt", 'r') as example:
    text = example.read()
    matches = re.findall(r'(?<=[\s|\(])(?:(?:\"\\\".*?\"|\".*\")|[.+\w]+)@(?:[\w-]+\.+[\w.-]+|com|\[IPv6[0-9a-f:]+\])', text)
    i = 1
    for match in matches:
        print(i,". ", match)
        i += 1
