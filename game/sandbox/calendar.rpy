init python:
    class Calander(object):
        def __init__(self, weekdays, months, days_per_month, hours, minutes, month, days, total_days):
            self.weekdays = weekdays
            self.months = months
            self.days_per_month = days_per_month
            self.hours = hours
            self.minutes = minutes
            self.month = month
            self.days = days
            self.total_days = total_days

        @property
        def DaT(self):
            return self.weekdays[self.total_days % 7] + ", " + str(self.days + 1) + ", " + self.months[self.month % 12] + " " + str(self.hours).zfill(2) + ":" + str(self.minutes).zfill(2)

        def addTimeInHours(self, hours):
            self.hours += hours
            if self.hours >= 24:
                self.days += self.hours // 24
                self.total_days += self.hours // 24
                self.hours = self.hours % 24
            if self.days >= self.days_per_month[self.month % 12]:
                temp = self.month
                self.month += self.days // self.days_per_month[temp % 12]
                self.days = self.days % self.days_per_month[temp % 12]

        def addTimeInMinutes(self, minutes):
            self.minutes += minutes
            if self.minutes >= 60:
                self.hours += self.minutes // 60
                self.minutes = self.minutes % 60
            if self.hours >= 24:
                self.days += self.hours // 24
                self.total_days += self.hours // 24
                self.hours = self.hours % 24
            if self.days >= self.days_per_month[self.month % 12]:
                temp = self.month
                self.month += self.days // self.days_per_month[temp % 12]
                self.days = self.days % self.days_per_month[temp % 12]

        def addTimeInDays(self, days):
            self.days += days
            self.total_days += days
            if self.days >= self.days_per_month[self.month % 12]:
                temp = self.month
                self.month += self.days // self.days_per_month[temp % 12]
                self.days = self.days % self.days_per_month[temp % 12]

    default_weekdays = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    default_months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    default_days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    calendar = Calander(default_weekdays, default_months, default_days_per_month, hours=8, minutes=0, month=0, days=0, total_days=0)

    def advance_hours(hours):
        calendar.addTimeInHours(hours)

    def advance_minutes(minutes):
        calendar.addTimeInMinutes(minutes)

    def advance_days(days):
        calendar.addTimeInDays(days)

    def set_day(day):
        calendar.days = day
        
        # Recalculate total_days by summing days from all previous months
        total_days = 0
        for i in range(calendar.month):
            total_days += calendar.days_per_month[i % 12]
        total_days += calendar.days
        calendar.total_days = total_days

    def set_hour(hour):
        calendar.hours = hour

    def set_minute(minute):
        calendar.minutes = minute