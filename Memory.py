import psutil


class Memory:
    def __init__(self):
        self.total = 0   # in bytes     # without swap memory
        self.total_GB = 0

        self.available = 0     # in bytes
        self.available_GB = 0

        self.percent = 0  # usage percentage

        self.update_data()

    def update_data(self):
        mem_parameters = psutil.virtual_memory()

        self.total = mem_parameters[0]   # in bytes
        self.total_GB = round(self.total / (1024 * 1024 * 1024), 2)

        self.available = mem_parameters[1]     # in bytes
        self.available_GB = round(self.available / (1024 * 1024 * 1024), 2)

        self.percent = mem_parameters[2]  # usage percentage

    def show_parameters(self):
        print("total memory = " + str(self.total_GB) + " GB")
        print("available memory = " + str(self.available_GB) + " GB")
        print("used memory: " + str(self.percent) + " %")


# TODO delete when main is done
m = Memory()
m.show_parameters()
