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
    #Niveau utilisé en cas de Cours Standard/Approfondissement
    niveau_module = models.PositiveIntegerField(
        choices=[(1, 'Débutant'), (2, 'Intermédiaire'), (3, "Avancé")],
        null=True, blank=True
    )
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

class Exercice(models.Model):
    TYPES = [
        ('QCM', 'Questionnaire à choix multiples'),
        ('CODE', 'Exercice de programmation'),
    ]
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='exercices')
    titre = models.CharField(max_length=150)
    enonce = models.TextField()
    type_exercice = models.CharField(max_length=10, choices=TYPES)
    #Niveau utilisée en cas de Test de Positionnement
    niveau_exercice = models.PositiveIntegerField(
        choices=[(1, 'Débutant'), (2, 'Intermédiaire'), (3, "Avancé")],
        null=True, blank=True
    )
    def __str__(self):
        return f"{self.titre} - {self.type_exercice}"

# --- Exercice Type QCM ---

class QuestionQCM(models.Model):
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE, related_name='questions')
    texte = models.TextField()

class Choix(models.Model):
    question = models.ForeignKey(QuestionQCM, on_delete=models.CASCADE, related_name='choix')
    texte = models.CharField(max_length=255)
    est_correct = models.BooleanField(default=False)

# --- Exercice Type Programmation ---

class ExerciceCode(models.Model):
    LANGUAGES = [
        ('python', 'Python'),
        ('java', 'JAVA'),
        ('javascript', 'Javascript'),
        ('php', 'PHP'),
        ('html', 'HTML/CSS'),
    ]
    exercice = models.OneToOneField(Exercice, on_delete=models.CASCADE, related_name='contenu_code')
    langage = models.CharField(max_length=20, choices=LANGUAGES)
    code_initial = models.TextField(blank=True, help_text="Code affiché au début")
    solution_attendue = models.TextField(help_text="Code de référence ou résultat attendu")