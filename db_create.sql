--Datenbank erstellen, falls nicht vorhanden & definierte Tabellen erstellen

CREATE DATABASE IF NOT EXISTS ticketsystem;

USE ticketsystem;

CREATE TABLE benutzer (
	id INTEGER AUTO_INCREMENT PRIMARY KEY, --!WICHTIG: ID bei Login als Username angeben
	vorname VARCHAR(30),
	nachname VARCHAR(30),
	passwort VARCHAR(30),
	kurs VARCHAR(30),
	raum VARCHAR(30),
	mail VARCHAR(30),
	klasse INTEGER
);

CREATE TABLE ticket (
	ticketid INTEGER AUTO_INCREMENT PRIMARY KEY,
	bezeichnung VARCHAR(30),
	ersteller VARCHAR(30),
	problembeschreibung VARCHAR(30),
	zeitstempel TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	bearbeiter VARCHAR(30),
	status VARCHAR(30),
	supportnotiz VARCHAR(30),
	prioritaetskategorie INTEGER
);