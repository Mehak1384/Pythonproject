Create Database person_management_system;
create table person(
    person_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    dob VARCHAR(20),
    address TEXT,
    phone_number BIGINT,
    qualification VARCHAR(100)
);