with open('1punto3.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')

with open ('2punto3.txt') as g:
    glines = g.readlines()

with open ('1punto3.txt', 'w') as f:
    for i in range(len(lines)):
        f.write('\n' + lines[i] + ' ' + glines[i] )