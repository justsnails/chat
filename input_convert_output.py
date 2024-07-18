def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
        print(lines)
    return lines

def convert_file(lines):
    new = []
    for line in lines:
        if line == 'Allen':
            person = 'Allen' 
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        new.append(person + ':' + line)
    print(new)
    return new

def output(filename,new):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for out in new:
            f.write(out + '\n')

    
def main():
    lines = read_file('input.txt')
    new = convert_file(lines)
    output('output.txt',new)

main()