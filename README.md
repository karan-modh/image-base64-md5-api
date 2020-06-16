# image-base64-md5-api
An API to convert Image to base64 and to md5 hash

It takes image as a form-data (i.e. enctype = 'multipart/form-data') and returns the JSON response of its base64 version and MD5 hash applied on it.

## To test and use.
Navigate to https://image-base64-md5-api.herokuapp.com/ and there will be a form to insert image and get a response
OR one can make a direct POST request with image file as form-data to https://image-base64-md5-api.herokuapp.com/api 

#### Procedure to setup and run:
- Navigate to cloned repository
```shell script
cd <project_directory>    # In this case image-base64-md5-api
```
- Setup Virtual Environment and activate it
```shell script
python3 -m venv env
source env/bin/activate
```
- Use Pip to install all dependencies
```shell script
pip install -r requirements.txt
```
- Make database Migrations
```shell script
python3 manage.py makemigrations
python3 manage.py migrate
```
- Create SuperUser to access admin panel (#Optional - Not necessary in this project but you can)
```shell script
python3 manage.py createsuperuser
```
- Finally, run a development server
```shell script
python3 manage.py runserver
```
- That's it, Api is ready to use in local environment

`
Note: There are 2 branches 'master' and 'django-heroku'. 'master' is for development purposes and 'django-heroku' is for deployment and hence has some extra dependencies which needs to be installed.
` 
