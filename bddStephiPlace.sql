-- création de la base de donnée
DROP DATABASE IF EXISTS `stephiPlace_data`;
CREATE DATABASE IF NOT EXISTS `stephiPlace_data`;
-- création des table
USE `stephiPlace_data`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users`
(
    `user_id` INT NOT null AUTO_INCREMENT,
    `user_name` VARCHAR(65),
    `user_firstName` VARCHAR(65),
    `user_mail` VARCHAR(65),
    `user_pseudo` VARCHAR(65),
    `user_password` VARCHAR(255),
    `user_age` INT,
    `user_genre` VARCHAR(5),
    `user_tel` VARCHAR(15),
    `user_img` VARCHAR(255)
);ENGINE=InnoDB
DROP TABLE IF EXISTS `type_bien`;
CREATE TABLE IF NOT EXISTS `type_bien`
(
    `id_type_bien` SERIAL PRIMARY KEY,
    `type_bien_name` VARCHAR(255)
);ENGINE=InnoDB
DROP TABLE IF EXISTS `biens`;
CREATE TABLE IF NOT EXISTS `biens`
(
    `biens_id` SERIAL,
    `biens_surface` INT,
    `biens_prix` INT,
    `user_id` INT,
    `id_type_bien` INT,
    `biens_img` VARCHAR(255),
    `biens_description` VARCHAR (255),
    `biens_localisation` VARCHAR(255),
    `agence_id`INT,
    PRIMARY KEY (`agence_id`,`biens_id`)
);ENGINE=InnoDB
DROP TABLE IF EXISTS `agence`;
CREATE TABLE IF NOT EXISTS `agence`
(
    `agence_id` SERIAL PRIMARY KEY,
    `agence_localisation` VARCHAR(255),
    `agence_codePostal` INT,
    `agence_ville` VARCHAR(255)
);ENGINE=InnoDB

INSERT INTO `biens` (`bien_id`,`bien_surface`,`bien_prix`,`user_id`,`id_type_bien`,`bien_img`,`bien_description`,`bien_localisation`,`agence_id`)
VALUES
(1,300,350000,null,2,'/img/maison_anonce1.jpg','petite maison avec un voisinage assez calme avec une piscine et un petit jardin pour les paysants', 'Meyreuil',3),
(2,150,100000,null,1,'/img/maison_anonce3.jpg','Maison avec étage et munie d un garage zone calme très peu de trafic à 10 min d un carrefour market','Gardanne',3),
(3,200,400,null,2,'/img/maison_anonce2.jpg','Appartement avec voisin calme bientôt mort pas de garage ou place de parking','Aix-en-Provence',2),
(4,400,400000,null,1,'/img/maison_carousel3.jpg','Maison plan pied avec beaucoup de trafic mais passède un très grand terrain risque de guerre de gang et de descente de police','Marseille',1)

INSERT INTO `agence` (`agence_id`,`agence_name`,`agence_localisation`)
VALUES
(1,'109 Avenue de la Timone', 13010,' Marseille'),
(2,'57 Rue Espariat', 13100, 'Aix-en-Provence'),
(3,'38 Cours de la République', 13120, 'Gardanne')

