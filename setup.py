from setuptools import setup, find_namespace_packages

setup(
    name="brbcoffee_logging",
    version="1.2.0",
    packages=find_namespace_packages(include=["brbcoffee.*"]),
    python_requires=">=3.5",
    dependency_links=[],
)
