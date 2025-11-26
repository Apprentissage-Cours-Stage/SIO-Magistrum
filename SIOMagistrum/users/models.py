from django.db import models
from django.contrib.auth.models import User


# ------------------------------------------------------------------
# Année scolaire
# ------------------------------------------------------------------
class AnneeScolaire(models.Model):
    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


# ------------------------------------------------------------------
# Options (spécialisation de 2ème année par exemple)
# ------------------------------------------------------------------
class Option(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


# ------------------------------------------------------------------
# Élève
# ------------------------------------------------------------------

class Eleve(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='eleve')
    photo = models.ImageField(upload_to='photos_eleves/', blank=True, null=True)
    pseudo = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    annee_scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.PROTECT, related_name='eleves')
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, blank=True, null=True, related_name='eleves') #Uniquement si annee_scolaire = 2

    def save(self, *args, **kwargs):
        if self.annee_scolaire and self.annee_scolaire.nom != "2ème année":
            self.option = None
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.pseudo} (Élève)"

# ------------------------------------------------------------------
# Matière
# ------------------------------------------------------------------

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    annee_scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.PROTECT, related_name='matieres')
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, blank=True, null=True, related_name='matieres')

    def __str__(self):
        return self.nom

# ------------------------------------------------------------------
# Professeur
# ------------------------------------------------------------------

class Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professeur')
    photo = models.ImageField(upload_to='photo_profs/', blank=True, null=True)
    pseudo = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    matieres = models.ManyToManyField('Matiere', related_name='professeurs')

    def __str__(self):
        return f"{self.pseudo} (Professeur)"