import os
from datetime import datetime
from datetime import timedelta

def int_to_ord(n: int, tag: str | None = "sup") -> str:
    match n:
        case 1 | -1:
            ord_suffix = "st"
        case 2 | -2:
            ord_suffix = "nd"
        case 3 | -3:
            ord_suffix = "rd"
        case _:
            ord_suffix = "th"

    if tag == None:
        return f"{n}{ord_suffix}"
    else:    
        return f"{n}<{tag}>{ord_suffix}</{tag}>"



TODAY = datetime.today()
CURRENT_YEAR = TODAY.strftime("%y")

# Determine dates for the next two PUGs, labelled 'Upcoming' and 'Future'

# Find the 'next first Thursday of the month'

test_thursday = TODAY + timedelta(days=(3-TODAY.weekday())%7)

while test_thursday.weekday() != 3 or test_thursday.day > 7:
    test_thursday += timedelta(weeks=1)

upcoming_date = test_thursday
upcoming_month = upcoming_date.strftime("%b")

test_thursday += timedelta(weeks = 3)

while test_thursday.weekday() != 3 or test_thursday.day > 7:
    test_thursday += timedelta(weeks=1)

future_date = test_thursday
future_month = future_date.strftime("%b")

with open("template.ipynb") as f:
    TEMPLATE = f.read()

current_dir = [dir for dir in os.listdir() if CURRENT_YEAR in dir]

if len(current_dir) != 1:
    raise FileNotFoundError("Cannot find this year's notebooks.")

current_dir = current_dir[0]

# Create the upcoming and next following notebooks
notebooks = [nb for nb in os.listdir(current_dir) if nb[-2:] == "nb"]

if not any([nb for nb in notebooks if upcoming_month in nb]):
    # Find next number
    n = max([int(nb[:2]) for nb in notebooks]) + 1
    
    # Create notebook and fill with template
    upcoming_nb_path = f"{current_dir}/{n}-{upcoming_month}{CURRENT_YEAR}.ipynb"  
    
    replacements = (("yyyy",upcoming_date.strftime("%Y")),
                    ("MMM",upcoming_month),
                    ("Mmmm", upcoming_date.strftime("%B")),
                    ("dord",int_to_ord(upcoming_date.day)),
                    ("NN", str(n)))
    
    upcoming_nb_contents = TEMPLATE

    for r in replacements:
        upcoming_nb_contents = upcoming_nb_contents.replace(*r)

    with open(upcoming_nb_path, "w") as f:
        f.write(upcoming_nb_contents)
        
notebooks = [nb for nb in os.listdir(current_dir) if nb[-2:] == "nb"]

if not any([nb for nb in notebooks if future_month in nb]):
    # Find next number
    n = max([int(nb[:2]) for nb in notebooks]) + 1

    # Find 
    
    # Create notebook and fill with template
    future_nb_path = f"{current_dir}/{n}-{future_month}{CURRENT_YEAR}.ipynb"  
    
    replacements = (("yyyy",future_date.strftime("%Y")),
                    ("MMM",future_month),
                    ("Mmmm", future_date.strftime("%B")),
                    ("dord",int_to_ord(future_date.day)),
                    ("NN", str(n)))
    
    future_nb_contents = TEMPLATE

    for r in replacements:
        future_nb_contents = future_nb_contents.replace(*r)
    
    with open(future_nb_path, "w") as f:
        f.write(future_nb_contents)



# Build in Dec-Jan process