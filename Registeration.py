import re
import maskpass
import json

users_data_file = 'User_data.json'
users = []
def save_user_data(users):
    with open(users_data_file,'w')as file:
        json.dump(users,file)

def load_data_user():
    try:
        with open(users_data_file,'r')as file:
            return json.load(file)
    except FileNotFoundError:
        return users

def duplicted(id):
    for user in users:
        if user['user_id'] == id:
            print('Duplicated ID')
            return True
        else:
            return False
        
def register():
    mail_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    phone_pattern = r'^\+20\d{10}$'  
    while True:
        f_name = input('First name: ')
        l_name = input('Last name: ')
        try:
            user_id = int(input('User_id: '))
            duplicated_id = duplicted(user_id)
        except ValueError:
            print('ID must be integer')
            continue
        
        email = input('Email: ').strip()

        if re.match(mail_pattern,email) == None:
            valid_email = False
            print('Invalid email')
        else:
            valid_email =True

        passwd = maskpass.advpass(prompt='Password: ',ide = True).strip()
        cpasswd = maskpass.advpass(prompt='Confirm password: ',ide = True).strip()

        if passwd != cpasswd:
            valid_pass = False
            print('Passwords don\'t match')
        else:
            valid_pass = True

        phone = input('Mobile phone: ') 

        if re.match(phone_pattern,phone) == None:
            valid_phone = False 
            print('Invalid phone number') 
        else:
            valid_phone = True  

        if valid_email and valid_pass and valid_phone and not duplicated_id:
            print('User registered successfully')
            break
        else:
            print('Invalid data, please try again')
            continue
        
    user = {'user_id':user_id,
            'f_name':f_name,
            'l_name':l_name,
            'email':email,
            'password':passwd,
            'phone':phone}
    
    users.append(user)
    save_user_data(users)

users = load_data_user()
   

if __name__ == '__main__':
   register()


