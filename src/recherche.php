

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/styleMenu.css">
    <link rel="stylesheet" href="../css/styleMain.css">
    <link rel="stylesheet" href="../css/styleAsset.css">
    <link rel="shortcut icon" href="../favIcon.ico" type="image/x-icon">
    <?php
    $budget ="";
    $lieux ="";
    $typeBien ="";
    if (isset($_GET['envoi'])){
        $budget = $_GET['budget'];
        $lieux = $_GET['lieux'];
        $typeBien = $_GET['typeB'];
    };
    if($budget == ""){$budget = "N/A";}if($lieux == ""){$lieux = "N/A";}?>
    <title>Stephi Place - recherche</title>
</head>

<body>
    <header>
        <div class="contenu-header">
            <div class="header-img">
                <a href="../index.html"><img src="../img/Logo100x100sans_fond.png" alt="StephiPlace_logo"></a>
            </div>
            <div class="body">
                <div class="contenu contenu-btn-menu">
                    <div>
                        <a href="../pages/inscription.html">S'inscrire</a>
                    </div>
                    <div>
                        <a href="../pages/connexion.html">Se connecter</a>
                    </div>
                </div>
                <div class="contenu-menu">
                    <nav>
                        <ul>
                            <li><a href="#">FAQ</a></li>
                            <li><a href="#">Biens immobiliers</a></li>
                            <li><a href="../pages/agence.html">Agence</a></li>
                            <!-- <li></li> -->
                        </ul>
                    </nav>
                </div>
            </div>
        </div>
    </header>
    <div class="formulaire-review">
        <form action="recherche.php">
            <div class="entrer">
                <input type="text" placeholder="budget" class="input" name="budget" value="<?php echo $budget?>">
                <input type="text" placeholder="Lieux" class="input" name="lieux" value="<?php echo $lieux?>">
                <select name="typeB" id="type-bien" class="select" value="<?php echo $typeBien?>">
                    <option value="">Votre type de biens</option>
                    <option value="appartement">Appartement</option>
                    <option value="maison">Maison</option>
                </select>
                <button type="submit" id="envoi" name="envoi" class="btn btn-hover">Rechercher</button>

            </div>

        </form>
    </div>
    <div class="recherche">
        <?php for ($i = 0; $i < 6; $i++){
        echo <<< annonce
        <div class="carte btn-hover">
        <div class=" image-annonce">
            <img src="../img/maison_anonce1.jpg" alt="image-annonce"></img>
        </div>
        <div class="information">
            <span class="text">budget: $budget €</span><br>
            <span class="text">lieux: $lieux</span>
            <p class="text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nulla, corporis! Aut, nemo
                corporis tempora perferendis officia dolor temporibus sapiente unde voluptas in laboriosam esse quam
                quis aliquid, eaque qui nisi.</p>
        </div>
        </div>
        annonce;
    }
    ?>
    </div>
    <footer>
        <div class="contenu">
            <div class="contenu-footer copyright">
                <p class="copyright">©all right reserved</p>
            </div>
            <div class="contenu-btn">
                <a href="" class="btn btn-hover">Nous contacter</a>
                <a href="" class="btn btn-hover">Réseaux</a>
            </div>
        </div>
    </footer>
</body>

</html>