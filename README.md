### Setup Guide

While running a single-page site using Flask is overkill and really has no benefit, I wanted more Flask practice so there...I did it!

DO's guide on using [Nginx with Flask and Gunicorn](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04) was very helpful, I made some changes

#### Dependencies

- Install needed packages (for Ubuntu)
```
sudo apt install python3.8 python3.8-dev python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
```

- Install pipenv
```
sudo pip3 install pipenv
```

- Pull this repo for examples, or just grab the requirements.txt file for next step

- Create your pipenv project, with venv file locally, makes setting up systemd file easier for path
```
PIPENV_VENV_IN_PROJECT=1 pipenv --python python3.8
pipenv shell
pipenv install -r requirements.txt
```

MORE INSTRUCTIONS TO COME

Install Nginx
Copy Nginx Site config over
Copy systemd file over
Create, enable, start, etc
Certbot steps
