ARGUMENTS = $(filter-out $@,$(MAKECMDGOALS)) $(filter-out --,$(MAKEFLAGS))


ifneq (,$(wildcard ./.env))
	include .env 
	export
	ENV_FILE_PARAM = --env-file .env
endif

build:
	docker-compose up -d --build $(ARGUMENTS) --remove-orphans
up:
	docker-compose up $(ARGUMENTS)
down:
	docker-compose down $(ARGUMENTS)
logs:
	docker-compose logs $(ARGUMENTS)
prune: 
	docker system prune
