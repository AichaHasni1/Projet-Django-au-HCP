from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from .models import User
from django.contrib.auth import logout
from .models import Population
import pandas as pd
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "myapp/index.html", {})
def static(request):
    return render(request, "../static", {})

total_population_sup15 = Population.objects.filter(AGES__in=['15-19 ans', '20-24 ans', '25-29 ans', '30-34 ans', '35-39 ans', '40-44 ans', '45-49 ans', '50-54 ans', '55-59 ans', '60-64 ans', '65-69 ans', '70-74 ans', '75 ans et plus']).count()
# print(total_population_sup15)
total_analphabete = Population.objects.filter(NIV_ET_AGR="Aucun niveau d'études", AGES__in=['15-19 ans', '20-24 ans', '25-29 ans', '30-34 ans', '35-39 ans', '40-44 ans', '45-49 ans', '50-54 ans', '55-59 ans', '60-64 ans', '65-69 ans', '70-74 ans', '75 ans et plus']).count()
# print(total_analphabete)
taux_analphabete = (total_analphabete / total_population_sup15) * 100
# print(taux_analphabete)

total_analphabete_rur = Population.objects.filter(MIL='Rural', NIV_ET_AGR="Aucun niveau d'études", AGES__in=['15-19 ans', '20-24 ans', '25-29 ans', '30-34 ans', '35-39 ans', '40-44 ans', '45-49 ans', '50-54 ans', '55-59 ans', '60-64 ans', '65-69 ans', '70-74 ans', '75 ans et plus']).count()
total_analphabete_urb = Population.objects.filter(MIL='Urbain', NIV_ET_AGR="Aucun niveau d'études", AGES__in=['15-19 ans', '20-24 ans', '25-29 ans', '30-34 ans', '35-39 ans', '40-44 ans', '45-49 ans', '50-54 ans', '55-59 ans', '60-64 ans', '65-69 ans', '70-74 ans', '75 ans et plus']).count()
taux_analphabete_rur = (total_analphabete_rur / total_population_sup15) * 100
taux_analphabete_urb = (total_analphabete_urb / total_population_sup15) * 100
total_analphabete_fem = Population.objects.filter(SEXE='Féminin', NIV_ET_AGR="Aucun niveau d'études",
                                                  AGES__in=['15-19 ans', '20-24 ans', '25-29 ans', '30-34 ans',
                                                            '35-39 ans', '40-44 ans', '45-49 ans', '50-54 ans',
                                                            '55-59 ans', '60-64 ans', '65-69 ans', '70-74 ans',
                                                            '75 ans et plus']).count()
total_analphabete_masc = Population.objects.filter(SEXE='Masculin', NIV_ET_AGR="Aucun niveau d'études",
                                                  AGES__in=['15-19 ans', '20-24 ans', '25-29 ans', '30-34 ans',
                                                            '35-39 ans', '40-44 ans', '45-49 ans', '50-54 ans',
                                                            '55-59 ans', '60-64 ans', '65-69 ans', '70-74 ans',
                                                            '75 ans et plus']).count()
taux_analphabete_fem = (total_analphabete_fem / total_population_sup15) * 100
taux_analphabete_masc = (total_analphabete_masc / total_population_sup15) * 100


total_population = Population.objects.count()
priv_handicap = Population.objects.filter(SIT_HANDICAP="Personne en situation de handicap").count()
priv_handicap = (priv_handicap / total_population) * 100

prev_handicap_urb = (Population.objects.filter(MIL="Urbain",SIT_HANDICAP="Personne en situation de handicap").count() / total_population) * 100
prev_handicap_rur = (Population.objects.filter(MIL="Rural",SIT_HANDICAP="Personne en situation de handicap").count() / total_population) * 100
prev_nhandicap_urb = (Population.objects.filter(MIL="Urbain",SIT_HANDICAP="Personne non en situation de handicap").count() / total_population) * 100
prev_nhandicap_rur = (Population.objects.filter(MIL="Rural",SIT_HANDICAP="Personne non en situation de handicap").count() / total_population) * 100

