CREATE table songs(
	id int primary key auto_increment,
    title varchar(255) not null,
    artist varchar(255) not null,
    album varchar(255),
    release_year int not null
);

INSERT INTO songs (title, artist, album, release_year) 
VALUES
('Bohemian Rhapsody', 'Queen', 'A Night at the Opera', 1975),
('Imagine', 'John Lennon', 'Imagine', 1971),
('Like a Rolling Stone', 'Bob Dylan', 'Highway 61 Revisited', 1965),
('Respect', 'Aretha Franklin', 'I Never Loved a Man the Way I Love You', 1967),
("What's Going On", 'Marvin Gaye', "What's Going On", 1971),
('Hey Jude', 'The Beatles', 'Abbey Road', 1969),
('Stairway to Heaven', 'Led Zeppelin', 'Led Zeppelin IV', 1971),
('Yesterday', 'The Beatles', 'Help!', 1965),
('I Will Survive', 'Gloria Gaynor', 'I Will Survive', 1978),
('Born to Run', 'Bruce Springsteen', 'Born to Run', 1975),
('American Pie', 'Don McLean', 'American Pie', 1971),
('Dancing Queen', 'ABBA', 'Arrival', 1976),
('I Will Always Love You', 'Whitney Houston', 'The Bodyguard: Original Soundtrack Album', 1992),
('Hallelujah', 'Leonard Cohen', 'Various Positions', 1984),
('What a Wonderful World', 'Louis Armstrong', 'What a Wonderful World', 1967),
('Yesterday Once More', 'The Carpenters', 'Close to You', 1970),
('Bridge Over Troubled Water', 'Simon & Garfunkel', 'Bridge Over Troubled Water', 1970),
("Free Fallin'", 'Tom Petty', 'Full Moon Fever', 1989),
('I Want It That Way', 'Backstreet Boys', 'Millennium', 1999),
("Can't Stop the Feeling!", 'Justin Timberlake', 'Trolls', 2016);

select * from songs

--@block
CREATE table users(
    id int primary key auto_increment,
    username varchar(255) not null,
    pass varchar(255) not null
);

--@block
INSERT INTO users(username, _pass)
VALUES('admin', 'admin')

--@block
DROP 