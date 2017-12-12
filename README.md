# How to publish a Python package with Hy code?

[Hy language](https://hylang.org) is great: with it you to code in a Pythonic Lisp dialect and
embed that code directly in your Python applications.

No other runtime needed! Just the `hy` package.

However at first you may struggle (like me) to create a package including Hy code.
This is no big deal when you know which `setuptools` magic words to invoke.

Let's wrap up!

## Step 1: code your `.hy` files

You can put them in your package, like you do with your Python files.

This gives you a file tree like that:

```
setup.py
<your_package_name>>/
	__init__.py
	<one_hy_module>.hy
	<another_hy_module>.hy
```

## Step 2: add an `import hy`

If you want your users to use directly your code without to have themselves
to think about installing and importing Hy, you must do it for them.

So in your package `__init__.py`, add the following line:

```
import hy
```

## Step 3: announce your package depends on Hy

To import Hy successfully, your users first need it installed.
Easy, tell that your package depends on Hy, as you would for any other dependency:

in `setup.py`:
```
setup(
	# ...
	install_requires=[
		'hy'
	]
	# ...
)
```

## Step 4: tell `setuptools` to include `.hy` files

Finally for your users to call your Hy code, you must ensure it is duly included
in the final package.

in `setup.py`:
```
setup(
	# ...
	package_data={
		'<your_package_name>': ['*.hy']
	}
	# ...
)
```

## Final Step: create your package

You're done with the configuration.

You can test your package with:
```
python setup.py sdist bdist_wheel
```

Install it locally (to test it) with:
```
# De-install the previous version, if any.
pip uninstall <your_package_name>
python setup.py install
```

Finally when you're happy with it, you can publish it to PyPI:
```
# Register your package.
python setup.py register -r pypi
# Upload it!
python setup.py sdist bdist_wheel --universal upload -r pypi
```

You may also use [twine](https://github.com/pypa/twine) for a more secure and consistent
upload to PyPI. In this case, do:

```
python setup.py sdist bdist_wheel
twine upload dist/*
```

----------------------------------

Enjoy your Hy programming!

Yoan - https://blog.ytotech.com
