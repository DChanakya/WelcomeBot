from firebase import firebase
firebase = firebase.FirebaseApplication('https://welcomebiryani-51293.firebaseio.com/', None)
result='';
try:
    result = result+firebase.get('/table1', None)
    i=2;
    while i<5:
        result = result+","+firebase.get('/table'+str(i), None)
        i=i+1
        print(result)
    if("None" not in result):
        f=open("buffer.txt",'w')
        f.write(str(result))
        f.close()
except:
    print("adsa")
        


