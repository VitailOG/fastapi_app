from src.lib.celery.main import app


@app.task
def t():
    print('------------')
