use IDF;
SELECT
  TABLE_NAME AS 'Table',
  ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024) AS `Taille (kB)`
FROM
  information_schema.TABLES
WHERE
  TABLE_SCHEMA = "IDF" #NOM DE LA BDD
ORDER BY
  (DATA_LENGTH + INDEX_LENGTH)
DESC;

OPTIMIZE TABLE Coordonnees_geo, Distance_velo, Distance_voiture, Distance_voiture_pointe, Temps_transport, Temps_velo, Temps_voiture, Temps_voiture_pointe, Villes;