handicap_mas = (Population.objects.filter(SEXE="Masculin",SIT_HANDICAP="Personne en situation de handicap").count() / total_population) * 100
nhandicap_mas = (Population.objects.filter(SEXE="Masculin",SIT_HANDICAP="Personne non en situation de handicap").count() / total_population) * 100
handicap_fem = (Population.objects.filter(SEXE="Féminin",SIT_HANDICAP="Personne en situation de handicap").count() / total_population) * 100
nhandicap_fem = (Population.objects.filter(SEXE="Féminin",SIT_HANDICAP="Personne non en situation de handicap").count() / total_population) * 100


taux_urbanisme = Population.objects.filter(MIL="Urbain").count()
taux_urbanisme = (taux_urbanisme / total_population) * 100
taux_ruralisme = 100 - taux_urbanisme

taux_mariage = Population.objects.filter(E_MAT='Marié').count()
taux_mariage = (taux_mariage / total_population) * 100
taux_cel = 100 - taux_mariage
 

population_masculin = Population.objects.filter(SEXE='Masculin').count()
population_fem = Population.objects.filter(SEXE='Féminin').count()
taux_masculin = (population_masculin/total_population)*100
taux_fem = 100 - taux_masculin

 

total_population_inf20 = Population.objects.filter(AGES__in=['0-4 ans', '5-9 ans', '10-14 ans', '15-19 ans']).count()
total_population_sup65 = Population.objects.filter(AGES__in=['65-69 ans', '70-74 ans', '75 ans et plus']).count()
taux_jeuness = (total_population_inf20 / total_population)*100
taux_vieil = (total_population_sup65 / total_population)*100

urbain_auc = Population.objects.filter(MIL='Urbain', NIV_ET_AGR="Aucun niveau d'études").count()
rural_auc = Population.objects.filter(MIL='Rural', NIV_ET_AGR="Aucun niveau d'études").count()
urbain_prim = Population.objects.filter(MIL='Urbain', NIV_ET_AGR="Primaire").count()
rural_prim = Population.objects.filter(MIL='Rural', NIV_ET_AGR="Primaire").count()
urbain_pre = Population.objects.filter(MIL='Urbain', NIV_ET_AGR="Préscolaire").count()
rural_pre = Population.objects.filter(MIL='Rural', NIV_ET_AGR="Préscolaire").count()
urbain_sc = Population.objects.filter(MIL='Urbain', NIV_ET_AGR="Secondaire collégial").count()
rural_sc = Population.objects.filter(MIL='Rural', NIV_ET_AGR="Secondaire collégial").count()
urbain_squa = Population.objects.filter(MIL='Urbain', NIV_ET_AGR="Secondaire qualifiant").count()
rural_squa = Population.objects.filter(MIL='Rural', NIV_ET_AGR="Secondaire qualifiant").count()
urbain_sup = Population.objects.filter(MIL='Urbain', NIV_ET_AGR="Supérieur").count()
rural_sup = Population.objects.filter(MIL='Rural', NIV_ET_AGR="Supérieur").count()
masculin_auc = Population.objects.filter(SEXE='Masculin', NIV_ET_AGR="Aucun niveau d'études").count()
feminin_auc = Population.objects.filter(SEXE='Féminin', NIV_ET_AGR="Aucun niveau d'études").count()
masculin_prim = Population.objects.filter(SEXE='Masculin', NIV_ET_AGR="Primaire").count()
feminin_prim = Population.objects.filter(SEXE='Féminin', NIV_ET_AGR="Primaire").count()
masculin_pre = Population.objects.filter(SEXE='Masculin', NIV_ET_AGR="Préscolaire").count()
feminin_pre = Population.objects.filter(SEXE='Féminin', NIV_ET_AGR="Préscolaire").count()
masculin_sc = Population.objects.filter(SEXE='Masculin', NIV_ET_AGR="Secondaire collégial").count()
feminin_sc = Population.objects.filter(SEXE='Féminin', NIV_ET_AGR="Secondaire collégial").count()
masculin_squa = Population.objects.filter(SEXE='Masculin', NIV_ET_AGR="Secondaire qualifiant").count()
feminin_squa = Population.objects.filter(SEXE='Féminin', NIV_ET_AGR="Secondaire qualifiant").count()
masculin_sup = Population.objects.filter(SEXE='Masculin', NIV_ET_AGR="Supérieur").count()
feminin_sup = Population.objects.filter(SEXE='Féminin', NIV_ET_AGR="Supérieur").count()

