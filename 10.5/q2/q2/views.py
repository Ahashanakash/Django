from django.shortcuts import render
from datetime import datetime, timedelta

def home (request):
    d={'lst': ["python","is","best"], 'date':datetime.now(),'n':5, 'lst1':"python IS fun",
       'arr':[
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
],
       'value':123456789,
    'blog_date': datetime(2025, 1, 28, 12, 0, 0),
    'comment_date' : datetime.now(),
    }
    return render(request,'home.html',d)