run:
	python3 -m uvicorn app.main:app --reload

lint:
	python3 -m black . --check --exclude /venv
	python3 -m flake8 .

beautify:
	python3 -m black . --exclude /venv

test:
	python3 -m pytest -v

build_image:
	docker build . -t faisshf

run_image:
	docker run -p 8000:8000 faisshf
