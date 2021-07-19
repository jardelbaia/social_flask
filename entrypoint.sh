sleep 5s
poetry install
export FLASK_APP=social_flask/__init__.py
poetry run python -c 'import run; run.create_db()'
poetry run flask db init
poetry run flask db migrate
poetry run flask db upgrade
poetry run python run.py