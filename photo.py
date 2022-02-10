
import pyb, machine, sensor, image, pyb, os, time

def photo():
  sensor.reset() #Initialize the sensor.
  sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
  sensor.set_framesize(sensor.WQXGA2) # Set frame size to WQXGA2(2592x1944)
  sensor.skip_frames(time = 3000)     # Wait for settings take effect
  rtc = pyb.RTC() #RTC refers to the independent real time clock that keeps track of the date and time.
  newFile = False
  try:
     os.stat('list.txt')
  except OSError:
     #If the "list.txt" does not exist, then set RTC and set newFile's time. This document is used to record time.
     #Year, Month, Day, Weekdays(Mon=1,Sun=7), Hours(24h), Min, Sec, subSec
     rtc.datetime((2022, 1, 17, 1, 10, 0, 0, 0))
     newFile = True
  #Get time information from RTC object
  dateTime = rtc.datetime()
  year = str(dateTime[0])
  month = '%02d' % dateTime[1]
  day = '%02d' % dateTime[2]
  hour = '%02d' % dateTime[4]
  minute = '%02d' % dateTime[5]
  second = '%02d' % dateTime[6]
  subSecond = str(dateTime[7])
  newName='I'+year+month+day+hour+minute+second+'.jpg'
  #Naming the picture file based on time.
  #rtc.wakeup(10000) wake up every 10 sec
  BLUE_LED_PIN = 3
  #let us know that the camera is going to take a picture
  pyb.LED(BLUE_LED_PIN).on()
  if(newFile):
     #Edit list to record date, time, picture's name
     with open('list.txt', 'a') as timeFile:
        timeFile.write('Date and time format: year, month, day, hours, minutes, seconds, subseconds' + '\n')
        timeFile.write(newName + ',' + year + ',' + month +  ',' + day +  ',' + hour +  ',' + minute +  ',' + second +  ',' + subSecond + '\n')
  else:
     with open('list.txt', 'a') as timeFile:
        timeFile.write(newName + ',' + year + ',' + month +  ',' + day +  ',' + hour +  ',' + minute +  ',' + second +  ',' + subSecond + '\n')
  if not "images" in os.listdir(): os.mkdir("images")
  #take picture and save to the MicroSD card
  img = sensor.snapshot()
  img.save('images/' + newName)
  pyb.LED(BLUE_LED_PIN).off()


#The TimeLapse function is used to take picture every t secound.
def TimeLapse(t, n):
    i = 0
    while i != n:
      photo()
      i = 1+i
    machine.deepsleep()


