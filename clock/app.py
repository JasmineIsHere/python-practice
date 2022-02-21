import sys, time
import sevseg

try:
    while True:
        ## clear screen with breaklines
        # print("\n" * 60)

        ## get current time from computer's clock
        currentTime = time.localtime()
        
        hours = str(currentTime.tm_hour % 12) #for 12-hour clock
        if hours == "0":
            hours = "12" ##00:00 will show as 12:00
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        #get digits
        hourDigits = sevseg.getSevSegStr(hours, 2)
        hourTop, hourMiddle, hourBottom = hourDigits.splitlines()

        minDigits = sevseg.getSevSegStr(minutes, 2)
        minTop, minMiddle, minBottom = minDigits.splitlines()

        secDigits = sevseg.getSevSegStr(seconds, 2)
        secTop, secMiddle, secBottom = secDigits.splitlines()

        print(hourTop," ", minTop," ", secTop)
        print(hourMiddle, "*", minMiddle, "*", secMiddle)
        print(hourBottom, "*", minBottom, "*", secBottom)

        while True:
            time.sleep(0.01) ##update every min
            if time.localtime().tm_sec != currentTime.tm_sec:
                break


except KeyboardInterrupt:
    print("CLOCK")
    sys.exit()