### Setup Guide

While running a single-page site using Flask is overkill, I wanted more Flask practice so there...I did it!

DO's guide on using [Nginx with Flask and Gunicorn](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04) was very helpful, I did make the following tweaks to the instructions below:

- Used Python 3.8
```
sudo apt install python3.8 python3.8-dev
```

- Used Pipenv instead of venv
```
sudo pip3 install pipenv
PIPENV_VENV_IN_PROJECT=1 pipenv --python python3.8
pipenv shell
pipenv install -r requirements.txt
```

Examples of the systemd file and nginx config file available in ```configs``` directory