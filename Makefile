.PHONY: black-check
black-check:
	black --check --exclude venv .

.PHONY: black-fix
black-fix:
	black --exclude venv .

.PHONY: isort-check
isort-check:
	isort --check-only --skip venv .

.PHONY: isort-fix
isort-fix:
	isort --skip venv .

.PHONY: runserver
runserver8888:
	./manage.py runserver 0.0.0.0:8888

.PHONY: tests
tests:
	coverage run ./manage.py test tests
	coverage report
