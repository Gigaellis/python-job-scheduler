"""
Utility functions for safe scheduler.
"""

import json
from math import radians, sin, cos, atan2
from datetime import datetime


def travel_hours_between(loc1, loc2):
    """Simple Haversine + placeholder speed model."""
    lat1, lon1 = loc1["lat"], loc1["lon"]
    lat2, lon2 = loc2["lat"], loc2["lon"]

    R = 3958.8
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(dlon/2)**2
    miles = R * 2 * atan2(a**0.5, (1-a)**0.5)

    mph = 45
    return miles / mph + 0.5


def load_sample_jobs(path="examples/sample_jobs.json"):
    with open(path, "r") as f:
        return json.load(f)
