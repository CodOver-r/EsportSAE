-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : ven. 13 mai 2022 à 01:35
-- Version du serveur : 10.4.21-MariaDB
-- Version de PHP : 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `DBesport`
--

-- --------------------------------------------------------

--
-- Structure de la table `Classement`
--

CREATE TABLE `Classement` (
  `numClassement` int(10) NOT NULL,
  `numCompetition` int(10) NOT NULL,
  `numEquipe` int(10) NOT NULL,
  `Position` varchar(64) NOT NULL,
  `Score` varchar(64) NOT NULL,
  `Gain` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `Classement`
--

INSERT INTO `Classement` (`numClassement`, `numCompetition`, `numEquipe`, `Position`, `Score`, `Gain`) VALUES
(1, 1, 1, '1er', 'Final', 10000),
(2, 1, 2, '2ème', 'Final', 5000),
(3, 1, 3, '3ème', 'Demi-Final', 5000),
(4, 1, 4, '4ème', 'Demi-Final', 5000),
(5, 2, 5, '1er', 'Final', 10000),
(6, 2, 6, '2ème', 'Final', 5000),
(7, 2, 7, '3ème', 'Demi-Final', 5000),
(8, 2, 8, '4ème', 'Demi-Final', 5000),
(9, 3, 1, '1er', 'Final', 10000),
(10, 3, 3, '2ème', 'Final', 5000),
(11, 3, 5, '3ème', 'Demi-Final', 5000),
(12, 3, 7, '4ème', 'Demi-Final', 5000),
(13, 4, 2, '1er', 'Final', 10000),
(14, 4, 4, '2ème', 'Final', 5000),
(15, 4, 6, '3ème', 'Demi-Final', 5000),
(16, 4, 8, '4ème', 'Demi-Final', 5000);

-- --------------------------------------------------------

--
-- Structure de la table `Competition`
--

CREATE TABLE `Competition` (
  `numCompetition` int(10) NOT NULL,
  `nomCompetition` varchar(64) NOT NULL,
  `dateDebut` date NOT NULL,
  `dateFin` date NOT NULL,
  `Web` varchar(255) NOT NULL,
  `Lieu` varchar(64) NOT NULL,
  `Prix` int(10) NOT NULL,
  `Jeu` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `Competition`
--

INSERT INTO `Competition` (`numCompetition`, `nomCompetition`, `dateDebut`, `dateFin`, `Web`, `Lieu`, `Prix`, `Jeu`) VALUES
(1, 'Ligue française de League of Legends', '2022-01-12', '2022-03-31', 'lollfl.com', 'Virtuel', 0, 'League of Legends'),
(2, 'EU Masters', '2022-04-04', '2022-03-07', 'eu.masters.com', 'Virtuel', 0, 'League of Legends'),
(3, 'ESL pro', '2022-04-04', '2022-03-07', 'esl.pro', 'Virtuel', 0, 'Counter Strike: Global Offensive'),
(4, 'World LOL', '2022-04-04', '2022-03-07', 'eu.masters.com', 'Mexico', 0, 'League of Legends');

-- --------------------------------------------------------

--
-- Structure de la table `Equipe`
--

CREATE TABLE `Equipe` (
  `numEquipe` int(10) NOT NULL,
  `nomEquipe` varchar(64) NOT NULL,
  `nbJoueur` int(10) NOT NULL,
  `Logo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `Equipe`
--

INSERT INTO `Equipe` (`numEquipe`, `nomEquipe`, `nbJoueur`, `Logo`) VALUES
(1, 'Kcorp', 5, 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Karmine_Corp_logo.svg/1200px-Karmine_Corp_logo.svg.png'),
(2, 'Vitality', 5, 'https://liquipedia.net/commons/images/5/55/Team_Vitality_2021_allmode.png'),
(3, 'Natus Vincere', 5, 'https://liquipedia.net/commons/images/5/55/Team_Vitality_2021_allmode.png'),
(4, 'Fnatic', 5, 'https://liquipedia.net/commons/images/5/55/Team_Vitality_2021_allmode.png'),
(5, 'Mousesports', 5, 'https://liquipedia.net/commons/images/5/55/Team_Vitality_2021_allmode.png'),
(6, 'Virtus.pro', 5, 'https://liquipedia.net/commons/images/5/55/Team_Vitality_2021_allmode.png'),
(7, 'Evil Geniuses', 5, 'https://liquipedia.net/commons/images/5/55/Team_Vitality_2021_allmode.png'),
(8, 'Cloud9', 5, 'https://liquipedia.net/commons/images/5/55/Team_Vitality_2021_allmode.png');

-- --------------------------------------------------------

--
-- Structure de la table `Joueur`
--

CREATE TABLE `Joueur` (
  `numJoueur` int(10) NOT NULL,
  `numEquipe` int(10) NOT NULL,
  `pseudo` varchar(64) NOT NULL,
  `DateNaissance` date NOT NULL,
  `Email` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `Joueur`
--

INSERT INTO `Joueur` (`numJoueur`, `numEquipe`, `pseudo`, `DateNaissance`, `Email`) VALUES
(1, 1, 'Saken', '1998-11-05', 'saken@kcorp.fr'),
(2, 1, 'Cabochard', '1998-11-05', 'Cabochard@kcorp.fr'),
(3, 1, '113', '1998-11-05', '113@kcorp.fr'),
(4, 1, 'Rekkles', '1998-11-05', 'Rekkles@kcorp.fr'),
(5, 1, 'Hantera', '1998-11-05', 'Hantera@kcorp.fr'),
(6, 2, 'Alphari', '1998-11-05', 'Alphari@Vitality.fr'),
(7, 2, 'Selfmade', '1998-11-05', 'Selfmade@Vitality.fr'),
(8, 2, 'Perkz', '1998-11-05', 'Perkz@vitality.fr'),
(9, 2, 'Carzzy', '1998-11-05', 'Carzzy@vitality.fr'),
(10, 2, 'Labrov', '1998-11-05', 'Labrov@vitality.fr'),
(11, 3, 'BoombI4', '1998-11-05', 'BoombI4@vincere.com'),
(12, 3, 'electronic', '1998-11-05', 'electronic@vincere.com'),
(13, 3, 'b1t', '1998-11-05', 'b1t@vincere.com'),
(14, 3, 'Perfecto', '1998-11-05', 'Perfecto@vincere.com'),
(15, 3, 's1mple', '1998-11-05', 's1mple@vincere.com'),
(16, 4, 'Wunder', '1998-11-05', 'Wunder@fnatic.com'),
(17, 4, 'Razork', '1998-11-05', 'Razork@fnatic.com'),
(18, 4, 'Humanoid', '1998-11-05', 'Humanoid@fnatic.com'),
(19, 4, 'Upset', '1998-11-05', 'Upset@fnatic.com'),
(20, 4, 'Hylissang', '1998-11-05', 'Hylissang@fnatic.com'),
(21, 5, 'torzsi', '1998-11-05', 'torzsi@Mousesports.com'),
(22, 5, 'frozen', '1998-11-05', 'frozen@Mousesports.com'),
(23, 5, 'Dexter', '1998-11-05', 'Dexter@Mousesports.com'),
(24, 5, 'JDC', '1998-11-05', 'JDC@Mousesports.com'),
(25, 5, 'Bymas', '1998-11-05', 'Bymas@Mousesports.com'),
(26, 6, 'OKOLICIOUZ', '1998-11-05', 'OKOLICIOUZ@virtus.pro'),
(27, 6, 'Vegi', '1998-11-05', 'Vegi@virtus.pro'),
(28, 6, 'MICHU', '1998-11-05', 'MICHU@virtus.pro'),
(29, 6, 'Snatchie', '1998-11-05', 'Snatchie@virtus.pro'),
(30, 6, 'Snax', '1998-11-05', 'Snax@virtus.pro'),
(31, 7, 'Impact', '1998-11-05', 'Impact@evil.com'),
(32, 7, 'Inspired', '1998-11-05', 'Inspired@evil.com'),
(33, 7, 'jojopyun', '1998-11-05', 'jojopyun@evil.com'),
(34, 7, 'Deftly', '1998-11-05', 'Deftly@evil.com'),
(35, 7, 'Vulcan', '1998-11-05', 'Vulcan@evil.com'),
(36, 8, 'Fudge', '1998-11-05', 'Fudge@Cloud9.com'),
(37, 8, 'Blaber', '1998-11-05', 'Blaber@Cloud9.com'),
(38, 8, 'Perkz', '1998-11-05', 'Perkz@Cloud9.com'),
(39, 8, 'Zven', '1998-11-05', 'Zven@Cloud9.com'),
(40, 8, 'Vulcan', '1998-11-05', 'Vulcan@Cloud9.com');

-- --------------------------------------------------------

--
-- Structure de la table `MatchGame`
--

CREATE TABLE `MatchGame` (
  `numMatch` int(10) NOT NULL,
  `numCompetition` int(10) NOT NULL,
  `numEquipe1` int(10) NOT NULL,
  `numEquipe2` int(10) NOT NULL,
  `ScoreEquipe1` int(8) NOT NULL,
  `ScoreEquipe2` int(8) NOT NULL,
  `Duree` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `MatchGame`
--

INSERT INTO `MatchGame` (`numMatch`, `numCompetition`, `numEquipe1`, `numEquipe2`, `ScoreEquipe1`, `ScoreEquipe2`, `Duree`) VALUES
(1, 1, 2, 1, 1, 2, '01:40:00'),
(2, 2, 3, 1, 2, 1, '10:10:10'),
(3, 3, 4, 1, 1, 2, '01:40:00'),
(4, 4, 1, 1, 2, 1, '10:10:10'),
(5, 5, 6, 1, 1, 2, '01:40:00'),
(6, 6, 7, 1, 2, 1, '10:10:10'),
(7, 7, 8, 1, 1, 2, '01:40:00'),
(8, 8, 5, 1, 2, 1, '10:10:10'),
(9, 1, 3, 1, 1, 2, '01:40:00'),
(10, 3, 5, 1, 2, 1, '10:10:10'),
(11, 5, 7, 1, 1, 2, '01:40:00'),
(12, 7, 1, 1, 2, 1, '10:10:10'),
(13, 2, 4, 1, 1, 2, '01:40:00'),
(14, 4, 6, 1, 2, 1, '10:10:10'),
(15, 6, 8, 1, 1, 2, '01:40:00'),
(16, 8, 2, 1, 2, 1, '10:10:10');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Classement`
--
ALTER TABLE `Classement`
  ADD PRIMARY KEY (`numClassement`),
  ADD KEY `numEquipe` (`numEquipe`),
  ADD KEY `numCompetition` (`numCompetition`);

--
-- Index pour la table `Competition`
--
ALTER TABLE `Competition`
  ADD PRIMARY KEY (`numCompetition`);

--
-- Index pour la table `Equipe`
--
ALTER TABLE `Equipe`
  ADD PRIMARY KEY (`numEquipe`);

--
-- Index pour la table `Joueur`
--
ALTER TABLE `Joueur`
  ADD PRIMARY KEY (`numJoueur`);

--
-- Index pour la table `MatchGame`
--
ALTER TABLE `MatchGame`
  ADD PRIMARY KEY (`numMatch`),
  ADD KEY `numCompetition` (`numCompetition`),
  ADD KEY `numEquipe1` (`numEquipe1`),
  ADD KEY `numEquipe2` (`numEquipe2`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `Classement`
--
ALTER TABLE `Classement`
  MODIFY `numClassement` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT pour la table `Competition`
--
ALTER TABLE `Competition`
  MODIFY `numCompetition` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `Equipe`
--
ALTER TABLE `Equipe`
  MODIFY `numEquipe` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pour la table `Joueur`
--
ALTER TABLE `Joueur`
  MODIFY `numJoueur` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT pour la table `MatchGame`
--
ALTER TABLE `MatchGame`
  MODIFY `numMatch` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
