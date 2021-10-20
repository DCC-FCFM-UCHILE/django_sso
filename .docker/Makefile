# makefile

install:
	chmod +x app/secret.sh
	./app/secret.sh
	vim app/.env

build:
	docker-compose -f ../dc-produccion.yml up -d --build --force-recreate --remove-orphans
	docker ps

update:
	git stash
	git pull
	git stash pop
	docker exec django_sso python manage.py collectstatic --no-input

migrate:
	docker exec django_sso python manage.py migrate

ssh:
	docker exec -it django_sso bash

