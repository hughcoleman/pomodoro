#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# setup.py
# Copyright (c) 2020 Hugh Coleman
#
# This file is part of hughcoleman/pomodoro, a Pomodoro timer for the command
# line. It is released under the MIT License (see LICENSE.)

import setuptools
from pathlib import Path

with open(Path(__file__).parent / "README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pomodoro",
    version="1.0.0",
    author="Hugh Coleman",
    author_email="33557709+hughcoleman@users.noreply.github.com",
    url="https://github.com/hughcoleman/pomodoro",
    license="MIT",
    description="A Pomodoro timer for the command line.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers = [
        # TODO    
    ],
    platforms="any",
    scripts=["pomodoro"]
)
