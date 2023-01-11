CREATE TABLE animals(
  animal_name TEXT NOT NULL,
  height INTEGER NOT NULL,
  weight INTEGER NOT NULL,
  age INTEGER 
);

ALTER TABLE animals ADD COLUMN meal TEXT DEFAULT 'no meal';

ALTER TABLE animals RENAME COLUMN animal_name To name;

ALTER TABLE animals RENAME TO zoo;

DROP TABLE zoo;