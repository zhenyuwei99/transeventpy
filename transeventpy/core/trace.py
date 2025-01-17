#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
file : trace.py
created time : 2025/01/17
author : Zhenyu Wei, YiTao Ge
copyright : (C)Copyright 2024-present, Southeast University
"""


class Trace:
    def __init__(self):
        self._dt = None
        self._t_vec = None
        self._v_vec = None
        self._is_contain_current = True

    @property
    def dt(self):
        pass
