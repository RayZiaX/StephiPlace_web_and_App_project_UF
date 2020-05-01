<?php
include_once('./php/traitement.php');
$menus = getMenus();
$type = getTypeBien($cnx);
$tabBiens = annonces($cnx);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/styleMain.css"/>
    <link rel="stylesheet" href="./css/styleMenu.css">
    <link rel="stylesheet" href="./css/styleAsset.css">
    <link rel="stylesheet" href="./css/styleAnnonce.css">
    <title>Stephiplace - annonce</title>
</head>
<body>
    <?php
        echo $menus;
    ?>

    <div>
    <div class="formulaire">
        <form action="./php/traitement.php" method="GET">
            <div class="entrer">
                <input type="text" placeholder="budget MIN" class="input" name="budgetmin">
                <input type="text" placeholder="budget MAX" class="input" name="budgetmax">
                <input type="text" placeholder="surface MIN" class="input" name="surfacemin">
                <input type="text" placeholder="surface MAX" class="input" name="surfacemax">
                <input type="text" name="pieces" placeholder="nombre de pièces" class="input" id="piece">
                <input type="text" placeholder="Lieux" class="input" name="lieux">
            </div>
            <div class="formulaire-accueil">
                <div class="type">
                    <select name="typeB" id="type-bien" class="select">
                        <option value="none">Votre type de biens</option>
                        <?php
                            foreach ($type as $value) {
                                echo $value;
                            }
                        ?>
                    </select>
                </div>
                <input type="submit" value="recherche" name="envoi" class="btn btn-hover">
            </div>
    </div>
    </form>
    </div>
        <?php
            foreach ($tabBiens as $value) {
                echo $value;
            }
        ?>
    </div>

</body>
</html>