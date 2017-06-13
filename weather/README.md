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
# PLEASE NOTE : EMAIL SETTINGS
- For email functionality to work, kindly setup a sengrid (https://sendgrid.com)
- Then change the settings.py email configuration by enditing the lines having:
```
EMAIL_HOST_USER = 'username'
EMAIL_HOST_PASSWORD = 'password'
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
## Admin Operation 2 on main website and API
1. The super user can access the backend using the url below
```
localhost:8020/admin
```
2. The admin can add/change/delete new users or weather records from this interface.
3. The super user can access the weather record API via:
```
localhost:8020/weatherapp/api/create/
```
Records can be viewed, created, changed or deleted.

## Other User's Operation
1. Other users can access the backend using the url below:
```
http://localhost:8020/weatherapp/
```
2. An existing user enter his login details and click the login button to view weather records.

3. New users can directly click the register button. An email will be sent for activation.

4. The user can access the weather record API via:
```
localhost:8020/weatherapp/api/retrieve/
```
5. To view these records can also be retrieve by other python apps by including this to their code:
```
import requests
response = requests.get("http://localhost:8020/weatherapp/api/retrieve/", auth=('email address', 'password'))
print response.content
```
