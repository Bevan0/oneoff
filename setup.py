from setuptools import setup

setup(
    name="oneoff",
    version="0.1.0",
    py_modules=["oneoff"],
    install_requires=["click"],
    entry_points={
        'console_scripts': [
            'oneoff = oneoff:run'
        ],
    },
)