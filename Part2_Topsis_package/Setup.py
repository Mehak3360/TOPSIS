from setuptools import setup, find_packages

setup(
   name="topsis_mehak_102303699",
    version="0.2",
    author="Mehak",
    description="TOPSIS implementation in Python",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis_mehak.topsis:main'
        ]
    }
)
