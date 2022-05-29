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
