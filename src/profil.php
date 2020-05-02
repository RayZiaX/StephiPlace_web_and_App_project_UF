<?php
    include_once('./php/traitement.php');
    $menus = getMenus();
    $donnee = infoCompte($cnx);
    $warn = ModifInfo($cnx);
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/styleMenu.css">
    <link rel="stylesheet" href="./css/styleMain.css">
    <link rel="stylesheet" href="./css/styleAsset.css">
    <title>Stephiplace - Profil de <?php echo htmlentities($_SESSION['userName'])?></title>
</head>
<body>
    <?php
        echo $menus;
        echo $donnee;
        echo $warn;
    ?>
</body>
</html>