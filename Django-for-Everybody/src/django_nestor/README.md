
cd ...wherever...
cd django_nestor
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser --username root
# python3 manage.py changepassword root
# dj4e_nn_!
python3 manage.py runscript gview_load
python3 manage.py runscript many_load

These samples may be updated from time to time so you might want to get updates
using `git pull`.  Also if there are bugs, you are welcome to submit
a Pull Request on github.

All of the documentation material is copyright CC-BY 3.0 and the code is copyright MIT
by whomever wrote the code or documentation.  You are welcome to use this in any way you see
fit and paste code from this repo into your applications.
