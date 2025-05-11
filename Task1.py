try:
    f1=open("sample.txt",'r')
    print("Reading file content:")
    i=1
    for line in f1.readlines():
        print('Line '+str(i)+": "+line,end="")
        i+=1
    f1.close()
except:
    print("Error: The file 'sample.txt' was not found.")
