import psutil


class Process:
    def __init__(self, pid):
        self.pid = pid

    def update_data(self):
        pass

    def show(self):
        process_found = False
        for proc in psutil.process_iter(['pid', 'name', 'username', 'status']):
            if proc.pid == self.pid:
                print(proc.info)
                process_found = True
                break
        if not process_found:
            print("Process with ID "+str(self.pid)+" doesn't exist.")

    @staticmethod
    def get_pids():
        return psutil.pids()


Process.get_pids()
print(psutil.pids())

# TODO delete when main is done
p = Process(424)
p.show()
