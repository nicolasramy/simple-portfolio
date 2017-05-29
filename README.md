# simple-portfolio
A simple solution to publish your portfolio

## Requirements

- Python 2.7

## Installation

1. Clone the repository
2. Run Python packages installation ```pip install -r requirements.txt```
3. Generate a secret key ```python scripts/generate_secret_key.py```
4. Go to ```www/``` folder (```cd www/```)
5. Copy ```simple_portfolio/settings.py.default``` to ```simple_portfolio/settings.py```
6. Add the generated secret key to ```simple_portfolio/settings.py``` 
7. Run Django migrations ```python manage.py migrate```
8. Create a superuser ```python manage.py createsuperuser```
9. Run Django server ```python manage.py runserver```

## TODO

- [] Add auto-remove on picture edition and remove
