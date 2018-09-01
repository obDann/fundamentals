#######################################################################################################################################################
# a)  Give the class names and countries of the classes that carried guns of at least 16 inch bore
#######################################################################################################################################################
/*
SELECT class, country
FROM   classes
WHERE  bore >= 16;
*/
#######################################################################################################################################################
# b)  Find the ships launched prior to 1921
#######################################################################################################################################################
/*
SELECT name
FROM   ships
WHERE  launched<1921;
*/
#######################################################################################################################################################
#c) Find the ships sunk in the battle of the Denmark Strait
#######################################################################################################################################################
/*
SELECT ship
FROM   outcomes
WHERE  battle = 'Denmark Strait'
       AND result = 'sunk'
*/
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
WHERE  launched >= 1925;

SELECT DISTINCT name
FROM   heavy_class
       INNER JOIN 
       new_ships
ON     heavy_class.class = new_ships.class
*/


/*
    SELECT DISTINCT name
    FROM   (SELECT *
		           FROM ships
		           WHERE launched >= 1921) AS new_ships
           NATURAL JOIN (SELECT *
                         FROM classes
                         WHERE displacement > 35000) AS heavy_class
*/




#######################################################################################################################################################
# e)List the name, displacement and number of guns of the ships engaged in the battle of Guadalcanal
#######################################################################################################################################################

/*
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
ON ships.name=guada_fighters.ship;

SELECT name, displacement, numGuns
FROM classes
     INNER JOIN
	 guada_ships
ON   classes.class = guada_ships.class
*/


/*
SELECT name, displacement, numGuns
FROM   classes
       NATURAL JOIN
       (SELECT name, class
       FROM   (SELECT ship AS name, battle, result
               FROM   outcomes
			   WHERE  battle = 'Guadalcanal') AS guada_fighters
               NATURAL JOIN
               Ships) AS guada_ships
*/
#######################################################################################################################################################
# f) List all the capital ships mentioned in the database. (Remember that all these ships may not
# appear in the Ship relation."
#######################################################################################################################################################
/*
DROP VIEW IF EXISTS from_outcomes;
CREATE VIEW from_outcomes AS
SELECT DISTINCT ship as ship_name
FROM   outcomes;

DROP VIEW IF EXISTS from_ships;
CREATE VIEW from_ships AS
SELECT DISTINCT name as ship_name
FROM   ships;

SELECT DISTINCT *
FROM from_ships.ship_name UNION from_outcomes.ship_name  # getting errors
*/


/*
SELECT DISTINCT ship_name
FROM ((SELECT ship AS ship_name
       FROM     outcomes)
	   UNION
       (SELECT name AS ship_name
       FROM    ships)) as all_ships
*/

#######################################################################################################################################################
# g) Find the classes that had only one ship as a member of that class
#######################################################################################################################################################
/*
SELECT mtz.class
FROM   Ships as mtz, Ships as mto
WHERE  NOT mtz.class = mto.class 
	   AND NOT mtz.name != mto.name
*/

#INSERT INTO ships values ('fake ship', 'fakeship', 1999);
/*
DROP VIEW IF EXISTS mt_one;
CREATE VIEW mt_one AS
SELECT DISTINCT Ships1.class
FROM   ships AS ships1,
       ships AS ships2
WHERE Ships1.name != Ships2.name
      AND Ships1.class = Ships2.class;


SELECT DISTINCT ships.class
FROM   ships
       LEFT JOIN
       mt_one
       ON ships.class = mt_one.class
WHERE  mt_one.class IS NULL
*/

/*
    SELECT class
    FROM   Ships
    WHERE  class NOT IN (SELECT Ships1.class
                         FROM   Ships AS Ships1,
                                Ships AS Ships2
                         WHERE  Ships1.name <> Ships2.name
                                AND Ships1.class = Ships2.class)
*/

#######################################################################################################################################################
# h) Find those countries that had both battleships and battle cruisers
#######################################################################################################################################################

# MAY REWORD BECAUSE THERE CAN BE MORE THAN TWO TYPES OF SHIPS
/*
SELECT DISTINCT relevant.country
FROM   classes AS relevant,
       classes AS ship_checker
WHERE  relevant.country = ship_checker.country
       AND relevant.type != ship_checker.type
*/

/*
SELECT DISTINCT relevant.country
FROM   classes AS relevant,
       classes AS ship_checker
WHERE  relevant.country = ship_checker.country
       AND relevant.type = 'bb'
       AND ship_checker.type = 'bc'
*/
#######################################################################################################################################################
# i) Find those ships that "lived to fight another day"; they were damaged in one battle but laer fought in another
#######################################################################################################################################################
/*
DROP VIEW IF EXISTS survival;
CREATE VIEW survival AS
SELECT *
FROM   outcomes
       INNER JOIN
       battles
ON     outcomes.battle = battles.name;

#INSERT INTO outcomes values ('South Dakota', 'Surigao Strait', 'sunk');

SELECT survival.ship
FROM   survival, survival AS stronger
WHERE survival.ship = stronger.ship
	  AND survival.result = 'damaged'
      AND survival.date < stronger.date;

DELETE FROM outcomes
WHERE ship = 'South Dakota'
	  AND battle = 'Surigao Strait'
*/

/*
SELECT *
FROM   (SELECT *
	   FROM outcomes
	   NATURAL JOIN
                    (SELECT name AS battle, date
                    FROM battles) AS battle_updated
       ) AS survival,

       (SELECT *
	   FROM outcomes
	   NATURAL JOIN
                    (SELECT name AS battle, date
                    FROM battles) AS battle_updated
       ) AS stronger
WHERE survival.ship = stronger.ship
      AND survival.result = 'damaged'
      AND survival.date < stronger.date
*/