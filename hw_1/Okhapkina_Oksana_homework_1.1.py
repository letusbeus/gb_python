# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


minute = 60
hour = minute ** 2
day = hour * 24
year = day * 365
time = input("Перед вами бомба. Что на таймере? ")
if time.isdigit():
    time = int(time)
    if time < minute:
        print("Взрыв через:", time, "сек.")
    elif minute < time < hour:
        print("Взрыв через:", time // minute, "мин.,", time % minute, "сек.")
    elif hour < time < day:
        print("Взрыв через:", time // hour, "час.,", (time % hour) // minute, "мин.,", (time % hour) % minute, "сек.")
    elif day < time < year:
        print("Взрыв через:", time // day, "дн.,", (time % day) // hour, "час.,", ((time % day) % hour) // minute, "мин.", ((time % day) % hour) % minute, "сек.")
    else:
        print("До взрыва еще есть время. Как насчет кофе?")

else:
    print("Присмотритесь получше, кажется,", str(time.upper()), "не совсем число")
