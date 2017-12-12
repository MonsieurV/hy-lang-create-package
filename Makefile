install-dev:
	pipenv install --dev

hello-direct:
	pipenv run python hello.py

install-in-venv:
	pipenv uninstall hihylang
	pipenv run python setup.py install

hello-package: install-in-venv test

test:
	echo "Testing local code from source files"
	pipenv run python -m pytest
	echo "Testing from installed package"
	pipenv run pytest

publish:
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload dist/*
