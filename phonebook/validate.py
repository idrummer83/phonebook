
class Validate:
    def check_name(self):
        self.name = input('name: ')
        while len(self.name) < 3:
            self.name = input('minimal 3 letters, please type name: ')
        return self.name

    def check_phone(self):
        self.phone = input('phone: ')
        while len(self.phone) < 6:
            self.phone = input('minimal 6 numbers, please type phone: ')
        return self.phone
