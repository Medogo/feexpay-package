from setuptools import setup, find_packages

setup(
    name="feexpay",
    version="0.1.0",
    description="A Python package for handling mobile and card payments via the FeexPay API",
    author="feexpay team",
    author_email="contact@feexpay.me",
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
