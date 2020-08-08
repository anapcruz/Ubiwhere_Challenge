#!/usr/bin/env bash

#register some users
curl --header "Content-Type: application/json" --request POST --data '{"username":"user1", "email":"user1@gmail.com" , "password":"user1_password"}' http://localhost:8000/api/register/

curl --header "Content-Type: application/json" --request POST --data '{"username":"user2", "email":"user2@gmail.com" , "password":"user2_password"}' http://localhost:8000/api/register/

curl --header "Content-Type: application/json" --request POST --data '{"username":"user3", "email":"user3@gmail.com" , "password":"user3_password"}' http://localhost:8000/api/register/


#register some occurrences
curl --header "Content-Type: application/json" --request POST --data '{"author":"user1", "address":"São Bernardo" , "description":"Estrada condicionada.", "category":"ROAD_COND"}'  http://localhost:8000/api/occurrence/

curl --header "Content-Type: application/json" --request POST --data '{"author":"user2", "address":"Praia da Barra" , "description":"Existe muito nevoeiro.", "category":"WTHR_COND"}'  http://localhost:8000/api/occurrence/

curl --header "Content-Type: application/json" --request POST --data '{"author":"user3", "address":"Rua Dr. Mario Sacramento, Aveiro" , "description":"Acidente entre motociclo e viatura.", "category":"INCI_COND"}'  http://localhost:8000/api/occurrence/

curl --header "Content-Type: application/json" --request POST --data '{"author":"user2", "address":"Rua Santa Maria da Feira, Aveiro" , "description":"Estrada cortada devido a obras.", "category":"CONS_COND"}'  http://localhost:8000/api/occurrence/