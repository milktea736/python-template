======================
cookiecutter python template
======================

This is template for a Python. 
This template provides two kind of templates (``library`` / ``service``), you can select when starting project with cookiecutter.
    | - ``library``: provide as a library, use import library with ``import``
    | - ``service``: run as a web service, access your service with ``RESTful API``
Start your project with ``$ cookiecutter git@gitlab.com:milktea736/python-template.git``


Concepts
========
- Use ``cookiecutter`` to generate project template.
- Use ``tox`` to manage CI / CD tasks
- Use ``pre-commit`` to manage git hooks.
- Use ``bumpversion`` to manage project version information.
- The ``fastapi`` is a project built-in web framework, you can also use other frameworks you like.


Requirements
=============

- Support Python > 3.8
- Python packages: ``cookiecutter``, ``tox``, ``pre-commit``, ``bumpversion``, ``fastapi`` and ``uvicorn[standard]``
- Install ``cookiecutter``, ``tox``, ``pre-commit`` and ``bumpversion`` globally
- Install ``fastapi`` and ``uvicorn[standard]`` in your project venv

*Notes*:
- This repository based on cookiecutter-pylibrary, please follow the details `here <https://github.com/ionelmc/cookiecutter-pylibrary>`_