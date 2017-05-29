# simple-portfolio
A simple solution to publish your portfolio


## Requirements

- Python 2.7

## Installation

1. Clone the repository
2. Run Python packages installation ```pip install -r requirements.txt```
3. Go to ```www/``` folder (```cd www/```)
4. Copy ```simple_portfolio/settings.py.default``` to ```simple_portfolio/settings.py```
5. Generate a secret key ```python -c "import string,random; uni=string.ascii_letters+string.digits+string.punctuation; print repr(''.join([random.SystemRandom().choice(uni) for i in range(random.randint(45,50))]))"```
5. Add the secret key to ```simple_portfolio/settings.py``` 
6. Run Django migrations ```python manage.py migrate```
7. Create a superuser ```python manage.py createsuperuser```
8. Run Django server ```python manage.py runserver```

## TODO

- [] Add auto-remove on picture edition and remove
