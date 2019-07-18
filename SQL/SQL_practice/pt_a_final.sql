#######################################################################################################################################################
# a)  Give the class names and countries of the classes that carried guns of at least 16 inch bore
#######################################################################################################################################################

SELECT DISTINCT class, country
    FROM   classes
    WHERE  bore >= 16;

#######################################################################################################################################################
# b)  Find the ships launched prior to 1921
#######################################################################################################################################################

SELECT DISTINCT name
FROM   ships
WHERE  launched<1921;

#######################################################################################################################################################
#c) Find the ships sunk in the battle of the Denmark Strait
#######################################################################################################################################################

SELECT DISTINCT ship
FROM   outcomes
WHERE  battle = 'Denmark Strait'
       AND result = 'sunk';

#######################################################################################################################################################
#d)The Treaty of Washington in 1921 prohibited capital ships heavier than 35,000 tons. List the
# ships that violated the Treaty of Washington"
#######################################################################################################################################################
/*
DROP VIEW IF EXISTS heavy_class;
create view heavy_class AS
SELECT *
FROM   classes
WHERE  displacement > 35000;

DROP VIEW IF EXISTS new_ships;
CREATE VIEW new_ships AS
SELECT *
FROM   ships
WHERE  launched >= 1921;

SELECT DISTINCT name
FROM   heavy_class
       INNER JOIN 
       new_ships
ON     heavy_class.class = new_ships.class;
*/
DROP VIEW IF EXISTS heavy_class;
create view heavy_class AS
SELECT *
FROM   classes
WHERE  displacement > 35000;

SELECT DISTINCT name
FROM   heavy_class
       INNER JOIN 
       ships
ON     heavy_class.class = ships.class;


#######################################################################################################################################################
# e)List the name, displacement and number of guns of the ships engaged in the battle of Guadalcanal
#######################################################################################################################################################

DROP VIEW IF EXISTS guada_fighters;
CREATE VIEW guada_fighters AS
SELECT ship, battle, result
FROM   outcomes
WHERE  battle = 'Guadalcanal';

DROP VIEW IF EXISTS guada_ships;
CREATE VIEW guada_ships AS
SELECT name, class
FROM   guada_fighters
       INNER JOIN
       ships
ON     ships.name = guada_fighters.ship;

SELECT name, displacement, numGuns
FROM   classes
       INNER JOIN
       guada_ships
ON     classes.class = guada_ships.class;

#######################################################################################################################################################
# f) List all the capital ships mentioned in the database. (Remember that all these ships may not
# appear in the Ship relation."
#######################################################################################################################################################

SELECT DISTINCT ship_name
FROM ((SELECT ship AS ship_name
       FROM   outcomes)
	   UNION
       (SELECT name AS ship_name
        FROM   ships)) as all_ships;

#######################################################################################################################################################
# g) Find the classes that had only one ship as a member of that class
#######################################################################################################################################################

DROP VIEW IF EXISTS mt_one;
CREATE VIEW mt_one AS
SELECT DISTINCT ships1.class
FROM   ships AS ships1,
       ships AS ships2
WHERE  ships1.name != ships2.name
       AND ships1.class = ships2.class;

SELECT DISTINCT ships.class
FROM   ships
       LEFT JOIN
       mt_one
ON     ships.class = mt_one.class
WHERE  mt_one.class IS NULL;

#######################################################################################################################################################
# h) Find those countries that had both battleships and battle cruisers
#######################################################################################################################################################

SELECT DISTINCT relevant.country
FROM   classes AS relevant,
       classes AS ship_checker
WHERE  relevant.country = ship_checker.country
       AND relevant.type = 'bb'
       AND ship_checker.type = 'bc';

#######################################################################################################################################################
# i) Find those ships that "lived to fight another day"; they were damaged in one battle but laer fought in another
#######################################################################################################################################################

DROP VIEW IF EXISTS survival;
CREATE VIEW survival AS
SELECT *
FROM   outcomes
       INNER JOIN
       battles
ON     outcomes.battle = battles.name;

SELECT survival.ship
FROM   survival, survival AS stronger
WHERE survival.ship = stronger.ship
	  AND survival.result = 'damaged'
      AND survival.date < stronger.date;
