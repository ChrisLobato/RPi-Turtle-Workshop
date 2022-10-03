import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

#Set up motors and corresponding pins
Motor1_input1 = 3    
Motor1_input2 = 6
Motor1_enable = 1    

Motor2_input1 = 3    
Motor2_input2 = 6
Motor2_enable = 1

Motor3_input1 = 14    
Motor3_input2 = 11
Motor3_enable = 9

Motor4_input1 = 13    
Motor4_input2 = 11
Motor4_enable = 9

#Set Up pins
GPIO.setup(Motor1_input1,GPIO.OUT)
GPIO.setup(Motor1_input2,GPIO.OUT)
GPIO.setup(Motor1_enable,GPIO.OUT)

GPIO.setup(Motor2_input1,GPIO.OUT)
GPIO.setup(Motor2_input2,GPIO.OUT)
GPIO.setup(Motor2_enable,GPIO.OUT)

GPIO.setup(Motor2_input1,GPIO.OUT)
GPIO.setup(Motor2_input2,GPIO.OUT)
GPIO.setup(Motor2_enable,GPIO.OUT)

GPIO.setup(Motor2_input1,GPIO.OUT)
GPIO.setup(Motor2_input2,GPIO.OUT)
GPIO.setup(Motor2_enable,GPIO.OUT)


def turn_right():
    #Rotate the Turtle to the right
    for i in range(20):
        #Front Left and Back Left Motors moves forward
        GPIO.output(Motor1_input1,GPIO.HIGH)
        GPIO.output(Motor1_input2,GPIO.LOW)
        GPIO.output(Motor1_enable,GPIO.HIGH)

        GPIO.output(Motor2_input1,GPIO.HIGH)
        GPIO.output(Motor2_input2,GPIO.LOW)
        GPIO.output(Motor2_enable,GPIO.HIGH)

        #Front Right and Back Right Motors moves back
        GPIO.output(Motor3_input2,GPIO.HIGH)
        GPIO.output(Motor3_input1,GPIO.LOW)
        GPIO.output(Motor3_enable,GPIO.HIGH)

        GPIO.output(Motor4_input2,GPIO.HIGH)
        GPIO.output(Motor4_input1,GPIO.LOW)
        GPIO.output(Motor4_enable,GPIO.HIGH)

def turn_left():
    #Rotate the Turtle to the left
    for i in range(20):
        #Front Left and Back Left Motors moves back
        GPIO.output(Motor1_input2,GPIO.HIGH)
        GPIO.output(Motor1_input1,GPIO.LOW)
        GPIO.output(Motor1_enable,GPIO.HIGH)

        GPIO.output(Motor2_input2,GPIO.HIGH)
        GPIO.output(Motor2_input1,GPIO.LOW)
        GPIO.output(Motor2_enable,GPIO.HIGH)

        #Front Right and Back Right Motors moves forward
        GPIO.output(Motor3_input1,GPIO.HIGH)
        GPIO.output(Motor3_input2,GPIO.LOW)
        GPIO.output(Motor3_enable,GPIO.HIGH)

        GPIO.output(Motor4_input1,GPIO.HIGH)
        GPIO.output(Motor4_input2,GPIO.LOW)
        GPIO.output(Motor4_enable,GPIO.HIGH)
def move_forward():
    #move Turtle Forwards
    for i in range(20):
        GPIO.output(Motor1_input1,GPIO.HIGH)
        GPIO.output(Motor1_input2,GPIO.LOW)
        GPIO.output(Motor1_enable,GPIO.HIGH)

        GPIO.output(Motor2_input1,GPIO.HIGH)
        GPIO.output(Motor2_input2,GPIO.LOW)
        GPIO.output(Motor2_enable,GPIO.HIGH)

        GPIO.output(Motor3_input1,GPIO.HIGH)
        GPIO.output(Motor3_input2,GPIO.LOW)
        GPIO.output(Motor3_enable,GPIO.HIGH)

        GPIO.output(Motor4_input1,GPIO.HIGH)
        GPIO.output(Motor4_input2,GPIO.LOW)
        GPIO.output(Motor4_enable,GPIO.HIGH)
def move_backward():
    #move Turtle BackWards
    for i in range(20):
        GPIO.output(Motor1_input2,GPIO.HIGH)
        GPIO.output(Motor1_input1,GPIO.LOW)
        GPIO.output(Motor1_enable,GPIO.HIGH)

        GPIO.output(Motor2_input2,GPIO.HIGH)
        GPIO.output(Motor2_input1,GPIO.LOW)
        GPIO.output(Motor2_enable,GPIO.HIGH)

        GPIO.output(Motor3_input2,GPIO.HIGH)
        GPIO.output(Motor3_input1,GPIO.LOW)
        GPIO.output(Motor3_enable,GPIO.HIGH)

        GPIO.output(Motor4_input2,GPIO.HIGH)
        GPIO.output(Motor4_input1,GPIO.LOW)
        GPIO.output(Motor4_enable,GPIO.HIGH)



def move(movement_type):
    if(movement_type == "Left"):
        turn_left()
    if(movement_type == "Right"):
        turn_right()
    if(movement_type == "Forward"):
        move_forward()
    if(movement_type == "Backward"):
        move_backward()
    print("Just Moved",movement_type)


def main():
    sentinel = True
    user_input = ""
    #main Loop
    while (sentinel):
        user_input = input("Select a Movement: Left, Right, Forward, Backward")
        move(user_input)
        continuePrompt = input("Continue?")
        if continuePrompt == "n":
            sentinel == False

if __name__ == "__main__": 
    main()