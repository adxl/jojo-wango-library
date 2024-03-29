# jojo-wango-library

La bibliothèque de Jojo Wango

## Prérequis

- `python>=3.10`
- `poetry>=1.1.10`

Pour installer `poetry` (OSX) :  
`$ curl -sSL https://install.python-poetry.org | python3 -`

Si ça ne fonctionne pas : [Installation](https://python-poetry.org/docs/)

## Mise en place du projet

1 - configurer poetry : `poetry config virtualenvs.in-project true`  
2 - installer les dependances : `poetry install`  
3 - lancer la BDD : `docker-compose up -d`  
4 - activer l'environnement : `source .venv/bin/activate`  
5 - lancer les migration :  
  ```bash
  python3 manage.py makemigrations`  
  python3 manage.py migrate`
  ```
6 - Importer les données: 
```bash 
docker container exec -i jojo_wango_db psql -U root -d jojo_wango_db < django_dump.sql
```  
NOTE: en cas de fausse manipulation, il faut drop la DB et relancer les migration et le dump  
7 - lancer le serveur : `$ python3 manage.py runserver`

## Django manager

Pour utiliser le manager: `$ python3 manage.py <command>`  
Liste des commandes : `$ python3 manage.py`

Pour créer une entité :  
1 - Créer le model  
2 - `$ python3 manage.py makemigrations`  
3 - `$ python3 manage.py migrate`

## Contributions au projet

[Guide de contribution](https://github.com/adxl/jojo-wango-library/blob/master/CONTRIBUTING.md)
