# DAS API

DAS api is the core rest api for the districts and their sub-counties in Uganda.

## Installation

### Requirements
* Python3 >
* django 2.2.5 >

Clone project from Github
```bash
git clone git@github.com:kenedyivan/das_api.git for ssh
or
git clone https://github.com/kenedyivan/das_api.git for http
```

Create virtual environment using virtualenv
```bash
virtualenv -p python3 myenv
```

Activate the virtual environment
```bash
source myvenv/bin/activate
```

Install the packages using pip
```bash
pip install -r requirements.txt
```

## Running

Using django development server
```bash
python manage.py runserver
```

### Deploying to apache

* use mod_wsgi_py3
* Create virtual environment using virtualenv -p python3 venv


## Built With

* [Django](https://laravel.com/) - Web framework
* [Python](https://www.php.net/) - Programming language

## Running tests

```bash
python manage.py test
```

## Versioning

We use [Git](https://git-scm.com/) and [Github](https://github.com/) for versioning. 

## Authors

* **Kenedy Akena**

## License

[MIT](https://choosealicense.com/licenses/mit/)
