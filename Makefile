COMPOSE_FILE ?= docker/docker-compose.yml

.PHONY: lint-bandit
lint-bandit:
	bandit --ini .bandit --recursive

.PHONY: lint-black
lint-black:
	black --check --diff ./$(SOURCE_FILES)

.PHONY: lint-flake8
lint-flake8:
	flake8 ./$(SOURCE_FILES)

.PHONY: lint-isort
lint-isort:
	isort --check-only --diff ./$(SOURCE_FILES)

.PHONY: lint-mypy
lint-mypy:
	mypy

.PHONY: lint
lint: lint-black lint-flake8 lint-isort # lint-bandit

.PHONY: fmt
fmt:
	isort .
	black .

.PHONY: docker-up
docker-up:
	docker-compose -f ./docker/docker-compose.yml up --remove-orphans -d
	docker-compose -f ./docker/docker-compose.yml ps

.PHONY: docker-down
docker-down:
	docker-compose -f ./docker/docker-compose.yml down

.PHONY: docker-prune
docker-prune:
	docker container prune -f
	docker volume prune -f
	docker network prune -f

.PHONY: docker-logs
docker-logs:
	docker-compose -f ./docker/docker-compose.yml logs --follow

.PHONY: test
test:
	./myapp/manage.py test ./myapp/tests/



