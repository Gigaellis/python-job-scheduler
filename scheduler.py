"""
SAFE PORTFOLIO VERSION
----------------------
This is a sanitized demonstration of the scheduling architecture I built.
It shows structure, logic flow, and modular design without exposing any
proprietary algorithms, datasets, or platform‑specific behavior.
"""

from datetime import timedelta
from utils import travel_hours_between, load_sample_jobs
from filters import filter_jobs
from ranking import rank_jobs


def sliding_anchor_limit(total_jobs: int) -> int:
    """Simple scaling rule for demonstration."""
    if total_jobs <= 8:
        return total_jobs
    elif total_jobs < 15:
        return 15
    return 25


def sliding_subset_limit(anchor_count: int) -> int:
    """Subset size rule for demonstration."""
    if anchor_count <= 8:
        return anchor_count
    elif anchor_count == 15:
        return 4
    return 3


def solo_eff(job, home_loc):
    """Basic efficiency formula (safe placeholder)."""
    travel = travel_hours_between(home_loc, job)
    return job["pay"] / (job["onsite_hours"] + travel * 2)


def group_jobs_by_date(jobs):
    """Group jobs by date for daily scheduling."""
    grouped = {}
    for j in jobs:
        d = j.get("date")
        if d:
            grouped.setdefault(d, []).append(j)
    return grouped


def run_daily_schedule(jobs_for_day, home_loc):
    """Simplified daily scheduler (safe placeholder)."""
    ranked = sorted(jobs_for_day, key=lambda j: solo_eff(j, home_loc), reverse=True)
    return ranked[:5]  # show top 5 for demo


def run_pipeline():
    print(">>> SAFE SCHEDULER DEMO <<<\n")

    home_loc = {"lat": 29.7, "lon": -85.0}  # fake home coords

    jobs = load_sample_jobs()
    jobs = filter_jobs(jobs)

    grouped = group_jobs_by_date(jobs)

    for day, todays in sorted(grouped.items()):
        print(f"\n=== {day} ===")

        anchor_limit = sliding_anchor_limit(len(todays))
        subset_limit = sliding_subset_limit(anchor_limit)

        print(f"Using {anchor_limit} anchors, subset size {subset_limit}")

        best = run_daily_schedule(todays, home_loc)

        for j in best:
            print(f"- {j['title']} | Pay ${j['pay']} | Eff {solo_eff(j, home_loc):.2f}")


if __name__ == "__main__":
    run_pipeline()
