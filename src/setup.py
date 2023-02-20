from setuptools import setup

setup(
    name="waterland",
    version="0.1",
    packages=["waterland"],
    install_requires=[
        "click==8.1.3",
    ],
    extras_require={
        "dev": [
            "pytest==7.2.1",
        ],
    }
)
