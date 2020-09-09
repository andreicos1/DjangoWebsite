import os
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogsite.settings')

import django
django.setup()
import random
from users.models import User
from faker import Faker
from django.utils import timezone

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_username = fake_first_name + fake_last_name
        fake_email = fakegen.email()

        new_user = User.objects.get_or_create(username = fake_username,
                                        first_name = fake_first_name,
                                        last_name = fake_last_name,
                                        email = fake_email,
                                        )[0]
        new_user.profile.bio=fakegen.sentence()
        new_user.profile.birth_date = fakegen.date()
        THIS_DIR = os.path.dirname('populate_users.py')
        new_user.profile.image = random.choice([x for x in os.listdir(os.path.join(
                                            THIS_DIR, 'users/media/'))])
        new_user.profile.save()



if __name__ == '__main__':
    print("Populating Script!")
    populate(10)
    print("Populating Complete !")
