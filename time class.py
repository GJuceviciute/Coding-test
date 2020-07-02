class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def scale(self, seconds):
        self.seconds += seconds
        self.minutes += self.seconds//60
        self.seconds %= 60
        self.hours += self.minutes//60
        self.minutes %= 60
        self.hours %= 24

    def timeString(self):
        Time.scale(self, 0)
        h = str(self.hours)
        m = str(self.minutes)
        s = str(self.seconds)
        if self.hours < 10:  # could use built-in string formatting to add leading 0s
            h = '0' + h
        if self.minutes < 10:
            m = '0' + m
        if self.seconds < 10:
            s = '0' + s
        return ':'.join([h, m, s])  # return h + ':' + m + ':' + s
