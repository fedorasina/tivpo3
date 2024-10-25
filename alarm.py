import datetime
import time
import playsound

def alarm(alarm_time):
    try:
        alarm_datetime = datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        now = datetime.datetime.now()
        print(str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        if alarm_datetime.hour <= now.hour and alarm_datetime.minute <= now.minute and alarm_datetime.second <= now.second:
          print("Время будильника должно быть в будущем.")
          return False

        melodies = ["melody1.mp3", "melody2.mp3", "melody3.mp3"]

        melody_index = int(input(f"Выберите мелодию (1 - {len(melodies)}): "))
        if melody_index < 0 or melody_index >= len(melodies):
          print("Неверный номер мелодии.")
          return False

        while True:
            current_time = datetime.datetime.now()
            if current_time.hour == alarm_datetime.hour and \
               current_time.minute == alarm_datetime.minute and \
               current_time.second == alarm_datetime.second:
                print("Время будильника!")
                playsound.playsound(melodies[melody_index - 1])
                break
            time.sleep(1)
        return True

    except ValueError:
        print("Неверный формат времени. Введите время в формате HH:MM:SS.")
        return False

if __name__ == "__main__":
    while True:
        alarm_time = input("Введите время будильника в формате HH:MM:SS: ")
        if alarm(alarm_time):
            break