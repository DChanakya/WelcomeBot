from firebase import firebase
firebase = firebase.FirebaseApplication('https://welcomebiryani-51293.firebaseio.com/', None)
while(1):
    try:
        result = firebase.get('/table', None)
        if("None" not in result):
            f=open("buf.txt",'w')
            f.write(str(result))
            f.close()
            firebase.delete('/table', None)
    except:
        print("")
