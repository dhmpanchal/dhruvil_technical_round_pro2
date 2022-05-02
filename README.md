# Follow the bellow steps to run project

1. clone the repository.
2. create a new virtual environment with name of env (python -m venv env)
3. activate the virtual environment (Windows: .\env\Scripts\activate or Linux/MAC os: source env/bin/activate)
4. install requirements from the requirements.txt file (pip install -r requirements.txt)
5. migrate the database
    1. python manage.py makemigrations
    2. python manage.py migrate
6. run the project by running the following command python manage.py runserver
7. test the apis on postman. (you can find demo api postman collection in project directory.)
