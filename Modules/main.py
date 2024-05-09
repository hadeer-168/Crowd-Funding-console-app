from Registeration import*
from login import*
from projects import*
import os 

print('Welcome in Crowd-Funding app')
while True:
    key = input('R: Register \nL: login ').lower()
    if key == 'r':
        register()
        os.system('cls')
        continue
    elif key == 'l':
        login()
        os.system('cls')
        while True:
            print('choose operation\n'
                'C: create new project\n'
                'E: edit project\n'
                'v: view project\n'
                'A: view all projects\n'
                'D: delete project\n'
                'S: search\n'
                'X: Exit')
            
            op_key = input().lower()
            os.system('cls')
            if op_key == 'c':
                print('Create project: ')
                create_project()
                continue
            elif op_key == 'e':
                print('Edit project: ')
                edit_project()
                continue
            elif op_key == 'v':
                print('View project: ')
                view_project()
                continue
            elif op_key == 'a':
                print('View all projects: ')
                view_all_projects()
                continue
            elif op_key == 'd':
                print('Delete project: ')
                delete_project()
                continue
            elif op_key == 's':
                print('Search: ')
                search()
                continue
            elif op_key == 'x':
                break

        break  
    else: 
        print('Try again')
       
    print('Bye')
    break      
