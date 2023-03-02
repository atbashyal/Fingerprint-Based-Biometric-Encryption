class info:
    def __init__(self):
        self.name = input("Enter the name")
        self.phone = input("Enter the phone")
        self.email = input("Enter the email")
        self.token = "This is our ISAA project"

class enc:
    def __init__(self,person,key):
        fernet = Fernet(key)
        self.name = fernet.encrypt(person.name.encode())
        self.phone = fernet.encrypt(person.phone.encode())
        self.email = fernet.encrypt(person.email.encode())
        self.token = fernet.encrypt(person.token.encode())
        print(self.name)
        print(self.phone)
        print(self.email)
        print(self.token)

class dec:
    def __init__(self,person_enc,key):
        fernet = Fernet(key)
        try:
        self.token = fernet.decrypt(person_enc.token).decode()
        print("Fingerprint matched !")
        except:
        print("Fingerprint not matched !")