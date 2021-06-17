## Requête de base
Cette requête permet de récupérer les noms, les titres des oeuvres ainsi que la date de publication de ces dernières pour chaque récipendiaire ayant un identifiant BnF. 
Tous les récipendiaites ayant un identifiant BnF ne sont pas tous présents dans cette requête. Le SPARQL de la BnF permet une quantité de valeurs limitées. Nous avons donc répété l'opération cinq fois, ce qui nous a permis de récupérer toutes les données pour chaque récipendiaire. Toutes les URI BnF de tous les récipendaires en possédant un sont disponibles dans le fichier [`lot_URIbnf.csv`](sparql/lot_URIbnf.csv). 
```SQL
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX bnf-onto: <http://data.bnf.fr/ontology/bnf-onto/>
PREFIX rdagroup1elements: <http://rdvocab.info/Elements/>
PREFIX dcterms: <http://purl.org/dc/terms/>
SELECT ?name ?title ?date ?s
WHERE {VALUES ?s {<http://data.bnf.fr/ark:/12148/cb13006789j> <http://data.bnf.fr/ark:/12148/cb12459909x> <http://data.bnf.fr/ark:/12148/cb12943930z> <http://data.bnf.fr/ark:/12148/cb10593907h> <http://data.bnf.fr/ark:/12148/cb16205590q> <http://data.bnf.fr/ark:/12148/cb13163220w> <http://data.bnf.fr/ark:/12148/cb122811886> <http://data.bnf.fr/ark:/12148/cb15241827h> <http://data.bnf.fr/ark:/12148/cb17774991c> <http://data.bnf.fr/ark:/12148/cb11926319z> <https://data.bnf.fr/ark:/12148/cb11065267k> <https://data.bnf.fr/ark:/12148/cb130786656> <https://data.bnf.fr/ark:/12148/cb12250901n> <https://data.bnf.fr/ark:/12148/cb12287936m> <https://data.bnf.fr/ark:/12148/cb13008872k> <https://data.bnf.fr/ark:/12148/cb13962361w> <https://data.bnf.fr/ark:/12148/cb135129714> <https://data.bnf.fr/ark:/12148/cb121468483> <https://data.bnf.fr/ark:/12148/cb149696815> <https://data.bnf.fr/ark:/12148/cb11499224k> <https://data.bnf.fr/ark:/12148/cb12459373c> <https://data.bnf.fr/ark:/12148/cb11909525r> <https://data.bnf.fr/ark:/12148/cb137418393> <https://data.bnf.fr/ark:/12148/cb10720941v> <https://data.bnf.fr/ark:/12148/cb15290882f> <https://data.bnf.fr/ark:/12148/cb110474018> <https://data.bnf.fr/ark:/12148/cb12529045v> <https://data.bnf.fr/ark:/12148/cb10726918s> <https://data.bnf.fr/ark:/12148/cb13211614q> <https://data.bnf.fr/ark:/12148/cb13164460x> <https://data.bnf.fr/ark:/12148/cb16549649v> <https://data.bnf.fr/ark:/12148/cb104026120> <https://data.bnf.fr/ark:/12148/cb110212266> <https://data.bnf.fr/ark:/12148/cb13007268f> <https://data.bnf.fr/ark:/12148/cb12567508c> <https://data.bnf.fr/ark:/12148/cb12738449n> <https://data.bnf.fr/ark:/12148/cb12337301f> <https://data.bnf.fr/ark:/12148/cb12429519h> <https://data.bnf.fr/ark:/12148/cb10074289q> <https://data.bnf.fr/ark:/12148/cb134242811> <https://data.bnf.fr/ark:/12148/cb10528554p> <https://data.bnf.fr/ark:/12148/cb10217045c> <https://data.bnf.fr/ark:/12148/cb11910531q> <https://data.bnf.fr/ark:/12148/cb127569598> <https://data.bnf.fr/ark:/12148/cb124881229>}
?s foaf:focus ?creator. 
?work dcterms:creator ?creator ; 
      dcterms:title ?title;
      dcterms:date ?date.
?creator foaf:name ?name.
}
GROUP BY ?name ?s
```