# Programming Assignment 1: Stable Matching

This project implements the hospital-proposing Gale–Shapley stable matching algorithm and a verifier that checks whether a given matching is valid and stable. The project also includes a scalability experiment that measures the runtime of the matcher and verifier for increasing input sizes.

## Authors

Carlos Felipe - UFID 70583368  
Alexis Morales - UFID 20325573  


## Task A: Matching Engine

The file matcher.py implements the hospital-proposing Gale–Shapley algorithm.  
It reads an input file containing preference lists and prints a stable matching to standard output.

### How to run the matcher

    python3 src/matcher.py data/example.in

To save the output to a file:

    python3 src/matcher.py data/example.in > data/example.out

## Task B: Verifier

The file verifier.py checks whether a given matching is:
- Valid: every hospital and student is matched exactly once.
- Stable: there is no blocking pair.

### How to run the verifier

    python3 src/verifier.py data/example.in data/example.out

Possible outputs:
   - VALID STABLE
   - INVALID: reason
   - UNSTABLE: blocking pair (h, s)

Several invalid and unstable example matchings are included in the data folder for testing.

## Assumptions

- Preference lists are complete and contain strict rankings.
- The number of hospitals equals the number of students.
