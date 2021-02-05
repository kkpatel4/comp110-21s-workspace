"""A vaccination calculator."""

__author__ = "730225319"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses_done: int = int(input("Doses administered: "))
dose_rate: int = int(input("Doses per day: "))
vaccinated: int = int(input("Target percent vaccinated: "))

doses_needed: int = round(population * (vaccinated / 100)) * 2
doses_to_go: int = doses_needed - doses_done
days_needed: int = round(doses_to_go / dose_rate)

date_finished: datetime = datetime.today() + timedelta(days_needed)

print("We will reach " + str(vaccinated) + "% vaccination in " + str(days_needed) + " days, which falls on " + date_finished.strftime("%B %d, %Y") + ".")