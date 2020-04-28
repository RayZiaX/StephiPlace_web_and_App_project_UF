<?php 

//DELETE FROM users WHERE user_pseudo = 'RayZiaX'
session_start();
$utilisateur = 'root';
$mdp = '';
try{
    $cnx = new PDO('mysql:host=localhost;dbname=stephiplace_data;port=3308',$utilisateur,$mdp);
}catch(Exception $e) {
    print($e->getMessage());
    exit;
}

function getAgences($cnx){
    $tab = [];
    $rqt = "SELECT * FROM agence";
    $stmt = $cnx->prepare($rqt);
    $stmt->execute();
    while($line = $stmt->fetch(PDO::FETCH_ASSOC)){
        array_push($tab,$line);
    }
    return $tab;
}

function getAgence($tab){
    $tabAgence = [];
    for ($i=0; $i < count($tab); $i++) {
        $parts = $tab[$i];
        $localisation = $parts['agence_localisation'];
        $codePostal = $parts['agence_codePostal'];
        $ville = $parts['agence_ville'];
        $img = $parts['agence_img'];
        $agence = "<div><img src='.$img' alt='img_annonce' class='img'></img><div>localisation: $localisation,$codePostal $ville</div></div><br>";
        array_push($tabAgence,$agence);
    }
    return $tabAgence;
}


function getMenus(){
    if (empty($_SESSION['userName']) || $_SESSION['userName'] === null){
        $menus = <<<html
        <header>
        <div class="contenu-header">
        <div class="header-img">
        <a href="index.php"><img src="./img/Logo100x100sans_fond.png" alt="StephiPlace_logo"></a>
        </div>
        <div class="body">
                    <div class="contenu contenu-btn-menu">
                        <div>
                            <a href="inscription.php" class="btn-profil">S'inscrire</a>
                        </div>
                        <div>
                            <a href="connexion.php" class="btn-profil">Se connecter</a>
                        </div>
                    </div>
                    <div class="contenu-menu">
                        <nav>
                            <ul>
                                <li><a href="#">FAQ</a></li>
                                <li><a href="./annonces.php">Biens immobiliers</a></li>
                                <li><a href="agence.php">Agence</a></li>
                                <!-- <li></li> -->
                            </ul>
                        </nav>
                    </div>
                </div>
            </div>
        </header>

    html;
    }elseif($_SESSION['userName']){
        $name = htmlentities($_SESSION['userName']);
        $imageProfil = htmlentities($_SESSION['img_profil']);
        $menus = <<< html
        <header>
            <div class="contenu-header">
                <div class="header-img">
                    <a href="index.php"><img src="./img/Logo100x100sans_fond.png" alt="StephiPlace_logo"></a>
                </div>
                <div class="body">
                    <div class="contenu contenu-btn-menu">
                        <div>
                            <a href="./pages/profil.php" class="btn-profil">Bonjour $name<img src=".$imageProfil" alt="img_profil" class="img-profil"></a>
                        </div>
                        <div>
                            <a href="./pages/deconnexion.php" class="btn-profil">Déconnexion</a>
                        </div>
                    </div>
                    <div class="contenu-menu">
                        <nav>
                            <ul>
                                <li><a href="#">FAQ</a></li>
                                <li><a href="./annonces.php">Biens immobiliers</a></li>
                                <li><a href="./pages/agence.php">Agence</a></li>
                                <!-- <li></li> -->
                            </ul>
                        </nav>
                    </div>
                </div>
            </div>
        </header>
        
    html;
    }
    return $menus;
}

