# Weather App Application and API
## Setting up environment for this project
1. This project was built using python 2.7.13.

2. Ensure python and virtual environment are installed. Switch to the virtual environment.

3. The packages in the requirements.txt file should be installed.
```
pip install -r requirements.txt
```
4. As this is a mini application, SQLite Database was used.

5. open a terminal and clone the repository as follows:
```
git clone https://github.com/popsonebz/weatherApp.git
```
This creates a folder called weatherApp in the current directory.

6. switch to that directory

```
cd weatherApp/weather
```
7. To create the database and tables, run the migration command
```
python manage.py makemigrations
python manage.py migrate
```

8. Create a super user who serves as the admin. It's gonna request for email and password
```
python manage.py createsuperuser
``` 
## Admin Operation 1
### Populating the database from remote api using management command
Run the code below:
```
 python manage.py import_weather
```
9. We can now startup the server
```
python manage.py runserver localhost:8020
```
## Admin Operation 2
1. The super user can access the backend using the url below
```
localhost:8020/admin
```
2. The admin can add/change/delete new users or weather records from this interface.

## Employee Operation

1. To apply for leave, the employee visits this url

<http://localhost:8010/leave/apply>

2. He/She is redirected to the login page for authentication

3. If Authentication is successful, the application page is displayed.

4. On selecting the start and end dates, the following are checked:

- Both either start or end date or end date cannot be less than the current date.
- The end date cannot be less than the start date.
- Start date cannot later than end date.
- End date cannot be the same as start date.
- Notify the user when there is no working days within the specified period.
- Preventing duration which exceeds the maximum 18 days of leave allocated.

### Automatically Decline the following leave application:

- Employees who have not spent up to 3 months in the company from appying for leave.
- Employee who has exhausted his leave.
- Employee taking more than the remaining leave days he has.

## Selenium Functional Test

Note: To use the functional test, the following needs to be done:
1. Chrome webdriver needs to be downloaden and placed into the folder path (tanget_leave_app_solution/leave/)

2. The webdriver path needs to be set accordingly as seen in leave/test.py (the current path only works on my laptop).

3. Open the link <http://localhost:8010/admin/add-employee/>

4. Create the following users:
```
first name = kate, last name = perry, employment date = 01/01/2017, username = kate, password= kate

```
```
first name = ben, last name = carson, employment date = 29/05/2017, username = ben, password= ben

```

3. Then run the command:
```
   python manage.py test
```

## Carrying Over Leave Not Taken

The system carry's over a maximum of 5 days leave.

This is done in the management command defined in leave/management/commands/carry_leave_over_the_year.py

The operation can be carried out in 2 ways:

1. Manually at the end of the year
```
   python manage.py carry_leave_over_the_year
```
2. Automatically by creating a linux crontab job which executes once a day to check if its the last day of the year.

if the condition is met, the command in option 1  will be executed.