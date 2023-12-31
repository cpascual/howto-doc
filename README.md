# howto-doc
Example project for teaching good practices on documentation of python projects

## Browse the project and the pre-built docs

This project publishes its pre-built docs in: https://cpascual.github.io/howto-doc/

You can see the project itself in : https://github.com/cpascual/howto-doc/

## Build the docs yourself from a clone of this repo

You may [clone / fork this project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) and then build the docs with sphinx-build (I recommend using a fresh python virtual environment with `sphinx` and `sphinx-autoapi` installed).

For example:

> ```console
> git clone https://github.com/cpascual/howto-doc.git
> python -m venv venv
> source ./venv/bin/activate
> pip install sphinx sphinx-autoapi
> sphinx-build -aE -b html docs/source/ docs/build/html
> firefox docs/build/html/index.html
> ```


## Create a project like this one from scratch

It is highly recommended to **start with a fresh venv**, created with e.g. conda or `python -m venv venv && source ./venv/bin/activate`)

1. Create fresh git repo. This can be done, e.g, by creating a new project in github with a README, a python-style .gitignore and a license file and then cloning it locally.
2. Install sphinx and autoapi: `pip install sphinx sphinx-autoapi`
3. Create a dummy python project under `src/myproject` and write its docstrings.
4. Create the `docs` dir and bootstrap sphinx (I chose separate source and build dirs in my case):
   ```console
   $ mkdir docs
   $ cd docs
   $ sphinx-autostart
   ```
5. Edit the bootstrapped `docs/source/conf.py` to customize it (e,g, select the theme, enable and configure the `autoapi` extension, ...)
6. Populate index.rst (you may include other .rst files and add them to the `.. toctree::` directive in `index.rst` and they will be added to your docs)
