start:
	docker compose up -d

stop:
	docker compose stop

down:
	docker compose down

restart:
	docker compose restart

pythonStart:
	python3 manage.py runserver

createMigration:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

turboStart: start pythonStart
