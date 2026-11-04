# Bugs trouvés et corrigés

| # | Problème | Branche | Statut |
|---|----------|---------|--------|
| 1 | Email inconnu : erreur 500 (IndexError) | bug/unknown-email | corrigé, fusionné |
| 2 | Réserver plus de places que de points | bug/places-over-points | corrigé, fusionné |
| 3 | Les points ne sont pas déduits après une réservation | | à faire |
| 4 | Réserver plus de places qu'il n'en reste (-1 place) | | à faire |
| 5 | Plus de 12 places par compétition possible | | à faire |
| 6 | Réserver une compétition déjà passée | | à faire |

## Méthode pour chaque bug
1. Reproduire à la main
2. Créer une branche `bug/...`
3. Écrire un test qui échoue
4. Corriger le code
5. Le test passe : commit, puis fusion dans `master`