hello-direct:
	pipenv run python hello.py

install-in-venv:
	pipenv uninstall hihylang
	pipenv run python setup.py install

hello-package: install-in-venv test

test:
	pipenv run python -m pytest
	pipenv run pytest
