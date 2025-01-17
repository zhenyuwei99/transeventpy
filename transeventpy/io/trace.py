#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
file : trace.py
created time : 2025/01/17
author : Zhenyu Wei, YiTao Ge
copyright : (C)Copyright 2024-present, Southeast University
"""

from transeventpy.core.trace import Trace


def load_trace(trace_file_path: str) -> Trace:
    """This function read a .npz file and returns a `transeventpy.core.Trace` object."""
    pass


def save_trace(trace_file_path: str, trace: Trace) -> None:
    """This function save a `transeventpy.core.Trace` object to a `.npz` file."""
    pass
