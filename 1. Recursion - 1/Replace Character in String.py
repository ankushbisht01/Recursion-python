'''
Question - 
create a function taking a string , and two alphabet as input and replace the first alphabet with the second alphabet 
in the string using recursion.

Sample input -
'Python is great programming language' , 'a' , 'b'

Sample Output-
'Python is grebt progrbmming lbngubge'

'''

def ReplaceChar(word,a,b):
    if len(word)==0:
        return word
    Rec_string = ReplaceChar(word[1:],a,b)
    if word[0]==a:
        return b + Rec_string
    else:
        return word[0]+Rec_string
