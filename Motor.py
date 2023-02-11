import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

#Set up motors and corresponding pins
Motor1_input1 = 5    
Motor1_input2 = 3
Motor1_enable = 7    
print()
Motor2_input1 = 35    
Motor2_input2 = 33
Motor2_enable = 37

Motor3_input1 = 10    
Motor3_input2 = 12
Motor3_enable = 8

Motor4_input1 = 38    
Motor4_input2 = 40
Motor4_enable = 36

#Set Up pins
GPIO.setup(Motor1_input1,GPIO.OUT)
GPIO.setup(Motor1_input2,GPIO.OUT)
GPIO.setup(Motor1_enable,GPIO.OUT)

GPIO.setup(Motor2_input1,GPIO.OUT)
GPIO.setup(Motor2_input2,GPIO.OUT)
GPIO.setup(Motor2_enable,GPIO.OUT)

GPIO.setup(Motor3_input1,GPIO.OUT)
GPIO.setup(Motor3_input2,GPIO.OUT)
GPIO.setup(Motor3_enable,GPIO.OUT)

GPIO.setup(Motor4_input1,GPIO.OUT)
GPIO.setup(Motor4_input2,GPIO.OUT)
GPIO.setup(Motor4_enable,GPIO.OUT)

GPIO.output(Motor1_input1,GPIO.LOW)
GPIO.output(Motor1_input2,GPIO.LOW)
GPIO.output(Motor1_enable,GPIO.LOW)

GPIO.output(Motor2_input1,GPIO.LOW)
GPIO.output(Motor2_input2,GPIO.LOW)
GPIO.output(Motor2_enable,GPIO.LOW)

GPIO.output(Motor3_input1,GPIO.LOW)
GPIO.output(Motor3_input2,GPIO.LOW)
GPIO.output(Motor3_enable,GPIO.LOW)

GPIO.output(Motor4_input1,GPIO.LOW)
GPIO.output(Motor4_input2,GPIO.LOW)
GPIO.output(Motor4_enable,GPIO.LOW)

def reset():
    GPIO.output(Motor1_input1,GPIO.LOW)
    GPIO.output(Motor1_input2,GPIO.LOW)
    GPIO.output(Motor1_enable,GPIO.LOW)

    GPIO.output(Motor2_input1,GPIO.LOW)
    GPIO.output(Motor2_input2,GPIO.LOW)
    GPIO.output(Motor2_enable,GPIO.LOW)

    GPIO.output(Motor3_input1,GPIO.LOW)
    GPIO.output(Motor3_input2,GPIO.LOW)
    GPIO.output(Motor3_enable,GPIO.LOW)

    GPIO.output(Motor4_input1,GPIO.LOW)
    GPIO.output(Motor4_input2,GPIO.LOW)
    GPIO.output(Motor4_enable,GPIO.LOW)




def turn_right(timeRunning,delay):
    #Rotate the Turtle to the right
        #Front Left and Back Left Motors moves forward
    #reset()
    delay = delay/100
    timeRunning *= 5
    #sleeps are so that we can add a delay and this is what causes the pulse width modulation
    #this makes it go slower
    for i in range(timeRunning):
        GPIO.output(Motor1_input2,GPIO.HIGH)
        GPIO.output(Motor1_enable,GPIO.HIGH)
        GPIO.output(Motor2_input2,GPIO.HIGH)
        GPIO.output(Motor2_enable,GPIO.HIGH)
        GPIO.output(Motor3_input1,GPIO.HIGH)
        GPIO.output(Motor3_enable,GPIO.HIGH)
        GPIO.output(Motor4_input1,GPIO.HIGH)
        GPIO.output(Motor4_enable,GPIO.HIGH)
        sleep(0.075*delay) # have to change the way the delays work
        #Sets Everything to LOW/OFF
        reset() 
        sleep(0.075*(1-delay)) # Have to change the way the delays work
        
    
    
