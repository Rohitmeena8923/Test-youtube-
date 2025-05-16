from setuptools import setup, find_packages

setup(
    name="youtube-telegram-bot",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "python-telegram-bot>=20.3",
        "pytube>=15.0.0",
        "python-dotenv>=1.0.0",
    ],
)