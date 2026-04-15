"""
Ranking logic (safe placeholder).
"""

def rank_jobs(jobs):
    return sorted(jobs, key=lambda j: j.get("eff", 0), reverse=True)
