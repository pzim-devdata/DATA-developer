Scraping du site : https://pca-cpa.org/

Analyse :
- Nouvelle affaire
- Metadata changée dans la page de la liste des affaires
- Nouveau document ajouté

BeautifullSoup a été utilisé.

Pour fonctionner il faut simplement télécharger le projet en format zip, le décomprésser et le lancer dans le terminal avec la commande "```python PCA_scraping.py```". 

Il faut aussi modifier le fichier Python afin d'y entrer les paramétres SMTP. Les dossiers sont deja créés.

Par ailleurs, vérifier que le swapfile est bien à 0B used à la fin de l'execution du code:
Pour verifier la taille du swap entrez cette commande dans le terminal : sudo swapon --show