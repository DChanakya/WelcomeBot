import os
data=''
k=1;
while(k==1):
    if( os.stat("buffer.txt").st_size != 0 ):
        f=open("buffer.txt","r")
        data=(str(f.read()))
        f.close()
        f=open("buffer.txt","w")
        f.write("")
        f.close()
        i=i+1;
mat=[]        
mat=data.split(",");
stri=list(map(int, mat))
print(stri);
matr=[]
matr.append(stri);
matr.append([0,0,0,0]);
matr.append([0,0,0,0]);
matr.append([0,0,0,0]);
print(matr)
