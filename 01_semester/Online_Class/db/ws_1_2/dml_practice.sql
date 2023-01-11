CREATE TABLE animals(
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INTEGER NOT NULL,
  height INTEGER,
  age INTEGER 
);

ALTER TABLE animals RENAME TO zoo;

INSERT INTO zoo VALUES ('gorilla', 'omnivore', 215, 180, 5), ('rabbit', 'herbivore',3, 150, '' ), ('tiger', 'carnivore', 220, 115, 3);

SELECT * FROM zoo;

UPDATE zoo SET height=15 WHERE name='rabbit';

DELETE FROM zoo WHERE eat='omnivore';

SELECT * FROM zoo;