# Property Estimate Take Home Assignment by Eshwar Tangirala

## Core Features

User can submit a form and have an AI assistant generate, cash flow, revenue, and cost based off of address and property size. 

## Setup Instructions and Command Configurations

Since this project runs in a docker container, the commands to run tests, install packages, and use the app will all need to be run in the container. 

### 1 Clone the repository
 
 Run ```git clone git@github.com:Eshwar1212-maker/property-estimate.git``` and cd into the right directory.

### 2 Build and start the containers
 
 ```docker compose up --build```

 Run migrations with:

```docker compose exec web python manage.py migrate```

 Create a superuser with:
 
 ```docker compose exec web python manage.py createsuperuser```

 (Optional) Create a superuser for Django Admin with:
 
 ```docker compose exec web pytest```

 Also, I used black and flake8 for overall cleanliness and formatting. Run these commands to ensure code is formatted, has less style errors and bugs"

```docker compose exec web black .```

```docker compose exec web flake8 /code```  

## Assumptions made

Here are some assumptions I made which explain the choices I used for certain technologies or paradigms. 

-I used Django Templates for the front end. Since you guys said that right now you're only using Tailwind CSS with HTML. I thought that this would be the most simplest approach to build the template with the Django application instead of creating a separate folder just with HTML/CSS in them. 

## Potential Improvements with more time

-Creating an 'apps' directory and putting estimates inside of that folder, instead of having the estimates folder be there by itself just for future scalability.
-UIx, styling, and responsiveness. If i had more than the 4 hour mark. I would of made the website look a little more user friendly, and styled and similar to the Figma designs.
