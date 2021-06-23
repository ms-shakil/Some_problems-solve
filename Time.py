## Convert seconds to Hours minutes and seconds
def TimeConvert(Inp):
    Hours=  int(Inp/3600) #we know 1 hours == 3600 seconds
    Minutes = int((Inp/60)-(Hours*60)) # we know 1 min == 60 seconds
    Seconds = Inp -(Hours*3600 + (Minutes*60))
    print("Hours:{} Minutes:{} Seconds:{}".format(Hours,Minutes,Seconds))
    
while True:
    try:
        Inp = int(input("Enter The value of Seconds:"))
    except ValueError:
        print("Please Enter the number value.")    
    else:
        break   
    
TimeConvert(Inp)     
 