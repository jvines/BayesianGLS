#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="bgls",
    version="0.0.1",
    author="Jose Vines",
    author_email="jose.vines@ug.uchile.cl",
    maintainer="Jose Vines",
    maintainer_email="jose.vines@ug.uchile.cl",
    description="Bayesian Generalized Lomb Scargle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/jvines/BayesianGLS",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    requires=["numpy", "numba"],
    include_package_data=True,
    python_requires='>=3.6',
)
