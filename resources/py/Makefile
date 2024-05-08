dev:
	pip install -e ".[dev]"

install:
	pip install -r requirements.txt

install-dev:
	make install
	pip install -r dev-requirements.txt

lint:
	ruff check ./guardrails_api_client

lint-fix:
	ruff check ./guardrails_api_client --fix

type:
	# Fails bc pyright doesn't account for hasattr checks
	pyright guardrails_api_client 

qa:
	make lint
	make type