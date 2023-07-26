lint:
	pylint --load-plugins pylint_django **/*.py
	flake8
