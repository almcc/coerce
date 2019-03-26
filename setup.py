from distutils.core import setup

setup(
    name="coerce",
    version="0.0.0",
    packages=["coerce"],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "pytest-black",
            "black==18.9b0",
            "coveralls==1.6.0",
        ]
    },
)
