from address.models import *

def run():
    LocalBodyCategory(id=102, name="Metropolitan City", new_old=1).save()
    LocalBodyCategory(id=103, name="Sub-MetropolitanCity", new_old=1).save()
    LocalBodyCategory(id=105, name="Municipality", new_old=1).save()
    LocalBodyCategory(id=119, name="Rural Municipality", new_old=1).save()
    LocalBodyCategory(id=107, name="Village Development Comittee", new_old=0).save()