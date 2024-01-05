import psutil


class Disk:
    def __init__(self, path):
        self.no_error = False
        self.path = path
        self.total = 0
        self.used = 0
        self.free = 0
        self.percentage = 0
        self.update_data()

    @staticmethod
    def get_available_discs():
        disk_paths = []
        discs = psutil.disk_partitions(False)
        for disc in discs:
            disk_paths.append(disc[0])
        return disk_paths

    def update_data(self):
        try:
            data = psutil.disk_usage(self.path)  # contains data in bytes and percentage
            self.total = round(data[0] / (1024 * 1024 * 1024), 2)  # converted to GB
            self.used = round(data[1] / (1024 * 1024 * 1024), 2)
            self.free = round(data[2] / (1024 * 1024 * 1024), 2)
            self.percentage = data[3]
            self.no_error = True
        except PermissionError:
            pass

    def show(self):
        if self.no_error:
            print("\nDisplaying information about disk " + self.path)
            print("Total disk partition capacity: ", self.total, "GB")
            print("Used disk partition capacity: ", self.used, "GB")
            print("Free disk partition capacity: ", self.free, "GB")
            print("Percentage of used disk partition capacity: ", self.percentage, "%")
        else:
            print("\nCouldn't load data about disc " + self.path)


# it may be useful in main
for disk_path in Disk.get_available_discs():
    print(disk_path)

# TODO delete when main is done
for disk_path in Disk.get_available_discs():
    d = Disk(disk_path)
    d.show()
# print(psutil.disk_usage('/'))
# print(psutil.disk_partitions())
