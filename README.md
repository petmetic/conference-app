This is a Conference App that helps you keep track of conference attendees and their arrivals to the conference. It
sends a daily email with a list of new attendees and the total number of them.

## Getting started

1. First, clone or fork the repo (SSH).
   ```git clone git@bitbucket.org:conference-app/backend.git```


2. Navigate to `backend` folder. Install the virtual environment:
   ```python3.11 -m venv venv```

3. Activate the virtual environment:
   ```. venv/bin/activate```

4. In the project folder of the application, install the requirements

   ```pip install -r requirements.txt```

5. Copy `localsettings.py` to `src/conferenceapp` folder (next to `settings.py`).


6. Create database: go to the `src` folder in project and run

   ```./manage.py migrate```

7. Create admin superuser for `Admin view`. Run command and follow the prompts:

   ```./manage.py createsuperuser```

8. For the application to work fully, install `Redis` on your computer:

   Go to `https://redis.io/docs/install/install-redis/` for instructions on how to install and test if installation is
   working

## How to run application

To run the application, using the Celery email scheduling for reporting, you have to have 4 different processes running
at the same time: the `Redis server`, `Celery worker`, `Celery beat` and the `Django application`.

1. Go to `backend` and activate `virtual env`(see Getting started - bullet no. 3) and start `Redis server` in new tab in
terminal:

   ``````redis-server``````

2. Run `Celery worker` in `src` folder different tab in terminal (before heading to `src` folder, don't forget to
activate `virtual env`):

   ```celery -A conferenceapp worker -l INFO --without-gossip --without-mingle -Ofair --pool=solo```

3. Run `Celery beat` in `src` folder in another tab in terminal:

   ```celery -A conferenceapp  beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler```

4. To run the application locally, in your `src` folder, enter in terminal:

   ```./manage.py runserver```

5. Go to `http://127.0.0.1:8000` to see the site.

## How to use

The application is easy to use. You got to `http://127.0.0.1:8000` and `sign up` or `log in`. After that you are
directed to the `home` page.
In the navbar you have a choice of `add attendee`, `attendee list`, `add arrival` and `arrival list`.

In the `add attendee`: There is a form to fill out with the mandatory name, surname, date of birth and ticket id.

`Attendee list` Gives you a list of all the attendees in the conference. You can get a `detailed view of attendee` if
clicking on `view` button.

In the `detailed view of attendee` you can also edit the information provided.

You can add an arrival of attendee in the `add arrival` tab: Choose an attendee from a dropdown list and choose time of
arrival and click the `submit` button.

In the `arrival list` tab you can search the list by name, surname, or time of arrival. By clicking the`view` button,
you can see the details of attendee.

There is also an API integration for processing arrivals and attendees.

### Administration page

If you got to `http://127.0.0.1:8000/admin/` and log in,

you can see the `Site administration` page, where you can `add`,`edit` and `delete` Arrivals and Attendees databases in
the `WEB` section.
Once in those tabs, you can search through the database using Name, Surname, Ticket ID number and date of arrival,
depending on which tab you are in (check the help text under search bar for more info).

## How to test the application

To run the test, go to the `src` folder and run:

```./manage.py test```




