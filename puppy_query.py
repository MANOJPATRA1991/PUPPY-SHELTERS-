from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from puppies import Base, Shelter, Puppy

from sqlalchemy import func
import datetime

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


def query_sort():
    """
    Print all Puppy names in ascending order
    """
    result = session.query(Puppy).order_by(Puppy.name.asc()).all()

    for i in result:
        print(i.name)


def query_sort_birth():
    """
    Print name and date of birth for all puppies less than 6 months old ordered by youngest first
    """
    today = datetime.date.today()
    if has_passed_leap_day(today):
        six_months_ago = today - datetime.timedelta(days=183)
    else:
        six_months_ago = today - datetime.timedelta(days=182)
    result = session.query(Puppy.name, Puppy.dateOfBirth) \
        .filter(Puppy.dateOfBirth >= six_months_ago) \
        .order_by(Puppy.dateOfBirth.desc())

    for i in result:
        print("{name}: {dob}".format(name=i.name, dob=i.dateOfBirth))


def query_weight():
    """
    Print name and weight of all puppies ordered by weight in ascending order
    """
    result = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight.asc())

    for i in result:
        print("{name}: {weight}".format(name=i.name, weight=i.weight))

# HELPER FUNCTION
def has_passed_leap_day(today):
    """
    This function checks if the day six months ago from today lies
    before or after 29 February in case of a leap year
    1. If the day lies before 29 February, we subtract 183 days
    2. If the day lies after 29 February, we subtract 182 days

    else if it is not a leap year, we subtract 182 days
    :param today:
    :return Boolean:
    """
    this_year = today.timetuple()[0]
    if is_leap_year(this_year):
        six_months_ago = today - datetime.timedelta(days=183)
        leap_day = datetime.date(this_year, 2, 29)
        return leap_day >= six_months_ago
    else:
        return False


def query_shelter():
    """
    Print number of puppies in each shelter
    """
    result = session.query(Shelter, func.count(Puppy.id))\
        .join(Puppy).group_by(Puppy.shelter_id).all()

    for i in result:
        print("{id}. {shelter}: {count}".format(id=i[0].id, shelter=i[0].name, count=i[1]))


# HELPER FUNCTION
def is_leap_year(year):
    """
    Check for leap year
    :param year:
    :return Boolean:
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


# query_sort()
# query_sort_birth()
# query_weight()
query_shelter()
