def time_calculator(time):
    x = 0
    for i in time: #count total data
        x = x + 1
    
    if x == 2: #filter data without "day" data
        time1 = time[0]
        hour1, xt = time1.split(":") 
        minute1, meridiem = xt.split(" ")
        time2 = time[1]
        hour2, minute2 = time2.split(":")

        if meridiem =="PM": #add 12 to time if it's PM
            hour1 = int(hour1) + 12

        totalhourtime = int(hour1) + int(hour2) #count time
        totalminutetime = int(minute1) + int(minute2) #count minute

        addhour = 0
        if totalminutetime > 59:    #convert excess minute to hour
            totalminutetime = totalminutetime % 60
            addhour = 1
        hour = totalhourtime + addhour 

        countday = int(hour/24) 
        if countday == 0:   #count elapsed day
            countday = "Today"
        elif countday == 1:
            countday = "Next day"
        elif countday > 1:
            countday = str(countday)+" days later"
        
        if hour > 23:   #confert back excess hour
            hour = hour % 24
        
        if hour > 11:   #determind AM or PM
            meridiem = "PM"
            if hour > 12:
                hour = hour - 12
        else:
            meridiem = "AM"
        
        if totalminutetime < 10: #give 0 if under 10 minutes example: 8 minutes to 08 minutes
            totalminutetime = "0" + str(totalminutetime)

        print(str(hour)+":"+str(totalminutetime),meridiem,"("+countday+")") 

    if x == 3: #filter data without "day" data
        time1 = time[0]
        hour1, xt = time1.split(":") 
        minute1, meridiem = xt.split(" ")
        time2 = time[1]
        hour2, minute2 = time2.split(":")
        day = time[2]

        if meridiem =="PM": #add 12 to time if it's PM
            hour1 = int(hour1) + 12

        totalhourtime = int(hour1) + int(hour2) #count total hour
        totalminutetime = int(minute1) + int(minute2) #count total minutes

        addhour = 0
        if totalminutetime > 59:    #convert excess minute to hour
            totalminutetime = totalminutetime % 60
            addhour = 1
        hour = totalhourtime + addhour
        countday = int(hour/24)
        if countday == 0: #count elapsed day
            dayelapsed = "Today"
        elif countday == 1:
            dayelapsed = "Next day"
        elif countday > 1:
            dayelapsed = str(countday)+" days later"
        
        
        if hour > 23: #confert back excess hour
            hour = hour % 24
        
        if hour > 11: #determind PM or AM
            meridiem = "PM"
            if hour > 12:
                hour = hour - 12
        else:
            meridiem = "AM"
        
        if totalminutetime < 10: #give 0 if under 10 minutes example: 8 minutes to 08 minutes
            totalminutetime = "0" + str(totalminutetime)
        

        if day == "Monday": #declare point for each day
            daycount = 1
        elif day == "Tuesday":
            daycount = 2
        elif day == "Wednesday":
            daycount = 3
        elif day == "Thursday":
            daycount = 4
        elif day == "Friday":
            daycount = 5
        elif day == "Saturday":
            daycount = 6
        elif day == "Sunday":
            daycount = 7

        countday = countday + daycount #point after convertion
        if countday > 7: #confert back excess point
            countday = countday % 7
        if countday == 1: #decide what day based on point
            day = "Monday"
        elif countday == 2:
            day = "Tuesday"
        elif countday == 3:
            day = "Wednesday"
        elif countday == 4:
            day = "Thursday"
        elif countday == 5:
            day = "Friday"
        elif countday == 6:
            day = "Saturday"
        elif countday == 7:
            day = "Sunday"
        
        print(str(hour)+":"+str(totalminutetime),meridiem+",",day,"("+dayelapsed+")")