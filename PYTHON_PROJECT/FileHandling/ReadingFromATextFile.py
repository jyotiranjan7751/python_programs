f=open("C:/Users/Jyotiranjan Nath/Desktop/Notes/pythonNotes.txt","r")# r means read the file 
#myNotes=f.read()#It will read all the text files
#myNotes=f.read(10)#It will read the 10 chracters
myNotes=f.readlines()# It will return all lines in List
print(myNotes)
f.close()