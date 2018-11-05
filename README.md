# f24

Write a Python program that asks the user to input a name and birthdate, in the format: mm-dd-yyyy.  For example, if someone were born today, we would specify the date as: 11-05-2018.  Store these on a Python dictionary.  Make sure that there is only one person with a particular name in the dictionary.  If the user enters a name that is already in the dictionary, the program returns their birthdate (in "raw" `datetime` format is OK).  When the user enters '`Write`' or '`write`' as a "name," then the program will write-out the dictionary to the file `friendsbdays.json` and quit.

Store the date using Python's date structure, whic is a part of the `datetime` module.

Here is how to store a date:

```
import datetime

strdate = '11-05-2018'

dtbday = datetime.datetime.strptime(strdate, "%m-%d-%Y").date()

# check
print(dtbday)
```

NOTE: If the date entered is *NOT* a valid date, according to the `datetime.datetime.strptime()` function, then prompt the user to enter another date 

Here is an example of the program running:
```
Please enter a name: Amy
Please enter Amy's birthdate: 11-05-2000
Please enter a name: Ben
Please enter Ben's birthdate: 11-31-1998
ERROR: There is a problem with that date !!!
Please enter Ben's birtydate: 11-05-1998
Please enter a name: Amy
Amy's birthday is: datetime.date(2000, 11, 5)
Please enter a name: Write
Dictionary written to friendsbdays.json
```

