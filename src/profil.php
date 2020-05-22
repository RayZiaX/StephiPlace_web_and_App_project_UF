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
    <link rel="stylesheet" href="./css/styleProfil.css">
    <title>Stephiplace - Profil de <?php echo htmlentities($_SESSION['userName'])?></title>
</head>
<body>
    <?php
        echo $menus;
    ?>
    <div class="profil">
    <?php
        echo $donnee;
        echo $warn;
    ?>
    </div>
    <footer>
        <div class="contenu">
            <div class="contenu-footer copyright">
                <p class="copyright">©all right reserved</p>
            </div>
            <div class="contenu-btn">
                <a href="" class="btn">Nous contacter</a>
                <a href="" class="btn">Réseaux</a>
            </div>
        </div>
    </footer>
</body>
</html>