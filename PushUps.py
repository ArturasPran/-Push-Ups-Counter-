""" Arturas Pranskunas
    This is the second part of "Push-Ups Counter"  project
    The project can be found at https://ehelper.tk/
  
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
"""
import RPi.GPIO as GPIO
import time
import Pushups_mysql as pmysql

#sqlSettings
server = "localhost"
user = "root"
password = "password"

#Counter settings
autoRecord = False # Change it to False if you prefer to control it with button in the browser window, else it record exercise automatically
exerciseDelay = 4 # The time loop waits for the next push up until it register as completed exercise

#Personal config   
cpushIn = 18  # Lowest sensor position
cpushOut = 35 # Predefined, there is a need of calibration for individual person

# status pin setup
ledgreen = 21
ledred = 16
ledyellow = 20

trigPin = 24
echoPin = 23
MAX_DISTANCE = 220          #define the maximum measured distance
timeOut = MAX_DISTANCE*60   #calculate timeout according to the maximum measured distance

def pulseIn(pin,level,timeOut): # function pulseIn: obtain pulse time of a pin
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    pulseTime = (time.time() - t0)*1000000
    return pulseTime
    
def getSonar():     #get the measurement results of ultrasonic module,with unit: cm
    GPIO.output(trigPin,GPIO.HIGH)      #make trigPin send 10us high level 
    time.sleep(0.00001)     #10us
    GPIO.output(trigPin,GPIO.LOW)
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)   #read plus time of echoPin
    distance = pingTime * 340.0 / 2.0 / 10000.0     # the sound speed is 340m/s, calculating distance in cm
    return distance
    
def setup():
    print ('Program is starting...')
    #GPIO.setmode(GPIO.BOARD)       #numbers GPIOs by physical location
    GPIO.setmode(GPIO.BCM)          #number system use
    GPIO.setup(trigPin, GPIO.OUT)   #
    GPIO.setup(echoPin, GPIO.IN)    #
    GPIO.setup(ledgreen, GPIO.OUT)
    GPIO.setup(ledred, GPIO.OUT)
    GPIO.setup(ledyellow, GPIO.OUT)

# Counter wariables to detect push up actions
CpushUpsCount = 0 
IsPartial = False
IsPushIn = False
Lastupdate = time.time()

def loop(p1):
    while(True):

        distance = getSonar()
        PushPerfomed(distance)
        time.sleep(0.20)
           
def PushPerfomed(distance):
    global IsPartial
    global IsPushIn
    global CpushUpsCount
    
    global IsPersonalBest
    global Lastupdate

    if(distance <= cpushIn and distance != 0 and IsPushIn == False):
        IsPartial = True
        IsPushIn = True

        GPIO.output(ledred, GPIO.HIGH)
        print("PushIn: " + "%.2f"%(distance))
    if(IsPartial == True):
        if(distance >= cpushOut):

            CpushUpsCount += 1
            IsPartial = False
            IsPushIn = False
 
            p1.updateRecord(CpushUpsCount)
            Lastupdate = time.time()
            print("PushUP"+" Count: " +str(CpushUpsCount)+" DistanceHigh: " + "%.2f"%(distance))
            GPIO.output(ledred, GPIO.LOW)
    if(distance >= cpushOut):
        GPIO.output(ledgreen, GPIO.HIGH)
    else:
        GPIO.output(ledgreen, GPIO.LOW)            
    
    if(CpushUpsCount > 0 and time.time() > Lastupdate + exerciseDelay and autoRecord == True):
        GPIO.output(ledyellow,GPIO.HIGH)
        p1.updatePersonalBest(CpushUpsCount)
        IsPersonalBest = False
        p1.updateProgress(CpushUpsCount)
        CpushUpsCount = 0
        #print(Lastupdate)
        GPIO.output(ledyellow,GPIO.LOW)
if __name__ == '__main__':     #program start from here
    setup()
    try:
        GPIO.output(ledgreen, GPIO.LOW)
        GPIO.output(ledred, GPIO.LOW)
        GPIO.output(ledyellow, GPIO.LOW) 
        p1 = pmysql.postdata(server,user,password)
        p1.updateRecord(0)
        loop(p1)
    except KeyboardInterrupt:  #when 'Ctrl+C' is pressed, the program will exit
        GPIO.cleanup()         #release resource


    
