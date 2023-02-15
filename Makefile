.PHONY: fastapi flask

fastapi:
	uvicorn main_fastapi:app --port 8000

flask:
	gunicorn main_flask:app -b :8001 --log-level DEBUG

test:
	python test_speed.py
