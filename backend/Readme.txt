Its project name is recruitment, and its app name are candidates, recruiters, users.

In candidates django app
it contains codes, functionalities of permission and role which can be used by candidate.

In Recruiter django app
it contains codes, functionlaities of permission and roles which can be used by recruiters or employers.

In User django app
it contains codes, functionalities of permission and roles which can be used by any users.

to make it run this project
first create conda environment

To create conda envrionment:
conda create -n myenv python=3.6

to activate conda envrionment:
conda activate myenv

to install requirements:
pip install -r requirements.txt

to run project:
python manage.py runserver

User can only login and register Via gmail but not facebook.

candidates can search, apply jobs, save jobs, remove jobs, see applied status of jobs, create profile, edit profile.

Recuiter can search candidates, post jobs, select or reject applicants, edit jobs, delete jobs, see job status, list candidates according to candidates skill and job's requirements.

Admin can manage users, manage jobs, manage accounts.
