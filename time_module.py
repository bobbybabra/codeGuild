from subprocess import call
import time

def timedots():
    message = "..."
    for i in range(0,10):
        message += "..."
        call(['clear'])
        print (message)
        time.sleep(0.4)
timedots()