urbain_celi_total = Population.objects.filter(MIL="Urbain", E_MAT="Célibataire").count()
urbain_mar_total = Population.objects.filter(MIL="Urbain", E_MAT="Marié").count()
rural_celi_total = Population.objects.filter(MIL="Rural", E_MAT="Célibataire").count()
rural_mar_total = Population.objects.filter(MIL="Rural", E_MAT="Marié").count()
urbain_div_total = Population.objects.filter(MIL="Urbain", E_MAT="Divorcé").count()
rural_div_total = Population.objects.filter(MIL="Rural", E_MAT="Divorcé").count()
urbain_ve_total = Population.objects.filter(MIL="Urbain", E_MAT="Veuf").count()
rural_ve_total = Population.objects.filter(MIL="Rural", E_MAT="Veuf").count()
celi = Population.objects.filter(E_MAT="Célibataire").count()
mar = Population.objects.filter(E_MAT="Marié").count()
ve = Population.objects.filter(E_MAT="Veuf").count()
div = Population.objects.filter(E_MAT="Divorcé").count()

total_urbains = Population.objects.filter(MIL="Urbain").count()
total_ruraux = Population.objects.filter(MIL="Rural").count()

hommes1 = Population.objects.filter(SEXE="Masculin", AGES__in=['0-4 ans', '5-9 ans']).count()
hommes2 = Population.objects.filter(SEXE="Masculin", AGES__in=['10-14 ans', '15-19 ans']).count()
hommes3 = Population.objects.filter(SEXE="Masculin", AGES__in=['20-24 ans', '25-29 ans']).count()
hommes4 = Population.objects.filter(SEXE="Masculin", AGES__in=['30-34 ans', '35-39 ans']).count()
hommes5 = Population.objects.filter(SEXE="Masculin", AGES__in=['40-44 ans', '45-49 ans']).count()
hommes6 = Population.objects.filter(SEXE="Masculin", AGES__in=['50-54 ans', '55-59 ans']).count()
hommes7 = Population.objects.filter(SEXE="Masculin", AGES__in=['60-64 ans', '65-69 ans']).count()
hommes8 = Population.objects.filter(SEXE="Masculin", AGES__in=['70-74 ans', '75 ans et plus']).count()
femmes1 = Population.objects.filter(SEXE="Féminin", AGES__in=['0-4 ans', '5-9 ans']).count()
femmes2 = Population.objects.filter(SEXE="Féminin", AGES__in=['10-14 ans', '15-19 ans']).count()
femmes3 = Population.objects.filter(SEXE="Féminin", AGES__in=['20-24 ans', '25-29 ans']).count()
femmes4 = Population.objects.filter(SEXE="Féminin", AGES__in=['30-34 ans', '35-39 ans']).count()
femmes5 = Population.objects.filter(SEXE="Féminin", AGES__in=['40-44 ans', '45-49 ans']).count()
femmes6 = Population.objects.filter(SEXE="Féminin", AGES__in=['50-54 ans', '55-59 ans']).count()
femmes7 = Population.objects.filter(SEXE="Féminin", AGES__in=['60-64 ans', '65-69 ans']).count()
femmes8 = Population.objects.filter(SEXE="Féminin", AGES__in=['70-74 ans', '75 ans et plus']).count()

