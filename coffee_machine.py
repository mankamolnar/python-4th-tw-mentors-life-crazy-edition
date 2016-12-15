class Coffee_machine:

    def __init__(self):
        self.price = 1
        self.on = False
        self.filled_beans = False
        self.coffees_poured = 0

    def turn_on(self):
        self.on = True
        print("Hi I'm Tivadar the cofee machine. You have successfully turned me on ;)")

    def fill_beans(self):
        self.filled_beans = True
        print("You have successfully filled me with coffee beans!")

    def pour_coffee(self):

        if not self.on:
            raise offMachineError

        elif not self.filled_beans:
            raise noBeansError

        else:
            self.coffees_poured += 1
            self.check_empty_beans()
            print("The coffee has been poured out! Drink responsibly!")

    def check_empty_beans(self):
        if self.coffees_poured == 10:
            self.coffees_poured = 0
            self.filled_beans = False
            print("The coffee beans tank is empty!")


class noBeansError(Exception):
    pass


class offMachineError(Exception):
    pass
