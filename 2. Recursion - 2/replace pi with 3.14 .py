'''
Question - 
create a function that will take an string as input and replace all pi wit h 3.14 in that string

sample input - 
xdepixdf
Sample output - 
xde3.14xdf
'''


def ReplacePi(x):
    if len(x)==1:
        return x
    smaller_string = ReplacePi(x[1:])
    if x[:2]=='pi':
        return '3.14'+ smaller_string[1:]
    else :
        return  x[0]+smaller_string

def main():
    input_string = input('enter the string which you want to convert:  ')
    string_with_replaced_pi = ReplacePi(input_string)
    print(string_with_replaced_pi)

if __name__ == '__main__':
    main()