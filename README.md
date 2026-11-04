# Güdlft : portail de réservation

Application Flask permettant aux secrétaires de clubs de réserver des places pour des compétitions de force, avec un tableau public des points.

## Installation

```bash
git clone https://github.com/GuillaumeQuelen/Python_Testing.git
cd Python_Testing
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Lancer le site

```bash
export FLASK_APP=server.py
flask run
```

Puis ouvrir http://127.0.0.1:5000. Exemple d'email : `john@simplylift.co`. Le tableau des points est sur http://127.0.0.1:5000/points.

## Règles de réservation

- un email inconnu affiche un message d'erreur ;
- un club ne peut pas réserver plus de places que ses points ni plus de places qu'il n'en reste ;
- 12 places maximum par compétition et par club (réservations cumulées) ;
- on ne peut pas réserver une compétition déjà passée ;
- les points sont déduits après chaque réservation (1 place = 1 point).

## Tests

```bash
python -m pytest                                # tous les tests
python -m pytest tests/unit tests/integration   # tests rapides
```

- `tests/unit` : tests unitaires
- `tests/integration` : parcours complet
- `tests/functional` : test Selenium (Google Chrome requis)
- `tests/performance` : test de charge Locust

### Couverture

```bash
python -m pytest --cov=server --cov-report=html
```

Le rapport est généré dans `htmlcov/index.html` (couverture actuelle : 100 %).

### Performance (Locust)

Site lancé dans un premier terminal, puis dans un second :

```bash
locust -f tests/performance/locustfile.py --host http://127.0.0.1:5000 --users 6 --spawn-rate 1 --run-time 30s --headless
```

## Anomalies corrigées

Voir `BUGS.md`.