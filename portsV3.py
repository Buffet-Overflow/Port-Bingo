import re

def main():
    while True:
        port = input("Port number: ")
        search = open(r'<ENTER PATH TO Port_List.txt>','r')
        for line in search:
            if line.split(" ")[0] == port:
                print(line)
                
if __name__ == "__main__":
    main()
