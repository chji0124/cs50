monlist = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    #9/8/1636 
    try:
        month, day, year = date.split("/", 2)
        if (1<= int(day) <= 31)and (1 <= int(month) <= 12):
            print(f"{year}-{int(month):02}-{int(day):02}")
        break
    
    except ValueError:
        pass
    #September 2, 1636
    try:
        month_day, year = date.split(",")
        month, day = month_day.split(" ")
        if (1 <= int(day) <= 31):
            print(f"{year}-{int(monlist.index(month)+1):02}-{int(day):02}")
        break
    
    except ValueError:
        pass


