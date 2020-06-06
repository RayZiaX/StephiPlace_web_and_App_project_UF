DROP DATABASE IF EXISTS `stephiplace_data`;
CREATE DATABASE IF NOT EXISTS `stephiplace_data`;

USE `stephiplace_data`;



DROP TABLE IF EXISTS `Utilisateurs`;
CREATE TABLE `Utilisateurs`(
   utilisateurs_id INT,
   utilisateur_nom VARCHAR(255),
   utilisateur_prenom VARCHAR(255),
   utilisateur_mdp VARCHAR(255),
   utilisateur_mail VARCHAR(255),
   utilisateur_tel VARCHAR(255),
   utilisateur_genre VARCHAR(255),
   utilisateur_img VARCHAR(255),
   utilisateur_status VARCHAR(255),
   utilisateur_adresse VARCHAR(255),
   utilisateur_ville VARCHAR(255),
   utilisateur_codePostal VARCHAR(255),
   utilisateur_age VARCHAR(50),
   utilisateur_description VARCHAR(50),
   PRIMARY KEY(utilisateurs_id)
);

DROP TABLE IF EXISTS `Agence`;
CREATE TABLE `Agence`(
   agence_id INT,
   agence_nom VARCHAR(255),
   agence_ville VARCHAR(255),
   agence_adresse VARCHAR(255),
   agence_codePostal VARCHAR(255),
   agence_img VARCHAR(255),
   PRIMARY KEY(agence_id)
);

DROP TABLE IF EXISTS `Agent`;
CREATE TABLE `Agent`(
   agent_id INT,
   agent_status VARCHAR(255),
   agence_id INT NOT NULL,
   utilisateurs_id INT NOT NULL,
   PRIMARY KEY(agent_id),
   FOREIGN KEY(agence_id) REFERENCES Agence(agence_id),
   FOREIGN KEY(utilisateurs_id) REFERENCES Utilisateurs(utilisateurs_id)
);

DROP TABLE IF EXISTS `Client`;
CREATE TABLE `Client`(
   client_id INT,
   client_status VARCHAR(255),
   utilisateurs_id INT NOT NULL,
   PRIMARY KEY(client_id),
   FOREIGN KEY(utilisateurs_id) REFERENCES Utilisateurs(utilisateurs_id)
);

DROP TABLE IF EXISTS `Vendeur`;
CREATE TABLE `Vendeur`(
   client_id INT,
   PRIMARY KEY(client_id),
   FOREIGN KEY(client_id) REFERENCES Client(client_id)
);

DROP TABLE IF EXISTS `dependance`;
CREATE TABLE `dependance`(
   dependance_id INT,
   dependance_nom VARCHAR(255),
   PRIMARY KEY(dependance_id)
);

DROP TABLE IF EXISTS `Bien`;
CREATE TABLE `Bien`(
   bien_id INT,
   bien_nom VARCHAR(255),
   bien_img VARCHAR(255),
   bien_adresse VARCHAR(255),
   bien_codePostal VARCHAR(255),
   bien_ville VARCHAR(255),
   bien_prix DECIMAL(25,2),
   bien_description VARCHAR(255),
   bien_surface VARCHAR(255),
   bien_piece VARCHAR(255),
   bien_afficher BOOLEAN,
   bien_type VARCHAR(255),
   agent_id INT NOT NULL,
   client_id INT NOT NULL,
   PRIMARY KEY(bien_id),
   FOREIGN KEY(agent_id) REFERENCES Agent(agent_id),
   FOREIGN KEY(client_id) REFERENCES Vendeur(client_id)
);

DROP TABLE IF EXISTS `Acheteur`;
CREATE TABLE `Acheteur`(
   client_id_1 INT,
   client_id INT,
   PRIMARY KEY(client_id_1),
   FOREIGN KEY(client_id_1) REFERENCES Client(client_id),
   FOREIGN KEY(client_id) REFERENCES Vendeur(client_id)
);

DROP TABLE IF EXISTS `Preferer`;
CREATE TABLE `Preferer`(
   bien_id INT,
   client_id INT,
   PRIMARY KEY(bien_id, client_id),
   FOREIGN KEY(bien_id) REFERENCES Bien(bien_id),
   FOREIGN KEY(client_id) REFERENCES Acheteur(client_id_1)
);

DROP TABLE IF EXISTS `Avoir`;
CREATE TABLE `Avoir`(
   bien_id INT,
   dependance_id INT,
   PRIMARY KEY(bien_id, dependance_id),
   FOREIGN KEY(bien_id) REFERENCES Bien(bien_id),
   FOREIGN KEY(dependance_id) REFERENCES dependance(dependance_id)
);


INSERT INTO `Agence` (`agence_id`,`agence_nom`,`agence_ville`,`agence_adresse`,`agence_codePostal`,`agence_img`)
VALUES (1,'Stephiplace-Marseille','Marseille','109 Avenue de la Timone','13010','/img/agence1.jpg');
INSERT INTO `Agence` (`agence_id`,`agence_nom`,`agence_ville`,`agence_adresse`,`agence_codePostal`,`agence_img`)
VALUES (2,'Stephiplace-Aix-en-Provence','Aix-en-Provence','57 rue Esparia','13100','/img/agence2.jpg');
INSERT INTO `Agence` (`agence_id`,`agence_nom`,`agence_ville`,`agence_adresse`,`agence_codePostal`,`agence_img`)
VALUES (3,'Stephiplace-Gardanne','Gardanne','38 cours de la République','13120','/img/agence3.jpg');

INSERT INTO `dependance` (`dependance_id`,`dependance_nom`) VALUES (1,'garage');
INSERT INTO `dependance` (`dependance_id`,`dependance_nom`) VALUES (2,'piscine');
INSERT INTO `dependance` (`dependance_id`,`dependance_nom`) VALUES (3,'jardin');
INSERT INTO `dependance` (`dependance_id`,`dependance_nom`) VALUES (4,'parking');
INSERT INTO `dependance` (`dependance_id`,`dependance_nom`) VALUES (5,'balcon');

INSERT INTO `bien` ()
