from setuptools import setup, find_packages

requires = [
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'waitress',
    'alembic',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'cornice',
    'gunicorn',
]

development_require = [
    'WebTest',
    'pytest',
    'pytest-cov',
    'debugpy',
]

setup(
    name='{{ cookiecutter.project_name_display }}',
    version='1.0',
    description='{{ cookiecutter.short_description }}',
    long_description='{{ cookiecutter.long_description }}',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    keywords='web pyramid pylons',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'development': development_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = {{cookiecutter.project_name}}:main',
        ],
        'console_scripts': [
            'initialize_{{cookiecutter.project_name}}_db={{cookiecutter.project_name}}.scripts.initialize_db:main',
        ],
    },
)
