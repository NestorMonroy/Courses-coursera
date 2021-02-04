from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    if num_visits > 4 : del(request.session['num_visits'])
    id_assignment = '767d3dd2'
    response = """ <p>"""+id_assignment+"""</p>  <p>view count """+str(num_visits)+"""</p>"""
    response = HttpResponse(response)
    response.set_cookie('dj4e_cookie', '767d3dd2', max_age=1000) # seconds until expire
    return response


