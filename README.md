# Hack The Printer Scoring Panel

This scoring panel was coded in a histerical rush, so its quality is quite low... But, it works! It simply displays a pretty scoring board for the Hack The Printer event in ekoparty13. You need to populate the database through Django Admin Panel, or directly to the chosen DB.

## How to use

### For developing or testing

Download a release or clone the repo and then, inside your virtual environment, run:

```
cd eko-panel
pip install -r requirements

cd eko
cp eko/settings.py.dist eko/settings.py

# Edit settings accordingly (change the secret key, disable debug, set static path, etc.)
vim eko/settings.py

./manage.py collectstatic
./manage.py check
./manage.py makemigrations
./manage.py migrate

# Run dev server
./manage.py runserver
```

### For a production server

NGINX + uWSGI + Django is the best combination. Check this project to create a Docker container: https://github.com/dockerfiles/django-uwsgi-nginx.

## License

"Hack The Printer" logo by Andres Snitcofsky, under WTFPL. Template design by A Fox, under WTFPL.

This project is under the [![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png)](http://www.wtfpl.net/) **Do What The Fuck You Want To Public License**. So, you know... Do what the fuck you want with this :)
