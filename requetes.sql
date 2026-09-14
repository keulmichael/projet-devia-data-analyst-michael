-- ============================================================
-- Projet Simplon - Analyser les ventes d'une PME
-- Table attendue : ventes
-- Colonnes : date, produit, prix, qte, region
-- ============================================================

-- 1. Vérifier que l'import du fichier CSV a fonctionné
SELECT *
FROM ventes;

-- 2. Chiffre d'affaires total
-- Le chiffre d'affaires d'une ligne = prix * quantité vendue
SELECT
    SUM(prix * qte) AS chiffre_affaires_total
FROM ventes;

-- Résultat attendu avec le fichier ventes.csv : 44825

-- 3. Ventes par produit
-- Ici, "ventes" correspond au nombre total d'unités vendues.
SELECT
    produit,
    SUM(qte) AS ventes
FROM ventes
GROUP BY produit
ORDER BY produit;

-- Résultats attendus :
-- Produit A : 1750
-- Produit B : 1055
-- Produit C : 575

-- 4. Ventes par région
SELECT
    region,
    SUM(qte) AS ventes
FROM ventes
GROUP BY region
ORDER BY region;

-- Résultats attendus :
-- Nord : 1605
-- Sud  : 1775

-- 5. Chiffre d'affaires par produit
-- Cette requête sera utile pour le graphique Python demandé dans le brief.
SELECT
    produit,
    SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY produit
ORDER BY produit;

-- Résultats attendus :
-- Produit A : 17500
-- Produit B : 15825
-- Produit C : 11500

-- 6. Optionnel : chiffre d'affaires par région
-- Non exigé dans les trois questions SQL du brief, mais utile pour approfondir l'analyse.
SELECT
    region,
    SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY region
ORDER BY region;
