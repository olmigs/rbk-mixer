from setuptools import find_packages, setup

setup(
    name='flaskapp',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'casio_rbk'
        'flask',
        'waitress'
    ],
)