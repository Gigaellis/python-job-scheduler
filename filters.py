"""
Filtering logic (safe placeholder).
"""

def filter_jobs(jobs):
    filtered = []
    for j in jobs:
        if j["pay"] <= 0:
            continue
        if j["onsite_hours"] <= 0:
            continue
        filtered.append(j)
    return filtered
