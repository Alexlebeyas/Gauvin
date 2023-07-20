#init-dev: init
#	pip3 install -q -r requirements-dev.txt
#init:
#	pip3 install -q -r requirements.txt

lint:
	pylint --load-plugins pylint_django **/*.py
