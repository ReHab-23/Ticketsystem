--Testdaten einfügen

USE ticketsystem;

INSERT INTO benutzer (vorname, nachname, passwort, kurs, raum, mail, klasse)
VALUES (
    'Max',         -- vorname
    'Mustermann',  -- nachname
    'password123', -- passwort
    'Informatik',  -- kurs
    'Raum 101',    -- raum
    'max.mustermann@example.com', -- mail
    '10A'          -- klasse
);

INSERT INTO benutzer (vorname, nachname, passwort, kurs, raum, mail, klasse)
VALUES (
    'Anna',         -- vorname
    'Schmidt',      -- nachname
    'xkcdpzrlei',   -- passwort
    'Physik',       -- kurs
    'Raum 523',     -- raum
    'anna.schmidt@example.com', -- mail
    '11A'           -- klasse
);

INSERT INTO ticket (bezeichnung, ersteller, problembeschreibung, zeitstempel, bearbeiter, status, supportnotiz, prioritaetskategorie)
VALUES (
    'Network Issue',                  -- bezeichnung
    'Peter Müller',                   -- ersteller
    'Network is down',                -- problembeschreibung
    '2024-07-21 12:34:56',            -- zeitstempel
    'Anna Schmidt',                   -- bearbeiter
    'In Bearbeitung',                 -- status
    'Investigating the issue',        -- supportnotiz
    'Hoch'                            -- prioritaetskategorie
);