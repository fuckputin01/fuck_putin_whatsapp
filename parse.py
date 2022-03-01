import re
pattern = '[(]{0,1}[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}[(]{0,1}'
pattern2 = '[(]{0,1}[0-9]{3}[\s-]+[0-9]{3}[\s-]+[0-9]{2}[\s-]+[0-9]{2}[(]{0,1}'
#                             # them (+)
# lines = "property"           # adding input string, raw_input("Enter Combination: ")
# ls = re.findall(pattern,lines)
# print ls

def parse():
    with open('1.txt', 'r') as f:
        q = f.read()
        ls = re.findall(pattern2, q)
        with open('list2.csv', 'w') as w:
            w.write('Primary Phone\n')
            for p in ls:
                w.write(f'+7-{p}\n')

if __name__ == '__main__':
    parse()
