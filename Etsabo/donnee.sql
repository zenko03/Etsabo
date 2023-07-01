-- Table Specialite
    INSERT INTO specialite (nom) VALUES ('Spécialité1'), ('Spécialité2'), ('Spécialité3'), ('Spécialité4');

-- Table TypeAbonnement
INSERT INTO type_abonnement (nom_abonnement, prix) VALUES ('Abonnement1', 9.99), ('Abonnement2', 19.99), ('Abonnement3', 29.99), ('Abonnement4', 39.99);

-- Table Famille
INSERT INTO famille (nom_famille, adresse, email, password) VALUES 
    ('Famille1', 'Adresse1', 'famille1@example.com', 'pass1'),
    ('Famille2', 'Adresse2', 'famille2@example.com', 'pass2'),
    ('Famille3', 'Adresse3', 'famille3@example.com', 'pass3'),
    ('Famille4', 'Adresse4', 'famille4@example.com', 'pass4');

-- Table Medicament
INSERT INTO medicament (nom) VALUES ('Medicament1'), ('Medicament2'), ('Medicament3'), ('Medicament4');

-- Table Patient
INSERT INTO patient (nom, prenoms, adresse, telephone, date_de_naissance, email, password, famille_id, is_actif) VALUES 
    ('Patient1', 'Prenoms1', 'Adresse1', '123456789', '2000-01-01', 'patient1@example.com', 'patient1pass', 1, 1),
    ('Patient2', 'Prenoms2', 'Adresse2', '987654321', '2000-02-02', 'patient2@example.com', 'patient2pass', 1, 0),
    ('Patient3', 'Prenoms3', 'Adresse3', '555555555', '2000-03-03', 'patient3@example.com', 'patient3pass', 2, 1),
    ('Patient4', 'Prenoms4', 'Adresse4', '999999999', '2000-04-04', 'patient4@example.com', 'patient4pass', 3, 0);

-- Table Medecin
INSERT INTO medecin (nom, prenoms, email, password, specialite_id) VALUES 
    ('Medecin1', 'Prenoms1', 'medecin1@example.com', 'medecin1pass', 1),
    ('Medecin2', 'Prenoms2', 'medecin2@example.com', 'medecin2pass', 2),
    ('Medecin3', 'Prenoms3', 'medecin3@example.com', 'medecin3pass', 3),
    ('Medecin4', 'Prenoms4', 'medecin4@example.com', 'medecin4pass', 4);

-- Table Message
INSERT INTO message (medecin_id, patient_id, type, contenus, date_envoie) VALUES 
    (1, 1, 1, 'Contenu1', '2023-06-18'),
    (2, 2, 0, 'Contenu2', '2023-06-18'),
    (3, 3, 1, 'Contenu3', '2023-06-18'),
    (4, 4, 0, 'Contenu4', '2023-06-18');

-- Table Abonnement
INSERT INTO abonnement (patient_id, date_fin, type_id) VALUES 
    (1, '2023-12-31', 1),
    (2, '2023-12-31', 2),
    (3, '2023-12-31', 3),
    (4, '2023-12-31', 4);

-- Table Consultation
INSERT INTO consultation (medecin_id, patient_id, date_consultation, symptomes, diagnostic) VALUES 
    (1, 1, '2023-06-18', 'Symptômes1', 'Diagnostic1'),
    (2, 2, '2023-06-18', 'Symptômes2', 'Diagnostic2'),
    (3, 3, '2023-06-18', 'Symptômes3', 'Diagnostic3'),
    (4, 4, '2023-06-18', 'Symptômes4', 'Diagnostic4');

-- Table Ordonnance
INSERT INTO ordonnance (consultation_id, medocs_id, prise) VALUES 
    (1, 1, 'Prise1'),
    (2, 2, 'Prise2'),
    (3, 3, 'Prise3'),
    (4, 4, 'Prise4');

-- Table Rdv
INSERT INTO rdv (medecin_id, patient_id, dateHeure_rdv, status) VALUES
    (1, 1, '2023-07-18 10:00:00', 0),
    (2, 2, '2023-07-18 11:00:00', 0),
    (3, 3, '2023-07-18 12:00:00', 0),
    (4, 4, '2023-07-18 13:00:00', 0);

INSERT INTO rdv (dateHeure_rdv, status,medecin_id, patient_id) VALUES
    ('2023-07-18 10:00:00', 0,1, 1),
    ('2023-07-18 11:00:00', 0,2, 2),
    ('2023-07-18 12:00:00', 0,3, 3),
    ('2023-07-18 13:00:00', 0,4, 4);


-- Table Pharmacie
INSERT INTO pharmacie (nom_pharmacie, long, lat) VALUES 
    ('Pharmacie1', 1.0, 1.0),
    ('Pharmacie2', 2.0, 2.0),
    ('Pharmacie3', 3.0, 3.0),
    ('Pharmacie4', 4.0, 4.0);

-- Table Publicite
INSERT INTO publicite (titre, description, photo, date_debut, date_fin) VALUES 
    ('Publicite1', 'Description1', 'photo1.jpg', '2023-06-18', '2023-12-31'),
    ('Publicite2', 'Description2', 'photo2.jpg', '2023-06-18', '2023-12-31'),
    ('Publicite3', 'Description3', 'photo3.jpg', '2023-06-18', '2023-12-31'),
    ('Publicite4', 'Description4', 'photo4.jpg', '2023-06-18', '2023-12-31');

INSERT INTO conseils_sanitaire (titre, description, img)
VALUES
    ('Maintenez une bonne hygiène des mains', 'Lavez-vous régulièrement les mains à l eau et au savon pendant au moins 20 secondes. Utilisez également du désinfectant pour les mains à base d alcool lorsque le lavage des mains n est pas possible.', 'laverMain.jpg');

INSERT INTO objet(nom_objet,prix) VALUES
    ('Thermometre electronique',12000),
    ('Tensiometre electronique',35000);

INSERT INTO photo_objet(objet_id, src) VALUES
    (1, 'obj1.jpg'),
    (2, 'obj2.jpg');
