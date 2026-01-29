import time
import random

from matcher import gale_shapley
from verifier import check_stability


def generate_preferences(n):
    hospital_pref = []
    student_pref = []

    for _ in range(n):
        prefs = list(range(n))
        random.shuffle(prefs)
        hospital_pref.append(prefs)

    for _ in range(n):
        prefs = list(range(n))
        random.shuffle(prefs)
        student_pref.append(prefs)

    return hospital_pref, student_pref


def run_experiment(n):
    hospital_pref, student_pref = generate_preferences(n)

    # Time matcher
    start = time.time()
    hospital_match = gale_shapley(n, hospital_pref, student_pref)
    matcher_time = time.time() - start

    # Build student_match for verifier
    student_match = [-1] * n
    for h in range(n):
        s = hospital_match[h]
        student_match[s] = h

    # Time verifier (stability only)
    start = time.time()
    stable, _, _ = check_stability(
        n, hospital_pref, student_pref, hospital_match, student_match
    )
    verifier_time = time.time() - start

    return matcher_time, verifier_time


def main():
    sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

    print("n,matcher_time,verifier_time")

    for n in sizes:
        matcher_time, verifier_time = run_experiment(n)
        print(f"{n},{matcher_time:.7f},{verifier_time:.7f}")


if __name__ == "__main__":
    main()
