from django.db import models
from django.contrib.auth.models import User

'''
Modèle Élève
'''

class Eleve(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='eleve')
    pseudo = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    annee_scolaire = models.IntegerField()
    option = models.CharField(max_length=50, blank=True, null=True) #Uniquement si annee_scolaire = 2

    def save(self, *args, **kwargs):
        if self.annee_scolaire != 2:
            self.option = None
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.pseudo} (Élève)"

'''
Modèle Matière
'''

class Matiere(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


'''
Modèle Professeur
'''

class Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professeur')
    pseudo = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    matieres = models.ManyToManyField(Matiere, blank=True)

    def __str__(self):
        return f"{self.pseudo} (Professeur)"