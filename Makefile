run:
	python3 -m uvicorn app.main:app --reload

lint:
	python3 -m black . --check --exclude /venv
	python3 -m flake8 .

beautify:
	python3 -m black . --exclude /venv

test:
	python3 -m pytest -v