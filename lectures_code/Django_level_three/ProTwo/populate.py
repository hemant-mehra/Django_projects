import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProTwo.settings")

import django
django.setup()


from faker import Faker
from AppTwo.models import User
import  random

fakegen=Faker()

def populate(n):
    for entry in range(n):
        fake_fn=fakegen.first_name()
        fake_ln=fakegen.last_name()
        fake_mail=fakegen.ascii_free_email()

        users=User.objects.get_or_create(first_name=fake_fn,last_name=fake_ln,mail=fake_mail)[0]

if __name__=="__main__":
    print("populate script")
    populate(20)
    print(" populate done")