def turn_left(timeRunning,delay):
    #Rotate the Turtle to the left
    #Front Left and Back Left Motors moves back
    #reset()
    timeRunning *= 10
    delay = delay/100
    for i in range(timeRunning):
        GPIO.output(Motor1_input1,GPIO.HIGH)
        GPIO.output(Motor1_enable,GPIO.HIGH)
        GPIO.output(Motor2_input1,GPIO.HIGH)
        GPIO.output(Motor2_enable,GPIO.HIGH)
        GPIO.output(Motor3_input2,GPIO.HIGH)
        GPIO.output(Motor3_enable,GPIO.HIGH)
        GPIO.output(Motor4_input2,GPIO.HIGH)
        GPIO.output(Motor4_enable,GPIO.HIGH)
        sleep(0.075*delay)
        reset()
        sleep(0.075*(1-delay))

def move_forward(timeRunning,delay):
    #move Turtle Forwards
    # reset(distane)
    timeRunning *= 10
    delay = delay/100
    for i in range (timeRunning):
        #print(i)    
        GPIO.output(Motor1_input1,GPIO.HIGH)
        GPIO.output(Motor1_enable,GPIO.HIGH)
        GPIO.output(Motor2_input1,GPIO.HIGH)
        GPIO.output(Motor2_enable,GPIO.HIGH)
        GPIO.output(Motor3_input1,GPIO.HIGH)
        GPIO.output(Motor3_enable,GPIO.HIGH)
        GPIO.output(Motor4_input1,GPIO.HIGH)
        GPIO.output(Motor4_enable,GPIO.HIGH)
        sleep(0.075*delay)
        reset()
        sleep(0.075*(1-delay))
def move_backward(timeRunning,delay):
    #move Turtle BackWards
    #reset()
    timeRunning *= 10
    delay = delay/100
    for i in range(timeRunning):        
        GPIO.output(Motor1_input2,GPIO.HIGH)
        GPIO.output(Motor1_enable,GPIO.HIGH)
        GPIO.output(Motor2_input2,GPIO.HIGH)
        GPIO.output(Motor2_enable,GPIO.HIGH)
        GPIO.output(Motor3_input2,GPIO.HIGH)
        GPIO.output(Motor3_enable,GPIO.HIGH)
        GPIO.output(Motor4_input2,GPIO.HIGH)
        GPIO.output(Motor4_enable,GPIO.HIGH)
        sleep(0.075*delay)        
        reset()
        sleep(0.075*(1-delay))
        
     #Im not sure if this works or caused errors at some point but this way it might
    #be more visible to see the changes from the movements as it completes one action and moves to the next
def move(movement_type,timeRunning=0,delay=0):
    if(movement_type == "Left"):
        #continue_sentinel = True
        turn_left(timeRunning,delay)
        print("Turning Left")
    #     StopPromt = input("Stop?")
    #     if (StopPromt == False):
    #         reset()
    if(movement_type == "Right"):
        turn_right(timeRunning,delay)
        print("Turn Right")
        # StopPromt = input("Stop?")
        # if (StopPromt == False):
        #     reset()
    if(movement_type == "Forward"):
        move_forward(timeRunning,delay)
        print("Moving Forward")
        # StopPromt = input("Stop?")
        # if (StopPromt == False):
        #     reset()
    if(movement_type == "Backward"):
        move_backward(timeRunning,delay)
        print("Moving Backward")
        # StopPromt = input("Stop?")
        # if (StopPromt == False):
        #     reset()
    if (movement_type == "Stop"):
        reset()  
    #print("Just Moved")


def main():
    user_input = ""
    #main Loop
    listOfMovements = [] #this is where we are going to store the movements like transactions
    #While loop keeps adding movements until we have finished adding movements via Stop movement
    while (user_input!="Stop"):
        user_input = input("Select a Movement: Left, Right, Forward, Backward or Stop\nFormat for input: 'MovementType TimeRunning/Loop DelayPercent'\n")
        if(user_input[:4]!= "Stop"):
            user_input = user_input.split()
            listOfMovements.append((move,user_input[0],int(user_input[1]),int(user_input[2]))) # should split the list into all the different arguments
        else:
            listOfMovements.append((move,"Stop")) # this is where we would end the loop
    #This will go through the list of transactions that we just created and will call them one at a time
    for movement in listOfMovements:
        movement[0](*movement[1:])
    reset()

if __name__ == "__main__": 
    main()