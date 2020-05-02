<?php
    include_once('./php/traitement.php');
    $menus = getMenus();
    $agence = getAgences($cnx);
    $agences = getAgence($agence);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/styleMain.css" />
    <link rel="stylesheet" href="./css/styleMenu.css">
    <link rel="stylesheet" href="./css/styleAsset.css">
    <link rel="stylesheet" href="./css/styleAnnonce.css">
    <title>StephiPlace - Agence</title>
    <!-- <?php echo $AGENCE;?> -->
</head>

<body>
    <?php
        echo $menus;


    ?>
    <div>
        <?php
        foreach ($agences as $value) {
            echo $value;
        }
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