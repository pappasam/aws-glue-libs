"""A simple setup process to get local glue auto completions

Update this fork when you need the latest completions.
"""

from setuptools import find_packages, setup

setup(
    name="awsglue",
    version="1.0",
    long_description="da kine for da kine",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
