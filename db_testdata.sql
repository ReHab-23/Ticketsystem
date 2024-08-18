USE ticketsystem;

INSERT INTO benutzer (vorname, nachname, passwort, kurs, raum, mail, klasse)
VALUES (
    'Max',         
    'Mustermann',  
    'password123', 
    'Informatik',  
    'Raum 101',    
    'max.mustermann@example.com', 
    '1'          
);

INSERT INTO benutzer (vorname, nachname, passwort, kurs, raum, mail, klasse)
VALUES (
    'Anna',         
    'Schmidt',     
    'xkcdpzrlei',  
    'Physik',       
    'Raum 523',     
    'anna.schmidt@example.com', 
    '2'           
);

INSERT INTO benutzer (vorname, nachname, passwort, kurs, raum, mail, klasse)
VALUES (
    'Bernd',         
    'Stromberg',     
    'capitol333',  
    'BWL',       
    'Raum 666',     
    'berndstromberg@capitol.de', 
    '3'           
);



INSERT INTO ticket (bezeichnung, ersteller, problembeschreibung, zeitstempel, bearbeiter, status, supportnotiz, prioritaetskategorie)
VALUES (
    'Netzwerk-Probleme',                 
    'Peter Müller',                   
    'Unregelmäßige Verbindungsfehler',                
    '2024-07-21 12:34:56',           
    'Anna Schmidt',                   
    'In Bearbeitung',                 
    'Fehlersuche',       
    'Hoch'                           
);

INSERT INTO ticket (bezeichnung, ersteller, problembeschreibung, zeitstempel, bearbeiter, status, supportnotiz, prioritaetskategorie)
VALUES (
    'Monitor defekt',                 
    'Peter Müller',                   
    'Monitor funktioniert nicht ordnungsgemäß',                
    '2024-07-21 12:34:56',           
    'Bernd Stromberg',                   
    'In Bearbeitung',                 
    'Monitor auswechseln',       
    'Niedrig'                           
);

INSERT INTO ticket (bezeichnung, ersteller, problembeschreibung, zeitstempel, bearbeiter, status, supportnotiz, prioritaetskategorie)
VALUES (
    'Verbindungsfehler',                 
    'Peter Müller',                   
    'Verbindung bricht nach kurzer Zeit ab',                
    '2024-07-21 12:34:56',           
    'Max Mustermann',                   
    'In Bearbeitung',                 
    'Fehlersuche',       
    'Mittel'                           
);