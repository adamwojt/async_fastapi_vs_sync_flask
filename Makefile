.PHONY: fastapi flask

fastapi:
	poetry run uvicorn main_fastapi:app --port 8000

flask:
	poetry run gunicorn main_flask:app -b :8001 --log-level DEBUG

test:
	poetry run python test_speed.py