ages1 = Population.objects.filter(AGES__in=['0-4 ans', '5-9 ans']).count()
ages2 = Population.objects.filter(AGES__in=['10-14 ans', '15-19 ans']).count()
ages3 = Population.objects.filter(AGES__in=['20-24 ans', '25-29 ans']).count()
ages4 = Population.objects.filter(AGES__in=['30-34 ans', '35-39 ans']).count()
ages5 = Population.objects.filter(AGES__in=['40-44 ans', '45-49 ans']).count()
ages6 = Population.objects.filter(AGES__in=['50-54 ans', '55-59 ans']).count()
ages7 = Population.objects.filter(AGES__in=['60-64 ans', '65-69 ans']).count()
ages8 = Population.objects.filter(AGES__in=['70-74 ans', '75 ans et plus']).count()


 

 
h_ages1 = Population.objects.filter(SIT_HANDICAP="Personne en situation de handicap", AGES__in=['0-4 ans', '5-9 ans', '10-14 ans', '15-19 ans']).count()
h_ages2 = Population.objects.filter(SIT_HANDICAP="Personne en situation de handicap", AGES__in=['20-24 ans', '25-29 ans', '30-34 ans', '35-39 ans']).count()
h_ages3 = Population.objects.filter(SIT_HANDICAP="Personne en situation de handicap", AGES__in=['40-44 ans', '45-49 ans', '50-54 ans', '55-59 ans']).count()
h_ages4 = Population.objects.filter(SIT_HANDICAP="Personne en situation de handicap", AGES__in=['60-64 ans', '65-69 ans', '70-74 ans', '75 ans et plus']).count()
def welcome(request):
    user_name = request.session.get('user_name')
    context = {
        'user_name': user_name,
        'taux_analphabete': taux_analphabete,
        'priv_handicap': priv_handicap,
       'taux_urbanisme': taux_urbanisme,
        'taux_ruralisme': taux_ruralisme,
        'taux_mariage': taux_mariage,
         'taux_cel': taux_cel,
        'taux_masculin': taux_masculin,
        'taux_fem': taux_fem,
        'taux_jeuness': taux_jeuness,
        'taux_vieil': taux_vieil,
        'urbain_auc': urbain_auc,
        'rural_auc': rural_auc,
        'urbain_prim': urbain_prim,
        'rural_prim': rural_prim,
        'urbain_pre': urbain_pre,
        'rural_pre': rural_pre,
        'urbain_sc': urbain_sc,
        'rural_sc': rural_sc,
        'urbain_squa': urbain_squa,
        'rural_squa': rural_squa,
        'urbain_sup': urbain_sup,
        'rural_sup': rural_sup,
        'masculin_auc': masculin_auc,
        'feminin_auc': feminin_auc,
        'masculin_prim': masculin_prim,
        'feminin_prim': feminin_prim,
        'masculin_pre': masculin_pre,
        'feminin_pre': feminin_pre,
        'masculin_sc': masculin_sc,
        'feminin_sc': feminin_sc,
        'masculin_squa': masculin_squa,
        'feminin_squa': feminin_squa,
        'masculin_sup': masculin_sup,
        'feminin_sup': feminin_sup,
        'taux_analphabete_rur': taux_analphabete_rur,
        'taux_analphabete_urb': taux_analphabete_urb,
        'taux_analphabete_fem': taux_analphabete_fem,
        'taux_analphabete_masc': taux_analphabete_masc,
        'prev_handicap_urb': prev_handicap_urb,
        'prev_handicap_rur': prev_handicap_rur,
        'prev_nhandicap_urb': prev_nhandicap_urb,
        'prev_nhandicap_rur': prev_nhandicap_rur,
        'urbain_celi_total': urbain_celi_total,
        'urbain_mar_total': urbain_mar_total,
        'rural_celi_total': rural_celi_total,
        'rural_mar_total': rural_mar_total,
        'population_masculin': population_masculin,
        'population_fem': population_fem,
        'total_urbains': total_urbains,
        'total_ruraux': total_ruraux,
        'hommes1': hommes1,
        'hommes2': hommes2,
        'hommes3': hommes3,
        'hommes4': hommes4,
        'hommes5': hommes5,
        'hommes6': hommes6,
        'hommes7': hommes7,
        'hommes8': hommes8,
        'femmes1': femmes1,
        'femmes2': femmes2,
        'femmes3': femmes3,
        'femmes4': femmes4,
        'femmes5': femmes5,
        'femmes6': femmes6,
        'femmes7': femmes7,
        'femmes8': femmes8,
        'ages1': ages1,
        'ages2': ages2,
        'ages3': ages3,
        'ages4': ages4,
        'ages5': ages5,
        'ages6': ages6,
        'ages7': ages7,
        'ages8': ages8,
        'handicap_mas': handicap_mas,
        'handicap_fem': handicap_fem,
        'nhandicap_mas': nhandicap_mas,
        'nhandicap_fem': nhandicap_fem,
     
        'urbain_div_total': urbain_div_total,
        'urbain_ve_total': urbain_ve_total,
        'rural_ve_total': rural_ve_total,
        'rural_div_total': rural_div_total,
        'celi': celi,
        'mar': mar,
        've': ve,
        'div': div
    }
    return render(request, "myapp/welcome.html", context)

