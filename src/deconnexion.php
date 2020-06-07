<?php
include_once('./php/traitement.php');
session_destroy();
header('Refresh: 3;url= ./index.php')
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stéphiplace - Déconnexion</title>
</head>
<body>
    <p>Vous êtes bien déconnecter aurevoir !</p>
</body>
</html>