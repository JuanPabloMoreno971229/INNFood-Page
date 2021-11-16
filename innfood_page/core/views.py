from django.shortcuts import render, HttpResponse
from .models import visitas
from datetime import datetime
# Create your views here.

def home(request):
    site_web = "Home"
    num_visits_home = request.session.get('num_visits_home', 0)
    request.session['num_visits_home'] = num_visits_home + 1
    
    date = datetime.today().strftime('%Y-%m-%d')
    ultimo = visitas.objects.values('id').last()
    element = visitas.objects.values('fecha').last()
    
    
    if ultimo is None:
        views_home = visitas(sitio_web = site_web, contador = num_visits_home, fecha = date)
        views_home.save()
    elif ultimo != None:
        last_id = ultimo.get('id')
        last = element.get('fecha') 
        if last == date:
            id = last_id
            views_home = visitas(id, sitio_web = site_web, contador = num_visits_home , fecha = date)
            views_home.save()
        elif last != date:
            num_visits_home = request.session.get('num_visits_home', 0)
            request.session['num_visits_home'] = num_visits_home + 1
            views_home = visitas(sitio_web = site_web, contador = num_visits_home, fecha = date)
            views_home.save()
            print()
    
    return render(request, "core/index.html")

def aboutus(request):

    site_web = "Sobre"
    num_visits_about = request.session.get('num_visits_about', 0)
    request.session['num_visits_about'] = num_visits_about + 1
    date = datetime.today().strftime('%Y-%m-%d')
    views_about = visitas(sitio_web = site_web, contador = num_visits_about, fecha = date)
    views_about.save()

    return render(request, "core/about.html")

