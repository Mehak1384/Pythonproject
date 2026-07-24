str=input("Enter the string you want to split and join")
def split(str):
    return str.split()
print(split(str))
def join(str):
    str="-".join(str)
    return str
print(join(str))
"""Given above code output is ['this', 'is', 'a', 'string']
 -t-h-i-s- -i-s- -a- -s-t-r-i-n-g- - -  and our required output is this this-is-a-string"""
def split_and_join(line):
     str=line.split()
     str ="-".join(str)
     return str
print(split_and_join(str))


