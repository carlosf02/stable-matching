import sys
from matcher import read_input


def read_matching(filename, n):
    with open(filename, "r") as f:
        lines = []
        for line in f:
            line = line.strip()
            if line:
                lines.append(line)

    if len(lines) != n:
        raise ValueError("Incorrect number of matching lines")

    hospital_match = [-1] * n
    student_match = [-1] * n

    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            raise ValueError("Invalid matching format")

        h = int(parts[0]) - 1
        s = int(parts[1]) - 1

        if h < 0 or h >= n or s < 0 or s >= n:
            raise ValueError("Matching index out of range")

        if hospital_match[h] != -1:
            raise ValueError("Hospital appears more than once")

        if student_match[s] != -1:
            raise ValueError("Student appears more than once")

        hospital_match[h] = s
        student_match[s] = h

    # Check that everyone is matched
    for h in range(n):
        if hospital_match[h] == -1:
            raise ValueError("Hospital is unmatched")

    for s in range(n):
        if student_match[s] == -1:
            raise ValueError("Student is unmatched")

    return hospital_match, student_match


def check_stability(n, hospital_pref, student_pref, hospital_match, student_match):
    # Build student rank table
    student_rank = [[0] * n for _ in range(n)]
    for s in range(n):
        for rank in range(n):
            h = student_pref[s][rank]
            student_rank[s][h] = rank

    # Check for blocking pairs
    for h in range(n):
        assigned_student = hospital_match[h]

        for s in hospital_pref[h]:
            if s == assigned_student:
                break  # no better students beyond this point

            current_h = student_match[s]

            # Student prefers this hospital more
            if student_rank[s][h] < student_rank[s][current_h]:
                return False, h, s

    return True, None, None


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 verifier.py <input_file> <matching_file>")
        return

    try:
        # Read original preferences
        n, hospital_pref, student_pref = read_input(sys.argv[1])

        # Read matching
        hospital_match, student_match = read_matching(sys.argv[2], n)

        # Check stability
        stable, h, s = check_stability(
            n, hospital_pref, student_pref, hospital_match, student_match
        )

        if stable:
            print("VALID STABLE")
        else:
            print("UNSTABLE: blocking pair ({}, {})".format(h + 1, s + 1))

    except ValueError as e:
        print("INVALID:", e)


if __name__ == "__main__":
    main()
