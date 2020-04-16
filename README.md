---
description: Django setup in CLI
---

# Process

**`Django project setup details:`** 

1\) Install Python3 \(ver 3.7.5 - 32 bit\) 

2\) Create a separate folder \(say, django\) and cd django. 

3\) Create a requirements.txt file in django and specify version of django to be considered for installation.\(say, Django~=2.2.4\) 

4\) Create a virtual environment for our project,

```text
Install virtualenv library
pip install virtualenv

Create a virtual environment
virtualenv myenv

activate this environment
myenv\Scripts\activate    
    Start working now.

if no work, deactivate it
myenv\Scripts\deactivate
```

5\) Install Django `cd django`   `pip install -r requirements.txt` 

6\) Create a django project `cd django`   `django-admin startproject weather` 

7\) Check for correct setup of django installation. run django sever at localhost. 

`cd django`   `py manage.py runserver`

