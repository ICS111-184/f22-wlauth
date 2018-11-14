# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:40:20 2018

@author: User
"""


nabirth = dict()
nabirth[Name] ='11-5-2000' 
nabirth['Ben'] ='11-31-1998'
#print(nabirth)
#print(nabirth['Amy'])
#print(nabirth['Ben'])
#import datetime
#
#strdate = '11-05-2018'
#
#dtbday = datetime.datetime.strptime(strdate, "%m-%d-%Y").date()
#
## check
#print(dtbday)

#Dictionary written to friendsbdays.json


#Please enter a name: Amy
#Please enter Amy's birthdate: 11-05-2000
#Please enter a name: Ben
#Please enter Ben's birthdate: 11-31-1998
#ERROR: There is a problem with that date !!!
#Please enter Ben's birtydate: 11-05-1998
#Please enter a name: Amy
#Amy's birthday is: datetime.date(2000, 11, 5)
#Please enter a name: Write
#Dictionary written to friendsbdays.json

#eng2sp = dict() 
#print(eng2sp) 
#
#eng2sp['one'] = 'uno' 
#print(eng2sp)


#Name =  input('Please enter a name ' )
#print(Name)


import datetime

dtnow = datetime.datetime.now()
# 2018-11-14 13:21:39.526898
dtnow2 = datetime.datetime.now()
# 2018-11-14 13:17:07.496796

print(dtnow)
# 2018-11-14 12:45:33.459172
type(dtnow)
#datetime.datetime

dtnow
#datetime.datetime(2018, 11, 14, 12, 49, 3, 68774)

dtnow.strftime('%A')
# Wednesday


dtnow.strftime('%a == %A')
# 'Wed == Wednesday'


dtnow.strftime('%D == %m - %d - %y')
# '11/14/18 == 11 - 14 - 18'

dtnow.strftime('%B %d, %Y')
# 'November 14, 2018'

dtnow.strftime('%b %d, %Y')
# 'Nov 14, 2018'
























