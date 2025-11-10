from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
 
# myapp/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, nom, prenom, cin, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, nom=nom, prenom=prenom, cin=cin, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nom, prenom, cin, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nom, prenom, cin, password, **extra_fields)

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=255)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    cin = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'cin']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def get_full_name(self):
        return f'{self.nom} {self.prenom}'

    @property
    def get_short_name(self):
        return self.prenom

    class Meta:
        db_table = 'users'



class Population(models.Model):
    N_ROW = models.AutoField(primary_key=True)
    
    SEXE = models.CharField(max_length=10)
    AGES = models.CharField(max_length=10)
    MIL = models.CharField(max_length=10)
    E_MAT = models.CharField(max_length=20)
    SIT_HANDICAP = models.CharField(max_length=50)
    
    NIV_ET_AGR = models.CharField(max_length=50)

    class Meta:
        db_table = 'individu_final'

    def age_range_tuple(self):
        start, end = self.age_range.split('-')
        return int(start), int(end)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User  # Assurez-vous d'importer le modèle User

@csrf_exempt
def user_update(request):
    if request.method == 'POST':
        try:
            # Récupérer les données de la requête POST
            id = request.POST.get('id')
            email = request.POST.get('email')
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            cin = request.POST.get('cin')

            # Récupérer l'utilisateur et mettre à jour les informations
            user = User.objects.get(pk=id)
            user.email = email
            user.nom = nom
            user.prenom = prenom
            user.cin = cin
            user.save()
            
            # Retourner une réponse JSON indiquant le succès
            return JsonResponse({'status': 'success', 'message': 'Utilisateur mis à jour avec succès'})
        
        except User.DoesNotExist:
            # Retourner une réponse JSON indiquant que l'utilisateur n'a pas été trouvé
            return JsonResponse({'status': 'error', 'message': 'Utilisateur non trouvé'})
    
    # Retourner une réponse JSON indiquant que la méthode de requête est invalide
    return JsonResponse({'status': 'error', 'message': 'Méthode de requête invalide'})
