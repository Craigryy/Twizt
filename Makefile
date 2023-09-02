# Define variables
APP_NAME = TODO
PYTHON = python
PIP = pip
FLASK = flask
GUNICORN = gunicorn


# Development tasks
install-dependencies:
	$(PIP) install -r requirements.txt

run-dev:
	$(PYTHON) app.py



# Docker-compose
run-docker:
	sudo docker-compose build && sudo docker-compose up

# Deployment tasks
deploy-heroku:
	heroku create
	git add .
	git commit -m "initial commit"
	git push heroku master

# Common tasks
clean:
	rm -rf _pycache_ *.pyc *.pyo
	
# Default task
help:
	@echo "Available tasks:"
	@echo "  install-dependencies  : Install Python and frontend dependencies"
	@echo "  run-dev               : Run the Flask app locally for development"
	@echo "  run-docker            : Build and run the app using Docker Compose"
	@echo "  deploy-heroku         : Deploy the app to Heroku"
	@echo "  clean                 : Clean up temporary files"
	@echo "  help                  : Show this help message"

.PHONY: install-dependencies run-dev ev run-docker deploy-heroku clean help