from django.contrib.auth import get_user_model
def welcome_admin(request):
    User = get_user_model()
    user_name = request.session.get('user_name')
    users = User.objects.all()
    context = {
        'user_name': user_name,
        'taux_analphabete': taux_analphabete,
        'priv_handicap': priv_handicap,
         
        'taux_urbanisme': taux_urbanisme,
        'taux_ruralisme': taux_ruralisme,
        'taux_mariage': taux_mariage,
        
        'taux_cel': taux_cel,
        'taux_masculin': taux_masculin,
        'taux_fem': taux_fem,
        'taux_jeuness': taux_jeuness,
        'taux_vieil': taux_vieil,
        'urbain_auc': urbain_auc,
        'rural_auc': rural_auc,
        'urbain_prim': urbain_prim,
        'rural_prim': rural_prim,
        'urbain_pre': urbain_pre,
        'rural_pre': rural_pre,
        'urbain_sc': urbain_sc,
        'rural_sc': rural_sc,
        'urbain_squa': urbain_squa,
        'rural_squa': rural_squa,
        'urbain_sup': urbain_sup,
        'rural_sup': rural_sup,
        'masculin_auc': masculin_auc,
        'feminin_auc': feminin_auc,
        'masculin_prim': masculin_prim,
        'feminin_prim': feminin_prim,
        'masculin_pre': masculin_pre,
        'feminin_pre': feminin_pre,
        'masculin_sc': masculin_sc,
        'feminin_sc': feminin_sc,
        'masculin_squa': masculin_squa,
        'feminin_squa': feminin_squa,
        'masculin_sup': masculin_sup,
        'feminin_sup': feminin_sup,
        'taux_analphabete_rur': taux_analphabete_rur,
        'taux_analphabete_urb': taux_analphabete_urb,
        'taux_analphabete_fem': taux_analphabete_fem,
        'taux_analphabete_masc': taux_analphabete_masc,
        'prev_handicap_urb': prev_handicap_urb,
        'prev_handicap_rur': prev_handicap_rur,
        'prev_nhandicap_urb': prev_nhandicap_urb,
        'prev_nhandicap_rur': prev_nhandicap_rur,
        'urbain_celi_total': urbain_celi_total,
        'urbain_mar_total': urbain_mar_total,
        'rural_celi_total': rural_celi_total,
        'rural_mar_total': rural_mar_total,
        'population_masculin': population_masculin,
        'population_fem': population_fem,
        'total_urbains': total_urbains,
        'total_ruraux': total_ruraux,
        'hommes1': hommes1,
        'hommes2': hommes2,
        'hommes3': hommes3,
        'hommes4': hommes4,
        'hommes5': hommes5,
        'hommes6': hommes6,
        'hommes7': hommes7,
        'hommes8': hommes8,
        'femmes1': femmes1,
        'femmes2': femmes2,
        'femmes3': femmes3,
        'femmes4': femmes4,
        'femmes5': femmes5,
        'femmes6': femmes6,
        'femmes7': femmes7,
        'femmes8': femmes8,
        'ages1': ages1,
        'ages2': ages2,
        'ages3': ages3,
        'ages4': ages4,
        'ages5': ages5,
        'ages6': ages6,
        'ages7': ages7,
        'ages8': ages8,
        'handicap_mas': handicap_mas,
        'handicap_fem': handicap_fem,
        'nhandicap_mas': nhandicap_mas,
        'nhandicap_fem': nhandicap_fem,
        
        'h_ages1': h_ages1,
        'h_ages2': h_ages2,
        'h_ages3': h_ages3,
        'h_ages4': h_ages4,
       
        'urbain_div_total': urbain_div_total,
        'urbain_ve_total': urbain_ve_total,
        'rural_ve_total': rural_ve_total,
        'rural_div_total': rural_div_total,
        'celi': celi,
        'mar': mar,
        've': ve,
        'div': div,
        'users': users
    }
    return render(request, "myapp/welcome_admin.html", context)

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
import mysql.connector as sql
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"email: {email}, password: {password}")  # Vérifier les valeurs des données postées

        user = authenticate(request, email=email, password=password)


        if user is not None:
            login(request, user)
            print("User authenticated successfully")  # Vérifier si l'authentification réussit

            # Redirection en fonction du type d'utilisateur (admin ou utilisateur normal)
            if email =="asma@gmail.com" and password == 2004:
                request.session['user_name'] = "chaaib asmae "
                request.session['message'] = 'You are now logged in as admin.'
                return redirect('welcome_admin.html')
            else:
                request.session['user_name'] = f"{user.first_name} {user.last_name}"
                request.session['message'] = 'You are now logged in.'
                return redirect('welcome.html')
        else:
            messages.error(request, 'Invalid email or password.')
            print("Authentication failed")  # Vérifier si l'authentification a échoué

    return render(request, 'myapp/index.html')



