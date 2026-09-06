import plotly.express as px
import pandas as pd

# Chargement des données
données = pd.read_csv(
    'https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv'
)

# --------------------------------------------------
# 1. Exemple fourni : quantité vendue par région
# --------------------------------------------------

figure_region = px.pie(
    données,
    values='qte',
    names='region',
    title='Quantité vendue par région'
)

figure_region.write_html('ventes-par-region.html')

print('ventes-par-region.html généré avec succès !')


# --------------------------------------------------
# 2. Quantité vendue par produit
# --------------------------------------------------

ventes_par_produit = données.groupby(
    'produit',
    as_index=False
)['qte'].sum()

figure_produit = px.bar(
    ventes_par_produit,
    x='produit',
    y='qte',
    title='Quantité vendue par produit',
    labels={
        'produit': 'Produit',
        'qte': 'Quantité vendue'
    }
)

figure_produit.write_html('ventes-par-produit.html')

print('ventes-par-produit.html généré avec succès !')


# --------------------------------------------------
# 3. Chiffre d'affaires par produit
# --------------------------------------------------

données['chiffre_affaires'] = données['prix'] * données['qte']

ca_par_produit = données.groupby(
    'produit',
    as_index=False
)['chiffre_affaires'].sum()

figure_ca = px.bar(
    ca_par_produit,
    x='produit',
    y='chiffre_affaires',
    title="Chiffre d'affaires par produit",
    labels={
        'produit': 'Produit',
        'chiffre_affaires': "Chiffre d'affaires (€)"
    }
)

figure_ca.write_html('chiffre-affaires-par-produit.html')

print('chiffre-affaires-par-produit.html généré avec succès !')