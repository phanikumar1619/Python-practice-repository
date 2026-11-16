class Printer:
    def execute(self):
        print("Printing document")

class Scanner:
    def execute(self):
        print("Scanning document")

class Fax:
    def execute(self):
        print("Sending fax")




def operate_device(device):
    device.execute()


printer = Printer()
scanner = Scanner()
fax = Fax()

operate_device(printer)
operate_device(scanner)
operate_device(fax)

# a = Printer()
# b = Scanner()
# c = Fax()

# machines = [a , b , c]

# for machine in machines:
#     machine.execute()