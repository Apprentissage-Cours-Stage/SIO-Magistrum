from django.db import models
from users.models import Professeur, Matiere

class Cours(models.Model):
    TYPE_CHOICES = [
        ('Positionnement', 'Parcours de positionnement'),
        ('Standard', 'Cours')
    ]
    titre = models.CharField(max_length=150)
    banniere = models.ImageField(upload_to='banniere_cours/', blank=True, null=True)
    icon = models.ImageField(upload_to='icon_cours/', blank=True, null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='cours')
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE, related_name='cours')
    type_cours = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Standard')
    date_creation = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titre} ({self.matiere.nom})"
    
class Module(models.Model):
    titre = models.CharField(max_length=150)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='modules')
    description = models.TextField(blank=True, null=True)
    ordre = models.PositiveIntegerField(default=1)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cours','ordre'],
                name="unique_ordre_par_cours"
            )
        ]
        ordering = ['ordre']

    def __str__(self):
        return f"{self.titre} ({self.cours.titre})"