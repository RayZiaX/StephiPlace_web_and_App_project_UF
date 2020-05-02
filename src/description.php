<?php
    include_once('./php/traitement.php');
    $menus = getMenus();
    $description = getDescription($cnx);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/styleMain.css"/>
    <link rel="stylesheet" href="./css/styleMenu.css">
    <link rel="stylesheet" href="./css/styleAsset.css">
    <title>StephiPlace - Description</title>
</head>

<body>
    <?php
        echo $menus;
        echo $description;
    ?>
    


</body>

</html>