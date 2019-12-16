CREATE TYPE campaignstaffsizes AS ENUM (
    'A',
    'B',
    'C',
    'D',
    'E'
);

CREATE TABLE company (
    registrationnumber character varying(50) NOT NULL,
    city character varying(100) NOT NULL,
    country character varying(50) NOT NULL,
    sizeofstaff campaignstaffsizes NOT NULL,
    id character varying(36) NOT NULL
);

CREATE TABLE companymigratesdatabase (
    companyid character varying(36) NOT NULL,
    migrationid character varying(36) NOT NULL
);

CREATE TABLE databaseentity (
    database character varying(50) NOT NULL,
    entityname character varying(50) NOT NULL,
    id character varying(36) NOT NULL
);

CREATE TABLE databasemigration (
    databasefrom character varying(50) NOT NULL,
    databaseto character varying(50) NOT NULL,
    date timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    hardwarenumber character varying(36),
    sucess boolean,
    id character varying(36) NOT NULL
);

CREATE TABLE operation (
    database character varying(50) NOT NULL,
    name character varying(50) NOT NULL,
    id character varying(36) NOT NULL
);

CREATE TABLE operationcontainsoperation (
    operation1id character varying(36) NOT NULL,
    operation2id character varying(36) NOT NULL
);

CREATE TABLE operationusedatabaseentity (
    operationid character varying(36) NOT NULL,
    databaseentityid character varying(36) NOT NULL
);


CREATE TABLE syntax (
    database character varying(50) NOT NULL,
    regex text NOT NULL,
    operationid character varying(36) NOT NULL
);

ALTER TABLE ONLY company
    ADD CONSTRAINT company_pkey PRIMARY KEY (id);

ALTER TABLE ONLY companymigratesdatabase
    ADD CONSTRAINT companymigratesdatabase_pkey PRIMARY KEY (companyid, migrationid);

ALTER TABLE ONLY databaseentity
    ADD CONSTRAINT databaseentity_pkey PRIMARY KEY (id);

ALTER TABLE ONLY databaseentity
    ADD CONSTRAINT databaseentity_unique UNIQUE (database, entityname);

ALTER TABLE ONLY databasemigration
    ADD CONSTRAINT databasemigration_pkey PRIMARY KEY (id);

ALTER TABLE ONLY operation
    ADD CONSTRAINT operation_pkey PRIMARY KEY (id);

ALTER TABLE ONLY operation
    ADD CONSTRAINT operation_unique UNIQUE (database, name);

ALTER TABLE ONLY operationcontainsoperation
    ADD CONSTRAINT operationcontainsoperation_pkey PRIMARY KEY (operation1id, operation2id);

ALTER TABLE ONLY operationusedatabaseentity
    ADD CONSTRAINT operationusedatabaseentity_pkey PRIMARY KEY (operationid, databaseentityid);

ALTER TABLE ONLY syntax
    ADD CONSTRAINT syntax_pkey PRIMARY KEY (database, regex);

ALTER TABLE ONLY companymigratesdatabase
    ADD CONSTRAINT cmdc_fk FOREIGN KEY (companyid) REFERENCES company(id);

ALTER TABLE ONLY companymigratesdatabase
    ADD CONSTRAINT cmdm_fk FOREIGN KEY (migrationid) REFERENCES databasemigration(id);

ALTER TABLE ONLY operationcontainsoperation
    ADD CONSTRAINT operationcontainedinoperationfk FOREIGN KEY (operation2id) REFERENCES operation(id);

ALTER TABLE ONLY operationcontainsoperation
    ADD CONSTRAINT operationcontainsoperationfk FOREIGN KEY (operation1id) REFERENCES operation(id);

ALTER TABLE ONLY operationusedatabaseentity
    ADD CONSTRAINT oudede_fk FOREIGN KEY (databaseentityid) REFERENCES databaseentity(id);

ALTER TABLE ONLY operationusedatabaseentity
    ADD CONSTRAINT oudeo_fk FOREIGN KEY (operationid) REFERENCES operation(id);

ALTER TABLE ONLY syntax
    ADD CONSTRAINT syntaxoperationfk FOREIGN KEY (operationid) REFERENCES operation(id);
