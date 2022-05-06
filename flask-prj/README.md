Original [repo](https://github.com/axat1/UTA_Enrollment)

# software

* python 
* pip 
* virtual env tool 

# check if python is installed

* `python --version`
* `pip --version`

# list available packages
* `pip list`

# install a package
* `pip install virtualenv`

# uninstall a package
* `pip uninstall virtualenv`

# install venv 
* `python -m venv venv`

# activate virtual environment and install needed libraries

* `venv\Scripts\activate`
* `pip install flask`
* `pip install flask-wtf`
* `pip install python-dotenv`
* `pip install flask-mongoengine`
* `pip install flask-restx`

# save packages
* `pip freeze > requirements.txt`

# install from requirements.txt
* `pip install -r requirements.txt`

# run flask application 
* `flask run`

# see environment content
* `pip list`

# use `--jsonArray` when importing data in mongodb with mongoimport

# generate a key from python
* `py -c "import os; print(os.random(16))"`
