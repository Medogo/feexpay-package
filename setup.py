from setuptools import setup, find_packages

setup(
    name="feexpay",
    version="0.1.0",
    description="A Python package for handling mobile and card payments via the FeexPay API",
    author="Dominique Megnidro",
    author_email="votre.email@example.com",
    url="https://github.com/Medogo/feexpay-package.git",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pydantic"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
