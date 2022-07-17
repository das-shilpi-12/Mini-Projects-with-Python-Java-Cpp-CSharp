height = int(input("Enter the Height of the tree: \n")) #height
width =  int(input("Enter the Width of the tree: \n"))#width
print (height,"\n")
print (width,"\n")
space = height*width #corner space
m = 1 #to print

#uppper part leaves
for r in range(1,height+1):
    for x in range(m,width+1):
        for y in range(space,x-1,-1):
            print(" ",end="")
        for z in range(1,x+1):
            print("🌲",end="")
        print()
    m = m+2
    width = width+2
#lower part - stem
for x in range(1,5):
    for y in range(space-5,-1,-1):
        print(" ",end="")
    for z in range(1,5):
        print("🌲",end="")
    print()
