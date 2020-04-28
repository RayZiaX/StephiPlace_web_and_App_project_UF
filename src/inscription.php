<?php

?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/styleMain.css" />
    <link rel="stylesheet" href="./css/styleMenu.css">
    <link rel="stylesheet" href="./css/styleFormulaire.css" />
    <link rel="stylesheet" href="./css/styleAsset.css">
    <link rel="shortcut icon" href="./favIcon.ico" type="image/x-icon">
    <title>Stephi Place - inscription</title>
</head>

<body>
    <div class="form">
        <form action="../php/traitement.php" method="POST" id="myform">
            <fieldset>
                <legend>Stephi Place - Formulaire d'inscription</legend>
                <label for="identifiant" class="label-form">Votre identifiant<i class="imporant">*</i></label><input type="text"
                    name="identifiant" id="identifiant"><br>
                <label for="mdp" class="label-form">Votre mot de passe<i class="imporant">*</i></label><input type="password" name="mdp"
                    id="mdp"><br>
                <label for="mdp" class="label-form">confirmer le mot de passe</label><input type="password" name="confirm_mdp"
                    id="confirm_mdp"><br>
                <label for="nom" class="label-form">Nom<i class="imporant">*</i> </label><input type="text" name="nom" id="nom"
                    class="nom" /><br>
                <label for="prenom" class="label-form">Prenom<i class="imporant">*</i></label><input type="text" name="prenom" id="prenom"
                    class="prenom" /><br>
                <label for="email" class="label-form">Email<i class="important">*</i></label><input type="email" name="email" id="email"
                    class="email" /><br>
                <label for="img">Image de profil: <input type="file" name="img" id="img"></label><br>
                <label for="telephone">téléphone: <input type="text" name="telephone" id="telephone"></label><br>
                <label for="age" class="label-form">votre age<i class="important">*</i></label><input type="text" name="age" id="age"
                    class="age" /><br>
                <label for="civilite" class="label-form">Civilité
                    <select name="civilite" id="civilite">
                        <option value="homme">Homme</option>
                        <option value="femme">Femme</option>
                        <option value="autre">Autre</option>
                    </select>
                </label>
            </fieldset>
            <fieldset class="formulaire second">
                <textarea name="description" id="description" cols="30" rows="10"
                    placeholder="descritpion optionel de vous, peut etre modifier plus tard"></textarea><br>
                <input type="checkbox" name="condition" id="condition" /> en cochant vous acceptez <a href="#">les
                    conditions d'utilisation du site</a><br>
                <input type="submit" value="s'inscrire" name="iscription">

            </fieldset>
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