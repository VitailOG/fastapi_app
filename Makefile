#make m:
	export PYTHONPATH="${PYTHONPATH}:/Users/macbookair/PycharmProjects/fastapi_micro_gd"
	export ENV_FILE=/Users/macbookair/PycharmProjects/fastapi_micro_gd/.env
#	python src/apps/cli/main.py migrate m

make m:
	python3 -m src.apps.cli.main migrate init

celery:
	celery -A main.app worker --loglevel=info
