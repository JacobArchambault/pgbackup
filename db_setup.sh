#!/bin/sh

echo "Configure database user"
read -p "Postgres user name: " name
read -s -p "Postgres user password: " password

export POSTGRES_USER=$name
export POSTGRES_PASSWORD=$password

podman rm --force postgres || true

podman volume rm --force pg-data || true
echo "Creating database container (and seed 'sample' database)"
podman volume create pg-data
podman run -d \
  --name postgres \
  -e POSTGRES_USER=$POSTGRES_USER \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  -e POSTGRES_DB=sample \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v "pg-data:/var/lib/postgresql/data" \
  -p "5432:5432" \
  --restart always \
  postgres:16.1-alpine

sleep 20 # Ensure enough time for postgres database to initialize and create role

podman exec -i postgres psql -U $POSTGRES_USER -d sample <<-EOF
create table employees (
  id INT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email VARCHAR(50),
  gender VARCHAR(50),
  favorite_color VARCHAR(50)
);
delete from employees;
insert into employees (id, first_name, last_name, email, gender, favorite_color) values (1, 'Lauralee', 'Morkham', 'lmorkham0@example.com', 'Female', '#878922');
insert into employees (id, first_name, last_name, email, gender, favorite_color) values (2, 'Hillery', 'Langland', 'hlangland1@example.com', 'Male', '#6fd569');
insert into employees (id, first_name, last_name, email, gender, favorite_color) values (3, 'Regan', 'Kroger', 'rkroger2@example.com', 'Male', '#d9c547');
EOF
