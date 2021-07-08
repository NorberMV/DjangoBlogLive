
"""Platzigram views"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json



# Greetings Function
def hi_func(request, name, age):
    #now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    if age > 18:
        message = 'Hi {}, welcome to Platzigram!' .format(
            name)
    else:
        message = 'Sorry {}, you\'re under age to access Platzigram!' .format(
            name)

    return HttpResponse("{}, The current server time is: {now}" .format(
        message, now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ) ) 
# Function 2
def hi(request):
    #import pdb; pdb.set_trace() Debbuger
    numbers = request.GET['numbers']
    #import pdb; pdb.set_trace()
    splitnum = numbers.split(',')

    integerslist = [int(num) for num in splitnum]
    sortedlist = sorted(integerslist)
    # pdb.set_trace()
    data = {
        'status':'ok',
        'sorted numbers': sortedlist,
        'message': 'The list of integers was sorted succesfully!'
    }

    return HttpResponse(json.dumps(data,indent=4),content_type='application/json')