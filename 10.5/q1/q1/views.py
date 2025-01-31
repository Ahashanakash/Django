from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    d = {"adress": "ctg", "age": 19, "lst": [1, 2, 3], 'courses':[
        {
            'id' : 111,
            'name': 'bangla',
            'fee': 6300,
        },
        {
            'id' : 211,
            'name': 'english',
            'fee': 7200,
        },
        {
            'id' : 311,
            'name': 'math',
            'fee': 8100,
        }
    ]}
    return render(request,'home.html',d)