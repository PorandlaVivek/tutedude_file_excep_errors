data=input("Enter text to write to the file: ")
f=open("output.txt","w")
f.write(data+'\n')
print("Data successfully written to output.txt.\n")
f.close()

data=input("Enter additional text to append: ")
f=open("output.txt","a")
f.write(data+'\n')
print("Data successfully appended.\n")
f.close()

print("Final content of output.txt:")
f=open("output.txt","r")
data=f.read()
f.close()
print(data)