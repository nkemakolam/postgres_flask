CREATE TABLE users
(
    id SERIAL PRIMARY KEY,
    email character varying(255),
    first_name character varying(255),
    last_name character varying(255)

)

SELECT * FROM  users
delete * from  users where  id!=1