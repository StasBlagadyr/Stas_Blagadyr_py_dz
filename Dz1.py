# sek = 60
#min = 60-3600
#hour = 3600 - 86400
#day = 86400 - 604800
#week = 604800 - 2629743
#mounth = 2629743 - 31556926
#year = 31556926 and more
time_interval = int(input("Введите интервал в секундах: "))
if time_interval <= 60 :
    print (time_interval, "cек")
elif time_interval > 60 and time_interval <= 3600 :
    result_min = time_interval // 60
    result_sek = (time_interval % 3600) % 60
    print(result_min, "мин", result_sek, "сек")
elif time_interval > 3600 and time_interval <= 86400 :
    result_hour = time_interval // 3600
    result_min = ((time_interval % 86400) % 3600) // 60
    result_sek = ((time_interval % 86400) % 3600) % 60
    print(result_hour, "часов", result_min, "мин", result_sek, "сек")
elif time_interval > 86400 and time_interval <= 604800 :
    result_day = time_interval // 86400
    result_hour = (time_interval % 86400) // 3600
    result_min = ((time_interval % 86400) % 3600) // 60
    result_sek = ((time_interval % 86400) % 3600) % 60
    print(result_day, "дн.",result_hour, "часов", result_min, "мин", result_sek, "сек")