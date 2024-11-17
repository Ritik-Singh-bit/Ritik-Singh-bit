from time import *
import random as r 
print(time( ))
def mistake(para,user):
    error = 0
    for i in range (len(para)) :
        try:
            if para[i] != user[i]:
                error=error +1
        except :
            error = error +1
    return error
def speed_time (time_s,time_e,user):
    time_delay=time_e-time_s
    time_R = round(time_delay,2)
    speed = len(user)/ time_R
    return round(speed)
                  

while True: 
 ck = input('ready to test : yes/ no :')
 if ck == "yes":

     test = [ " hi my name is ritik and this is my typing speed test program "," welcome to type word "]
     test1 = r.choice(test)
     print(" ***** typing speed ***** ")
     print(test)
     print()
     print()
     time_1 = time()
     testinput = input(" enter : ")
     time_2 = time()

     print('speed : ',speed_time (time_1,time_2, testinput),"w/sec")
     print ('Error : ' ,mistake(test1,testinput))
 elif ck == "no" :
     print("thank ypu ")  
     break
 else:
     print("wrong input")