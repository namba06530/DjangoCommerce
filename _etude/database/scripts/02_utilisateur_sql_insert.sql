
insert into utilisateur (prenom, nom, mail, password, role_id) values ('Olivier', 'Grellety', 'grellety.olivier@gmail.com', '12345', (select role_id from role where role_id='1'));
--insert into utilisateur (prenom, nom, mail, password, role_id) values ('Elon', 'Musk', 'elon.musk@email.com', '12345', (select role_id from role where role_id='3'));