def  signout(request):
    logout(request)
    return redirect('../')


# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def add_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        cin = request.POST.get('cin')
        password = request.POST.get('password')
        
        try:
            user = User.objects.create_user(email=email, nom=nom, prenom=prenom, cin=cin, password=password)
            return JsonResponse({'status': 'success', 'message': 'Utilisateur créé avec succès'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Méthode de requête invalide'})

def tab_users(request):
    users = User.objects.all()
    return render(request, 'myapp/tab_users.html', {'users': users})
 

def user_del(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user = User.objects.get(id=user_id)
        user.delete()
    return render(request, 'myapp/welcome_admin.html')
def user_update(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        email = request.POST.get('email')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        cin = request.POST.get('cin')

        user = get_object_or_404(User, id=user_id)
        user.email = email
        user.nom = nom
        user.prenom = prenom
        user.cin = cin
        user.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})


from django.shortcuts import render
import mysql.connector as sql

def signaction(request):
    if request.method == "POST":
        # Récupérer les données POST
        fn = request.POST.get('prenom', '')
        ln = request.POST.get('nom', '')
        s = request.POST.get('cin', '')
        em = request.POST.get('email', '')
        pwd = request.POST.get('password', '')

        try:
            # Connexion à la base de données MySQL
            conn = sql.connect(host="localhost", user="root", passwd="root", database="mydata")
            cursor = conn.cursor()

            # Construction de la requête SQL avec des paramètres sécurisés
            query = "INSERT INTO users (prenom, nom, cin, email, password) VALUES (%s, %s, %s, %s, %s)"
            values = (fn, ln, s, em, pwd)

            # Exécution de la requête SQL avec les paramètres
            cursor.execute(query, values)

            # Commit des modifications dans la base de données
            conn.commit()

            # Fermeture de la connexion
            cursor.close()
            conn.close()

            # Message de succès à afficher à l'utilisateur
            success_message = "Inscription réussie !"
            return render(request, 'myapp/signup.html', {'success_message': success_message})
            
        except sql.Error as e:
            # En cas d'erreur lors de la connexion ou de l'exécution de la requête SQL
            error_message = f"Erreur lors de l'inscription : {e}"
            return render(request, 'myapp/signup.html', {'error_message': error_message})

    return render(request, 'myapp/signup.html')

