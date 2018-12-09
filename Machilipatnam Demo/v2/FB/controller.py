import os
while(1):
    if( os.stat("buf.txt").st_size != 0 ):
        f=open("buf.txt","r")
        print(str(f.read()))
        f.close()
        f=open("buf.txt","w")
        f.write("")
        f.close()
