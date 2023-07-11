## 1. Install a virtual environment

### Linux :
```bash
python3 -m venv venv
```
## 2. Activate venv

### Linux :
```bash
source venv/bin/activate
```
## 3. Installing dependencies

### Linux :
```bash
pip3 install -r requirements.txt
```
## 4. Make db migrations 

### Linux :
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
## 5. Run server

### Linux :
```bash
python3 manage.py runserver
```
## 6. Run django-extensions console

### Linux :
```bash
python3 manage.py shell_plus --ipython
```


