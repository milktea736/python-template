======================
cookiecutter python template
======================

This is template for a Python. 
This template provides two kind of templates (``library`` / ``service``), you can select when starting project with cookiecutter.
    | - ``library``: provide as a library, use library with ``import``
    | - ``service``: run as a web service, access your service with ``RESTful API``
Start your project with ``$ cookiecutter git@gitlab.com:milktea736/python-template.git``


Concepts
========
- Use `cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ to generate project template.
- Use `tox <https://tox.wiki/en/latest/>`_ to manage CI / CD tasks
- Use `pre-commit <https://pre-commit.com/>`_ to manage git hooks.
- Use `bumpversion <https://pypi.org/project/bumpversion/>`_ to manage project version information.
- The `fastapi <https://fastapi.tiangolo.com/>`_ is a project built-in web framework, you can also use other frameworks you like.
- Use `python-dotenv <https://pypi.org/project/python-dotenv/>`_ to manage project configurations. This also provide the flexibility to modify configs when running in containers.
    | - ``src.{{cookiecutter.package_name}}.env`` is used to local developtment.
    | - ``src.{{cookiecutter.package_name}}.env.prod`` is used to deployment which will be copy into container.
- Use ``MANIFEST.in`` to manage non-python files. Please see `packaging pitfalls <https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/>`_
- Currently, the ``requirements.txt`` is used to demo. Please replace it with your project requirements.
    | - Use ``pipenv requirements --dev > requirements.txt`` or ``pipenv requirements > requirements.txt`` to generate your ``requirements.txt`` if you're using `pipenv <https://pipenv.pypa.io/en/latest/>`_.
- Set ``pyenv local 3.8.13 3.9.14 3.10.7``, this makes tox discover your different python version if you're using `pyenv <https://github.com/pyenv/pyenv>`_.
- DONT'T add big file in vcs, save them in S3 or anywhere you like. Then add a script to download them.


Requirements
=============
- Support Python > 3.8
- Python packages: ``cookiecutter``, ``tox``, ``pre-commit``, ``bumpversion``, ``python-dotenv``, ``fastapi`` and ``uvicorn[standard]``
- Install ``cookiecutter``, ``tox``, ``pre-commit`` and ``bumpversion`` globally
- Install ``python-dotenv``, ``fastapi`` and ``uvicorn[standard]`` in your project venv

*Notes*: This repository based on cookiecutter-pylibrary, please follow the details `here <https://github.com/ionelmc/cookiecutter-pylibrary>`_
