import time

class Clock:
    
    @staticmethod
    def clock():
        # get the current time
        current_time = time.strftime("%I:%M %p")
        # get the current date
        current_date = time.strftime("%d/%m/%Y")

        # print the time and date
        print("\n     Time:", current_time)
        print("     Date:", current_date)


if __name__ == '__main__':
	c = Clock()
	c.clock()
