import Registeration as reg
import maskpass

def login():
    attempts = 0
    for user in  reg.users:
        while attempts < 3:
            email = input('Email: ').strip()
            passwd = maskpass.advpass(prompt='Password: ',ide=True).strip()
            if user['email'] != email and user['password'] != passwd:
                print('Invalid email or password')
                attempts += 1
                continue
            else:
                print('User logged in successfully')
                break

        break       


if __name__ == '__main__': 
    login()           
                