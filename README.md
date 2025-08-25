# Property Estimate Take Home Assignment by Eshwar Tangirala

## Core Features

User can submit a form and have an AI assistant generate, cash flow, revenue, and cost based off of address and property size.

## Setup Instructions and Command Configurations

Since this project runs in a docker container, the commands to run tests, install packages, and use the app will all need to be run in the container. I put the Django application in a Server directory. I had scalability in mind in case the project might ever have a client folder to have a front end.

#### 1) Clone the repository

Run

```bash
git clone git@github.com:Eshwar1212-maker/property-estimate.git
```

and cd into the right directory.

### 2) Get your ENV variables

The only thing you will have to adjust is get your own API key from https://platform.openai.com/api-keys to use GPT's model.

```bash
DEBUG=1
SECRET_KEY=n3u4hx!5z%a3z3@7t*m1&6&m+2b@w67w
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
OPENAI_API_KEY=your-key-here
```

#### 3) Build and start the containers

Start by running the container with:
```bash
docker compose up --build
```

#### 4) Open a new terminal, and run the migrations with:

```bash
docker compose exec web python manage.py migrate
```

#### 5) Create a superuser with:

```bash
docker compose exec web python manage.py createsuperuser
```

(Optional) Tests

```bash
docker compose exec web pytest
```

Also, I used black and flake8 for overall cleanliness and formatting. Run these commands to ensure code is formatted, has less style errors and bugs"

```bash
docker compose exec web black .
docker compose exec web flake8 /code
```

After this, you should see the form on localhost:8000, submit the form, and it will take you the the properties page!

## Common issues during development

Bugs are very common during development for any application. A few common issues that are faced when I was reinstalling the application and cloning my repository had to do with migrations, volume conflicts CSRF token issues. If you run into any bugs, I would recommend following these next steps.

Clear your browsers cache, and then run:

```bash
docker compose down -v

docker compose up --build

docker compose exec web python manage.py migrate

```
and then restart from step three.

## Assumptions made

Here are some assumptions I made which explain the choices I used for certain technologies or paradigms:

-I used Django Templates for the front end. Since you guys said that right now you're only using Tailwind CSS with HTML. I thought that this would be the simplest approach to build the template with the Django application instead of creating a separate folder just with HTML/CSS in them.

## Potential Improvements with more time

-Creating an 'apps' directory and putting estimates inside of that folder, instead of having the estimates folder be there by itself just for future scalability.

-UI/UX styling, and responsiveness. If i had more than the 4 hour mark. I would have made the website look a little more user friendly, and styled and similar to the Figma designs.

-Since you guys said that right now you're using HTML and CSS I was thinking that further improvements would be separating the front end into a different folder, potentially using React if this project scales.

-For this project think I could've removed the server folder and just kept the project in end of itself. I'm realizing that it's because the HTML/CSS live inside of the Django app maybe the server folder can be misleading.

-Add better validation on the form. For example, ensure that maybe only correct real addresses that only exist are allowed to get submitted. Also I render the raw Python exception ({{ error }}) back to the user. In production this could leak stack traces or internal info.

-AI model accuracy. Right now since I'm on the free plan of open AI I didn't have an opportunity to test that many times to get an accurate/precise model. I think the estimations could be more accurate.

Overall, I had a blast working on the project. I would love to talk further about potential improvements if you guys proceed with the next round!