if(!empty($_POST['iscription'])){
    $user = $_POST['identifiant'];
    $mdp = $_POST['mdp'];
    $mdpConfirm = $_POST['confirm_mdp'];
    $prenom = $_POST['nom'];
    $nom = $_POST['prenom'];
    $mail = $_POST['email'];
    $age = $_POST['age'];
    $image = $_POST['img'];
    $tel = $_POST['telephone'];
    $civilite = $_POST['civilite'];
    if(empty($image) && $mdp === $mdpConfirm && !empty($_POST['identifiant']) && !empty($_POST['mdp']) && !empty($_POST['nom']) && !empty($_POST['prenom']) && !empty($_POST['age']) && !empty($_POST['condition']) || $_POST['condition'] === 'on'){
        $img = "/img/default_user.png";
        $password = password_hash($mdp,PASSWORD_DEFAULT);
        $rqt = "INSERT INTO users 
        (user_name,user_firstName,user_mail,user_pseudo,user_password,user_age,user_genre,user_tel,user_img)
        VALUE (:userName, :firstName, :mail, :pseudo, :password, :age, :genre, :tel, :img)";
        $stmt = $cnx->prepare($rqt);
        $stmt->bindParam(':userName',$nom,PDO::PARAM_STR);
        $stmt->bindParam(':firstName',$prenom,PDO::PARAM_STR);
        $stmt->bindParam(':mail',$mail,PDO::PARAM_STR);
        $stmt->bindParam(':pseudo',$user,PDO::PARAM_STR);
        $stmt->bindParam(':password',$password,PDO::PARAM_STR);
        $stmt->bindParam(':age',$age,PDO::PARAM_INT);
        $stmt->bindParam(':img',$img,PDO::PARAM_STR);
        $stmt->bindParam(':tel',$tel,PDO::PARAM_STR);
        $stmt->bindParam(':genre',$civilite,PDO::PARAM_STR);
        $stmt->execute();
        echo "<p>vos données on été enregistrer</p>";
        header('Refresh: 2, url=../index.php');
    }elseif($mdp === $mdpConfirm && !empty($_POST['identifiant']) && !empty($_POST['mdp']) && !empty($_POST['nom']) && !empty($_POST['prenom']) && !empty($_POST['age']) && !empty($image) &&!empty($_POST['condition']) || $_POST['condition'] === 'on'){
        $password = password_hash($mdp,PASSWORD_DEFAULT);
        $img = "/img/".$image;
        $rqt = "INSERT INTO users 
        (user_name,user_firstName,user_mail,user_pseudo,user_password,user_age,user_genre,user_tel,user_img)
        VALUE (:userName, :firstName, :mail, :pseudo, :password, :age, :genre, :tel, :img)";
        $stmt = $cnx->prepare($rqt);
        $stmt->bindParam(':userName',$nom,PDO::PARAM_STR);
        $stmt->bindParam(':firstName',$prenom,PDO::PARAM_STR);
        $stmt->bindParam(':mail',$mail,PDO::PARAM_STR);
        $stmt->bindParam(':pseudo',$user,PDO::PARAM_STR);
        $stmt->bindParam(':password',$password,PDO::PARAM_STR);
        $stmt->bindParam(':age',$age,PDO::PARAM_INT);
        $stmt->bindParam(':img',$img,PDO::PARAM_STR);
        $stmt->bindParam(':tel',$tel,PDO::PARAM_STR);
        $stmt->bindParam(':genre',$civilite,PDO::PARAM_STR);
        $stmt->execute();
        echo "<p>vos données on été enregistrer</p>";
        header('Refresh: 2, url=../index.php');
    }else{
        echo "<p>Veuillez respecter les conditions</p>";
        header("HTTP/1.0 404 Not Found");
    }
}


if (!empty($_POST['connexion'])) {
    $utilisateur = $_POST['user'];
    $passwd = $_POST['password'];
    $rqt = "SELECT * FROM users WHERE user_pseudo = :utilisateur";
    $stmt = $cnx->prepare($rqt);
    $stmt->bindParam(':utilisateur',$utilisateur, PDO::PARAM_STR);
    $stmt->execute();
    $data = $stmt->fetch(PDO::FETCH_ASSOC);
    if(password_verify($passwd, $data['user_password'])){
        $_SESSION['userName'] = $data['user_pseudo'];
        $_SESSION['img_profil'] = $data['user_img'];
        echo "<p>Vous etes bien connecter ".$_SESSION['userName']."</p>";
        header('Refresh: 3; url=../index.php');
    }else{
        echo "Une erreur est arrivée ! Verifiez vos données retour ...";
        header('Refresh: 2; url=../pages/connexion.php');
    }
}

if(!empty($_GET['envoi']) && $_GET['envoi'] === 'recherche'){
    echo "<p>Je recherche les biens </p>";
}elseif(!empty($_POST['envoi']) && $_POST['envoi'] === "s'inscrire"){
    echo"<p>Je m'inscrit !</p>";
}


function getAnnonce($cnx){
    $tab = [];
    $tabAffichage = [];
    $rqt = "SELECT * FROM annonces";
    $stmt = $cnx->prepare($rqt);
    $stmt->execute();
    while($line = $stmt->fetch(PDO::FETCH_ASSOC)){
        array_push($tab, $line);
    }
    for ($i=0; $i < count($tab); $i++) { 
        $parts = $tab[$i];
        $img = $parts['annonce_img'];
        $type = $parts['id_type_bien'];
        $description = $parts['annonce_description'];
        $localisation = $parts['annonce_localisation'];
        $prix = $parts['annonce_prix'];
        $surface = $parts['annonce_surface'];
        $affiche = "<div><img src='.$img' alt='img_annonce'></img><div><span>Prix: $prix, Surface: $surface, localisation: $localisation, type de bien: $type</span></div><div><p>$description</p></div></div><br>";
        array_push($tabAffichage, $affiche);
    }
    return $tabAffichage;
}

?>