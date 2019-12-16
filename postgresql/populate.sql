INSERT INTO operation(database, name, id) VALUES ('mysql', 'createtable', '1');
INSERT INTO operation(database, name, id) VALUES ('oracle', 'createtable', '2');
INSERT INTO operation(database, name, id) VALUES ('cassandra', 'createtable', '3');
INSERT INTO operation(database, name, id) VALUES ('cassandra', 'declaretablecolumn', '4');
INSERT INTO operation(database, name, id) VALUES ('mysql', 'declaretablecolumn', '5');
INSERT INTO operation(database, name, id) VALUES ('oracle', 'declaretablecolumn', '6');

INSERT INTO syntax (database , regex , operationId ) VALUES ( 'mysql', 'CREATE TABLE(\s+|)(.*)\);', '1' );
INSERT INTO syntax (database , regex , operationId ) VALUES ( 'oracle', 'CREATE TABLE(\s+|)(.*)\);', '2' );
INSERT INTO syntax (database , regex , operationId ) VALUES ( 'cassandra', 'CREATE TABLE(\s+|)(.*)\);', '3' );

Insert into databaseentity (database, entityName, id) VALUES ('mysql', 'datatable', '1');
Insert into databaseentity (database, entityName, id) VALUES ('oracle', 'datatable', '2');
Insert into databaseentity (database, entityName, id) VALUES ('cassandra', 'datatable', '3');

INSERT INTO OperationContainsOperation(operation1Id, operation2Id) VALUES ('1', '5');
INSERT INTO OperationContainsOperation(operation1Id, operation2Id) VALUES ('2', '6');
INSERT INTO OperationContainsOperation(operation1Id, operation2Id) VALUES ('3', '4');

INSERT INTO OperationUseDatabaseEntity(operationId, DatabaseEntityId) VALUES ('1', '1');
INSERT INTO OperationUseDatabaseEntity(operationId, DatabaseEntityId) VALUES ('2', '2');
INSERT INTO OperationUseDatabaseEntity(operationId, DatabaseEntityId) VALUES ('3', '3');
INSERT INTO OperationUseDatabaseEntity(operationId, DatabaseEntityId) VALUES ('5', '1');
INSERT INTO OperationUseDatabaseEntity(operationId, DatabaseEntityId) VALUES ('6', '2');
INSERT INTO OperationUseDatabaseEntity(operationId, DatabaseEntityId) VALUES ('4', '3');

INSERT INTO Company(RegistrationNumber, city, country, sizeOfStaff, id) VALUES ('1', 'Kyiv', 'Ukraine', 'A', '1');
INSERT INTO Company(RegistrationNumber, city, country, sizeOfStaff, id) VALUES ('1', 'Kyiv', 'Ukraine', 'A', '2');
INSERT INTO Company(RegistrationNumber, city, country, sizeOfStaff, id) VALUES ('1', 'Donetsk', 'Ukraine', 'E', '3');
INSERT INTO Company(RegistrationNumber, city, country, sizeOfStaff, id) VALUES ('1', 'Kyiv', 'Ukraine', 'D', '4');
INSERT INTO Company(RegistrationNumber, city, country, sizeOfStaff, id) VALUES ('1', 'Lviv', 'Ukraine', 'B', '5');
INSERT INTO Company(RegistrationNumber, city, country, sizeOfStaff, id) VALUES ('1', 'Kharkiv', 'Ukraine', 'C', '6');

INSERT INTO DatabaseMigration(databaseFrom, databaseTo, hardwareNumber, sucess, id) VALUES ('mysql', 'cassandra', '1', true, '1');
INSERT INTO DatabaseMigration(databaseFrom, databaseTo, hardwareNumber, sucess, id) VALUES ('mysql', 'cassandra', '2', true, '2');
INSERT INTO DatabaseMigration(databaseFrom, databaseTo, hardwareNumber, sucess, id) VALUES ('mysql', 'cassandra', '3', true, '3');
INSERT INTO DatabaseMigration(databaseFrom, databaseTo, hardwareNumber, sucess, id) VALUES ('mysql', 'cassandra', '1', true, '4');
INSERT INTO DatabaseMigration(databaseFrom, databaseTo, hardwareNumber, sucess, id) VALUES ('mysql', 'cassandra', '1', false, '5');
INSERT INTO DatabaseMigration(databaseFrom, databaseTo, hardwareNumber, sucess, id) VALUES ('mysql', 'cassandra', '2', false, '6');
INSERT INTO DatabaseMigration(databaseFrom, databaseTo, hardwareNumber, sucess, id) VALUES ('mysql', 'cassandra', '2', false, '7');
INSERT INTO DatabaseMigration(databaseFrom, databaseTo, hardwareNumber, sucess, id) VALUES ('mysql', 'cassandra', '3', true, '8');

INSERT INTO CompanyMigratesDatabase(companyId, migrationId) VALUES ('1', '1');
INSERT INTO CompanyMigratesDatabase(companyId, migrationId) VALUES ('2', '2');
INSERT INTO CompanyMigratesDatabase(companyId, migrationId) VALUES ('3', '3');
INSERT INTO CompanyMigratesDatabase(companyId, migrationId) VALUES ('1', '4');
INSERT INTO CompanyMigratesDatabase(companyId, migrationId) VALUES ('4', '5');
INSERT INTO CompanyMigratesDatabase(companyId, migrationId) VALUES ('5', '6');
INSERT INTO CompanyMigratesDatabase(companyId, migrationId) VALUES ('6', '7');
INSERT INTO CompanyMigratesDatabase(companyId, migrationId) VALUES ('1', '8');
