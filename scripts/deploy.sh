cd ..
pip install -r requirements.txt
python www/manage.py migrate frontend
python www/manage.py collectstatic
