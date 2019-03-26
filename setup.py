from distutils.core import setup

setup(
    name="coerce",
    version="0.0.0",
    packages=["coerce"],
    extras_require={"dev": ["pytest", "black"]},
)
