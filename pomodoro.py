import time
from plyer import notification
from plyer import battery



def tiempo(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1






while True:
    print("¿Empezar sesion de pomodoro? (y/n)", end="")
    opc = input()
    if opc == "y":
        "Empieza la sesion, 2 tiempos de 25 minutos"
        break

for i in range(2):
    notification.notify(
            title = "Pomodoro",
            message = "Empieza la sesion de trabajo",
            ticker = "ticker",
            timeout = 10
            #hints = {"sound-name": "alarm-clock-elapsed"}
        )
    tiempo(15) #25 minutos
    notification.notify(
            title = "Pomodoro",
            message = "Descanse",
            timeout = 10,
            #hints = {"sound-name": "alarm-clock-elapsed"}
        )
    tiempo(10) #5 minutos
