import argparse

def hexrake():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
 
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        # check if [8] has :
        # lenght must be > 58 or there is a problem with out input
        x = line[10:58]
        
        words = x.split(' ')
        print(words)
        #print("Line{}: {}".format(count, line.strip()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hex Dump Utitliy')
    parser.add_argument('-f', '--filename', help='Filename to process', required=True)
    parser.add_argument('-o', '--output', help='File to store output')
    
    args = parser.parse_args()
    
    hexrake()
    #h = hxdmp(args)
    #h.run()