# Bugs trouvés et corrigés

| # | Problème | Comment le reproduire | Branche | Statut |
|---|----------|----------------------|---------|--------|
| 1 | Email inconnu : erreur 500 (IndexError) | Page d'accueil, saisir un email absent de clubs.json | bug/unknown-email | corrigé, fusionné |
| 2 | Réserver plus de places que de points | Iron Temple (4 points) réserve 10 places | bug/places-over-points | corrigé, fusionné |
| 3 | Les points ne sont pas déduits après une réservation | Après la réservation, les points restent à 4 | bug/points-not-deducted | corrigé, fusionné |
| 4 | Réserver plus de places qu'il n'en reste (-1 place) | Fall Classic (13 places) : en réserver 14 | bug/places-over-available | corrigé, fusionné |
| 5 | Plus de 12 places par compétition | Réserver 13 places d'un coup | bug/max-12-places | corrigé, fusionné |
| 6 | Plus de 12 places au total en plusieurs réservations | Réserver 8 puis encore 8 places | bug/max-12-cumulative | corrigé, fusionné |
| 7 | Réserver une compétition déjà passée | Spring Festival et Fall Classic sont datées de 2020 | bug/past-competitions | corrigé, fusionné |

## Fonctionnalité
| Fonctionnalité | Branche | Statut |
|----------------|---------|--------|
| Tableau public des points des clubs (`/points`) | feature/points-board | corrigé, fusionné |

## Méthode pour chaque bug
1. Reproduire à la main
2. Créer une branche `bug/...`
3. Écrire un test qui échoue
4. Corriger le code
5. Le test passe : commit, puis fusion dans `master`