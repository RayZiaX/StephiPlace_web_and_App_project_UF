<?php
    include_once('./php/traitement.php');
    $menus = getMenus();
?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./css/styleMenu.css">
    <link rel="stylesheet" href="./css/styleMain.css">
    <link rel="stylesheet" href="./css/styleAsset.css">
    <link rel="shortcut icon" href="favIcon.ico" type="image/x-icon">

    <title>Stephi Place - Accueil</title>
</head>

<body>
    <?php
        echo $menus;
    ?>
    <div class="formulaire">
        <form action="./pages/recherche.php" method="GET">
            <div class="entrer">
                <input type="text" placeholder="budget" class="input" name="budget">
                <input type="text" placeholder="Lieux" class="input" name="lieux">
            </div>
            <div class="formulaire-accueil">
                <div class="type">
                    <select name="typeB" id="type-bien" class="select">
                        <option value="">Votre type de biens</option>
                        <option value="appartement">Appartement</option>
                        <option value="maison">Maison</option>
                    </select>
                </div>

                <button type="submit" id="envoie" name="envoi" class="btn btn-hover">Rechercher</button>
            </div>
            <!-- <div class="type">
                <div class="radio_1">
                    <input type="radio" name="Apartement" id="Apart" class="radio biens">
                    <label for="Apart" class="label">Apartement</label>
                </div>
                <div class="radio_2">
                    <input type="radio" name="Maison" id="Maison" class="radio biens">
                    <label for="Maison" class="label">Maison</label>
                </div> -->
    </div>
    </form>
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