#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
file : event.py
created time : 2025/01/17
author : Zhenyu Wei, YiTao Ge
copyright : (C)Copyright 2024-present, Southeast University
"""

from typing import List
from transeventpy.core.event import Event


def load_events(events_file_path: str) -> List[Event]:
    """This function read a .npz file and returns a list of `transeventpy.core.Event` objects."""
    pass


def save_events(event_file_path: str, event_list: List[Event]) -> None:
    """This function save a list of `transeventpy.core.Event` objects to a `.npz` file."""
    pass
