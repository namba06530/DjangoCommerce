-- object: public.role | type: TABLE --
DROP TABLE IF EXISTS public.role CASCADE;
CREATE TABLE public.role (
	role_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom varchar(20),
	CONSTRAINT role_pk PRIMARY KEY (role_id)

);
-- ddl-end --
COMMENT ON COLUMN public.role.nom IS E'Admin, Salarié, Client, Invité';
-- ddl-end --
ALTER TABLE public.role OWNER TO dev;
-- ddl-end --

-- object: public.utilisateur | type: TABLE --
DROP TABLE IF EXISTS public.utilisateur CASCADE;
CREATE TABLE public.utilisateur (
	utilisateur_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	prenom varchar(50),
	nom varchar(50),
	mail varchar(50) NOT NULL,
	password varchar(20) NOT NULL,
	role_id smallint NOT NULL,
	CONSTRAINT utilisateur_pk PRIMARY KEY (utilisateur_id)

);
-- ddl-end --
ALTER TABLE public.utilisateur OWNER TO dev;
-- ddl-end --

-- object: public.produit | type: TABLE --
DROP TABLE IF EXISTS public.produit CASCADE;
CREATE TABLE public.produit (
	produit_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom varchar(50) NOT NULL,
	description varchar(500),
	categorie varchar(50),
	prix decimal(7,2) NOT NULL,
	fournisseur varchar(50),
	CONSTRAINT produit_pk PRIMARY KEY (produit_id)

);
-- ddl-end --
ALTER TABLE public.produit OWNER TO dev;
-- ddl-end --

-- object: public.panier | type: TABLE --
DROP TABLE IF EXISTS public.panier CASCADE;
CREATE TABLE public.panier (
	panier_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom varchar(50),
	produit_id smallint NOT NULL,
	CONSTRAINT panier_pk PRIMARY KEY (panier_id)

);
-- ddl-end --
ALTER TABLE public.panier OWNER TO dev;
-- ddl-end --

-- object: public.commande | type: TABLE --
DROP TABLE IF EXISTS public.commande CASCADE;
CREATE TABLE public.commande (
	commande_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	panier_id smallint NOT NULL,
	utilisateur_id smallint NOT NULL,
	CONSTRAINT commande_pk PRIMARY KEY (commande_id)

);
-- ddl-end --
COMMENT ON COLUMN public.commande.commande_id IS E'numéro de la commande ?';
-- ddl-end --
ALTER TABLE public.commande OWNER TO dev;
-- ddl-end --

-- object: panier_fk | type: CONSTRAINT --
-- ALTER TABLE public.commande DROP CONSTRAINT IF EXISTS panier_fk CASCADE;
ALTER TABLE public.commande ADD CONSTRAINT panier_fk FOREIGN KEY (panier_id)
REFERENCES public.panier (panier_id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: commande_uq | type: CONSTRAINT --
-- ALTER TABLE public.commande DROP CONSTRAINT IF EXISTS commande_uq CASCADE;
ALTER TABLE public.commande ADD CONSTRAINT commande_uq UNIQUE (panier_id);
-- ddl-end --

-- object: produit_fk | type: CONSTRAINT --
-- ALTER TABLE public.panier DROP CONSTRAINT IF EXISTS produit_fk CASCADE;
ALTER TABLE public.panier ADD CONSTRAINT produit_fk FOREIGN KEY (produit_id)
REFERENCES public.produit (produit_id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: role_fk | type: CONSTRAINT --
-- ALTER TABLE public.utilisateur DROP CONSTRAINT IF EXISTS role_fk CASCADE;
ALTER TABLE public.utilisateur ADD CONSTRAINT role_fk FOREIGN KEY (role_id)
REFERENCES public.role (role_id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: utilisateur_fk | type: CONSTRAINT --
-- ALTER TABLE public.commande DROP CONSTRAINT IF EXISTS utilisateur_fk CASCADE;
ALTER TABLE public.commande ADD CONSTRAINT utilisateur_fk FOREIGN KEY (utilisateur_id)
REFERENCES public.utilisateur (utilisateur_id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --


