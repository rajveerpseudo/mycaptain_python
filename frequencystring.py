def most_frequent(string):
    dd = dict()
    for counter in string:
        if counter in dd:
            dd[counter]+=1
        else:
            dd[counter]=1
    return (dd)

in_=input("Enter String")
print(most_frequent(in_))
