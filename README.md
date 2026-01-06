# SIO-Magistrum

Plateforme e-learning développée dans le cadre du **BTS SIO – Projet de deuxième année (B2)**.

---

## Présentation

**SIO-Magistrum** est une plateforme pédagogique conçue dans le cadre du  
**BTS Services Informatiques aux Organisations (SIO)**, option **SLAM**.

L’objectif du projet est de proposer un environnement e-learning permettant aux étudiants d’accéder à des **cours**, **ressources pédagogiques** et **outils d’apprentissage**, au sein d’une application web moderne, structurée et évolutive.

Ce projet a été pensé comme un travail de **B2**, visant à démontrer :

- la maîtrise du framework **Django** ;
- la structuration complète d’un projet web professionnel ;
- la mise en place d’un environnement de développement propre et maintenable ;
- l’utilisation d’outils standards du monde professionnel (Docker, GitHub Actions).

---

## État d’avancement du projet

Le projet est **fonctionnel dans sa base**, mais **non finalisé** à ce stade.

Certaines parties, notamment la **containerisation avec Docker**, sont encore en cours de conception et d’intégration.

> Par manque de temps dans le cadre du BTS, l’ensemble des fonctionnalités initialement prévues n’a pas pu être implémenté.  
> Le projet a néanmoins été conçu pour être **repris, étendu et amélioré**, et sera poursuivi ultérieurement.

Cette démarche met en évidence la capacité à :

- planifier un projet informatique ;
- prioriser les fonctionnalités essentielles ;
- documenter clairement les limites et perspectives ;
- démontrer une volonté d’évolution et d’amélioration continue.

---

## Fonctionnalités actuelles

- Gestion des **cours** et **modules pédagogiques**
- Espace utilisateur (**étudiants (Commencée) / enseignants**)
- Suivi des activités
- Architecture Django structurée (apps, modèles, vues, templates)
- Début d’intégration **Docker** (non finalisée)

---

## Technologies utilisées

| Technologie | Rôle |
|------------|------|
| Python / Django | Backend et logique métier |
| HTML / CSS / JavaScript | Interface utilisateur |
| Docker (en cours) | Environnement isolé et déploiement |
| GitHub Actions | Automatisation CI/CD |

---

## Structure du projet

SIOMagistrum/<br>
├── manage.py<br>
├── requirements.txt<br>
├── SIOMagistrum/ # Configuration principale Django<br>
│ ├── settings.py<br>
│ ├── urls.py<br>
│ └── wsgi.py<br>
├── dashboards/ # Application dashboard (seulement professeur)<br>
├── executor/ # Execution Docker (Finalisée mais non-fonctionnel)<br>
├── home/ # Page d'accueil<br>
├── users/ # Connexion / Inscription<br>
├── media/ # Photos lors de la créations<br>
└── static/ # Fichiers statiques (CSS, JS, images)<br>
README.md<br>
.gitignore

---

## Perspectives d’évolution

- Finalisation de la containerisation Docker
- Passage complet à PostgreSQL
- Amélioration du suivi pédagogique
- Gestion avancée des rôles et permissions
- Enrichissement des contenus pédagogiques
- Déploiement automatisé

---

## Contexte pédagogique

Projet réalisé dans le cadre du **BTS SIO – option SLAM**,  
épreuve **E6 / Projet B2**.

Ce dépôt constitue un support de démonstration des compétences acquises en :

- développement web ;
- architecture logicielle ;
- organisation de projet ;
- bonnes pratiques professionnelles.

---

## Licence

Projet à vocation pédagogique.  
Toute réutilisation doit mentionner le contexte académique du projet.
