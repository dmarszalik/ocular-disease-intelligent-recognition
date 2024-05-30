from setuptools import setup, find_packages

setup(
    name="my_data_science_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn"
        # Dodaj inne wymagane pakiety
    ]
)