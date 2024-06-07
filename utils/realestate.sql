DROP TABLE IF EXISTS Property CASCADE;

CREATE TABLE IF NOT EXISTS Property(
    ID serial unique not null PRIMARY KEY,
	text varchar,
    beds int,
    baths int,
	type varchar(30),
    garage Bool,
	sqrf int,
    listPrice int,
	stories int,
	year_built int
);

DELETE FROM Property;

SELECT * FROM Property;


CREATE INDEX IF NOT EXISTS Property_index
ON Property (type, stories, garage);