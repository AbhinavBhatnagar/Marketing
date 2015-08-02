__author__ = 'abhatna4'

from ast import literal_eval
output = open('addresses.txt', 'wb')

def main():
    listed = []
    common = []
    with open('address.txt', 'r') as file:
        for lines in file:
            #print lines.rstrip()
            line = lines.split("""'----'""")
            for l in line:
                na = l.split('\t')
                if len(na[1]) != 2:
                    output.write(str(l)+"\n")




if __name__ == '__main__':
    main()