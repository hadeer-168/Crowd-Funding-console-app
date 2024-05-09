from datetime import datetime
import json

project_Data_file = 'project_data.json'
projects = []

def save_project_data(projects):
    with open(project_Data_file,'w')as file:
        json.dump(projects,file)


def load_project_data():
    with open(project_Data_file,'r')as file:
        try:
            return json.load(file)
        except FileNotFoundError:
            return projects
        

def create_project():
    while True:
        try:
            user_id = int(input('User_id: '))
            break
        except ValueError:
            print('ID must be a number, please try again')
            continue

    Title = input('Title: ')
    details = input('Details: ')    

    while True:
        try:
            target = float(input('Target: '))
            break
        except ValueError:
            print('Target must be a number, please try again')
            continue
      

    while True:    
        start_date = input('Start_Date(M-D-Y H:M): ')   
        end_date = input('End_Date(M-D-Y H:M): ')      

        try:
            start = datetime.strptime(start_date,'%m-%d-%Y %H:%M')
            end = datetime.strptime(end_date,'%m-%d-%Y %H:%M')   
            if start >= end :
                print('Start date must come before end date')
                continue

        except ValueError:
            print('Date must be in format Month-day-Year Hours:minutes')
            continue
        else:
            
            break  
      

    project_data={'user_id':user_id,
                  'title':Title,
                  'details':details,
                  'target':target ,
                  'start_date':start_date,
                  'end_date':end_date
                  }
    
    projects.append(project_data)
    save_project_data(projects)

projects = load_project_data()

def view_all_projects():
    for project in projects:
        print(project)

def view_project():
    while True:
        try:
            user_id = int(input('Enter ID: ')) 
            break
        except ValueError:
            print('ID must be a number, please try again')
            continue

    for project in projects:
        if project['user_id'] == user_id:
            print('Project found:')
            print(project)
        else:
            print('Project Not found')

def edit_project():
    while True:
        try:
            user_id = int(input('Enter your ID: ')) 
            break
        except ValueError:
            print('ID must be a number, please try again')
            continue

    for project in projects:
        items = project.keys()
        if project['user_id'] == user_id:
            print('Project found')
            item = input('item you wanna change: ')
            if item in items:
                value = input('New change: ')
                project[item] = value
            else:
                print('Item Not found , try again')
                continue

        else:
            print('Project Not found')

    save_project_data(projects)

def search():
    item = input('Search by: ')
    for project in projects:
        items = project.keys()
        data = project.values()
        if item in items:
          targeted_data = input('Search for: ')
          if targeted_data in data:
              print(project)
          else:
              print('Unvailable data')
        else:
            print('Unvailable data')

def delete_project():
    while True:
        try:
            user_id = int(input('Enter your ID: ')) 
            break
        except ValueError:
            print('ID must be a number, please try again')
            continue

    for project in projects:
        if project['user_id'] == user_id:
            projects.remove(project)
            save_project_data(projects) 
            print('Project deleted successfully')
        else:
            print('Not allowed')  
            
   
if __name__ =='__main__':
  view_project()