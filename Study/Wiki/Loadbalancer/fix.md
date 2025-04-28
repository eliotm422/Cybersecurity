
Cette partie sert à régler les différentes vulnérabilités (en plus)

# Le robots.txt

Modifier le fichier 
vim /var/www/html/robots.txt :
```bash
User-agent: *
Disallow: /
```
Ces actions permettent d'éviter de récupérer les données
# Fix le DOS sur nginx

Ajouter sur le fichier qui gère le load :

```nignx
http {
    limit_req_zone $binary_remote_addr zone=one:10m rate=5r/s;

    server {
        location / {
            limit_req zone=one burst=10 nodelay;
        }
    }
}

```
Mets une limite sur les requêtes reçues pour éviter la surcharge


# Fix les injections SQL

```sql
<?php
// Affiche toutes les erreurs PHP
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Connexion
$servername = "localhost";
$username = "sqli";
$password = "sqli123";
$dbname = "test";

$conn = new mysqli($servername, $username, $password, $dbname);

// Vérifier connexion
if ($conn->connect_error) {
    die("Connexion échouée : " . $conn->connect_error);
}

// Lire paramètre
if (isset($_GET['username'])) {
    $user = $_GET['username'];

    // Préparation de la requête sécurisée
    $stmt = $conn->prepare("SELECT id, username FROM users WHERE username = ?");
    $stmt->bind_param("s", $user);
    $stmt->execute();

    $result = $stmt->get_result();

    if ($result && $result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "ID: " . htmlspecialchars($row["id"]) . " - Username: " . htmlspecialchars($row["username"]) . "<br>";
        }
    } else {
        echo "Aucun utilisateur trouvé.";
    }

    $stmt->close();
} else {
    echo "Utilisez ?username=admin dans l'URL pour tester.";
}

$conn->close();
?>

```


La partie :
```sql

// Préparation de la requête sécurisée
    $stmt = $conn->prepare("SELECT id, username FROM users WHERE username = ?");
    $stmt->bind_param("s", $user);
    $stmt->execute();

    $result = $stmt->get_result();
```


Permet de générer des requêtes sécurisées (fonction de php)