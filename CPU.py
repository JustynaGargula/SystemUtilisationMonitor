import psutil


class CPU:
    def __init__(self):
        self.user_time = 0
        self.system_time = 0
        self.idle_time = 0
        self.current_freq = 0
        self.max_freq = 0
        self.percentage = 0

        self.update_data()

    def update_data(self):
        cpu_times = psutil.cpu_times()
        cpu_frequency = psutil.cpu_freq()

        self.user_time = round(cpu_times[0]/60, 2)      # converted into minutes
        self.system_time = round(cpu_times[1]/60, 2)
        self.idle_time = round(cpu_times[2]/60, 2)

        self.current_freq = cpu_frequency[0]/1000
        self.max_freq = cpu_frequency[2]/1000

        self.percentage = psutil.cpu_percent()      # has value 0
        # self.percentage = psutil.cpu_percent(interval=1)

    def show(self):
        print("current frequency = " + str(self.current_freq) + " Ghz")
        print("max frequency = " + str(self.max_freq) + " Ghz")
        self.percentage = psutil.cpu_percent(interval=1)
        print("CPU utilization percentage:  " + str(self.percentage) + " %")
        print("normal processes time: " + str(self.user_time) + " minutes")
        print("kernel mode processes time: " + str(self.system_time) + " minutes")
        print("CPU doing nothing time: " + str(self.idle_time) + " minutes")


# delete when main is done

# print(psutil.cpu_times())
# print(psutil.cpu_freq())
cpu = CPU()
cpu.show()