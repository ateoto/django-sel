from setuptools import setup

version = __import__('sel').__version__

setup(name = 'django-sel',
    version = version,
    author = 'Matthew McCants',
    author_email = 'mattmccants@gmail.com',
    description = 'Recipe management for Django',
    license = 'BSD',
    url = 'https://github.com/Ateoto/django-sel',
    packages = ['sel'],
    install_requires = ['django>=1.5', 'django-taggit>=0.10a1'])