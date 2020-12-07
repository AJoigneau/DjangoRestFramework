This python app uses Django Rest Framework, and manipulates users with model Player and reservations with model Booking.

**Steps to run app locally**:

- Install virtual environment :
    - `python -m venv env`
    - `source env/bin/activate`

- Install librairies :
    - `pip install -r requirements.txt`

- Make migrations :
    - `python manage.py makemigrations snippets`
    - `python manage.py migrate`

- Run app :
    - `python manage.py runserver`

Then you can go to `http://localhost:8000/`

- Run unit tests :
    - `python manage.py test`


**Steps to run unit tests with Docker**:

- Build the Docker image
    - `docker build -t test_some_module -f Dockerfile .`
- Create a container instance of that image (which will run the entrypoint)
    - `docker run -it --name test_some_module test_some_module`