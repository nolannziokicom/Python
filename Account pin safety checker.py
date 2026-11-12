
class Account:
 
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin   

    def show_pin_status(self):
        print("Account Owner:", self.owner)
        print("PIN is safely stored inside the class.")
 

    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated successfully.")
        else:
            print("Invalid PIN. PIN must be exactly 4 digits.")
 

    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("Access granted.")
        else:
            print("Access denied.")

bus=Account("Nolan",2024)
 







        