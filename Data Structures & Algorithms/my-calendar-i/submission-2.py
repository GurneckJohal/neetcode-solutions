class MyCalendar:
    
    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not startTime < endTime: return False
        has_conflict = False
        for booking in self.bookings:
            if startTime < booking[1] and booking[0] < endTime:
                return False
        self.bookings.append([startTime, endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)