import sys

def read_input(filename):
    with open(filename, "r") as f:
        lines = []
        for line in f:
            line = line.strip()
            if line:
                lines.append(line)

    if len(lines) == 0:
        raise ValueError("Empty input file")

    n = int(lines[0])
    if n <= 0:
        raise ValueError("n must be positive")

    if len(lines) != 1 + 2 * n:
        raise ValueError("Incorrect number of preference lines")

    hospital_pref = []
    student_pref = []

    # Read hospital preferences
    for i in range(1, 1 + n):
        nums = lines[i].split()
        if len(nums) != n:
            raise ValueError("Invalid hospital preference length")

        prefs = []
        seen = set()
        for x in nums:
            val = int(x) - 1
            if val < 0 or val >= n or val in seen:
                raise ValueError("Invalid hospital preference list")
            prefs.append(val)
            seen.add(val)

        hospital_pref.append(prefs)

    # Read student preferences
    for i in range(1 + n, 1 + 2 * n):
        nums = lines[i].split()
        if len(nums) != n:
            raise ValueError("Invalid student preference length")

        prefs = []
        seen = set()
        for x in nums:
            val = int(x) - 1
            if val < 0 or val >= n or val in seen:
                raise ValueError("Invalid student preference list")
            prefs.append(val)
            seen.add(val)

        student_pref.append(prefs)

    return n, hospital_pref, student_pref


def gale_shapley(n, hospital_pref, student_pref):
    hospital_match = [-1] * n
    student_match = [-1] * n
    next_proposal = [0] * n

    student_rank = [[0] * n for _ in range(n)]
    for s in range(n):
        for rank in range(n):
            h = student_pref[s][rank]
            student_rank[s][h] = rank

    # list of free hospitals
    free_hospitals = []
    for h in range(n):
        free_hospitals.append(h)

    # Main algorithm loop
    while len(free_hospitals) > 0:
        h = free_hospitals.pop(0)

        # hospital proposed to everyone
        if next_proposal[h] == n:
            continue

        s = hospital_pref[h][next_proposal[h]]
        next_proposal[h] += 1

        if student_match[s] == -1:
            # student is free
            hospital_match[h] = s
            student_match[s] = h
        else:
            current_h = student_match[s]

            # student prefers new hospital
            if student_rank[s][h] < student_rank[s][current_h]:
                hospital_match[h] = s
                student_match[s] = h

                hospital_match[current_h] = -1
                free_hospitals.append(current_h)
            else:
                # student rejects
                free_hospitals.append(h)

    return hospital_match


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 matcher.py <input_file>")
        return

    try:
        n, hospital_pref, student_pref = read_input(sys.argv[1])
        matching = gale_shapley(n, hospital_pref, student_pref)

        for h in range(n):
            print(h + 1, matching[h] + 1)

    except ValueError as e:
        print("INVALID INPUT:", e)


if __name__ == "__main__":
    main()
