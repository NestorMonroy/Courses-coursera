import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript load

from petselect.models import Pet


def run():
    fhand = open('petselect/pets.csv')
    reader = csv.reader(fhand)
    next(reader)

    Pet.objects.all().delete()

    for row in reader:
        #print(row)
        name = row[0]
        hair = row[1]
        size = row[2]


        pet = Pet.objects.create(
            name=name,
            hair = hair, 
            size=size
        )

        pet.save()
