Это репозиторий для хранения домашних заданий. Ссылка на курс: Автоматизация тестирования с помощью Selenium и Python

HOW TO INSTALL:

Python version -- 3.8.5

1) Activate your virtual environment:

For Mac:

python3 -m venv venv
source venv/bin/activate
For Windows:

pip install virtualenv
virtualenv venv
venv\Scripts\activate
2) Clone the repository to your local machine:

git clone https://github.com/oldevgeny/stepik-auto-tests-course.git
3) Install the requirements:

pip install --upgrade pip
pip install -r requirements.txt
START:

Run scripts

python3 [script_path]
Run PyTests

pytest scripts/selenium_scripts
# find all tests in dir scripts/selenium_scripts

pytest test_user_interface.py
# find and run all tests in file

pytest scripts/drafts.py::test_register_new_user_parametrized
# find test with name test_register_new_user_parametrized in current file in current dir and run# education_selenium
