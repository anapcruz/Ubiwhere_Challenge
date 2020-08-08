# Django rest API - Gestão de ocorrências

Django Rest API que permite a gestão de ocorrências em ambiente urbano.

### Installation
Instalação de todas as dependências e inicializar o servidor django.

```sh
$ docker-compose build
$ docker-compose up 
```

### Base de dados

Criar django admin, com a password **admin**:
```sh
$ docker-compose run web python src/occurrence_project/manage.py createsuperuser --email admin@admin.com --username admin
```

Executar o comando abaixo para o preenchimento da base de dados:

```sh
$ bash fill_database.sh
```

### Endpoints
Registar utilizadores:
```sh
localhost:8000/api/register/
```

Listar e criar ocorrências:
```sh
localhost:8000/api/occurrence/
```

Filtrar ocorrências por autor:
```sh
localhost:8000/api/occurrence/search?author=AUTHOR_NAME
```

Filtrar as ocorrências por categoria:
```sh
localhost:8000/api/occurrence/search?category=TYPE_CATEGORY
```

Tipos de categoria:
  - CONS_COND -> CONSTRUCTION: eventos planeados de obras nas estradas
  -  SPEC_COND -> SPECIAL_EVENT: eventos especiais, por exemplo, concertos
  -  INCI_COND -> INCIDENT: acidentes ou outros eventos inesperados
  -  WTHR_COND -> WEATHER_CONDITION: eventos meteorológicos que efetam as estradas
  -  ROAD_COND -> ROAD_CONDITION: estados das estradas que afetam a circulação

  
Filtrar ocurrências por localização:
```sh
localhost:8000/api/occurrence/search?address==LOCATION_NAME
```

### Collection Postman

Use coleção [postman] para testar a rest API.

License
----

MIT


[//]: #

   [postman]: <https://www.getpostman.com/collections/074b2c99191357c9ac73>
   