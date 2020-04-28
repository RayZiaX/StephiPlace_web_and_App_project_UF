<?php
    include_once('../php/traitement.php');
    $menus = getMenus();
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profil - <?php echo htmlentities($_SESSION['userName'])?></title>
</head>
<body>
    <?php
        echo $menus;
    ?>
    
</body>
</html>