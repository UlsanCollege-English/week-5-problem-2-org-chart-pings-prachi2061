def count_senior(root, min_level):
    """
    Return how many people in the org tree have level >= min_level.
    Node format: {"name": str, "level": int, "reports": [nodes]}
    """

    # If the tree is empty, return 0
    if root is None:
        return 0

    # Count this person if their level is high enough
    count = 1 if root["level"] >= min_level else 0

    # Recursively count in all reports (children)
    for report in root.get("reports", []):
        count += count_senior(report, min_level)

    return count


# Example test (optional, remove before submission if required)
if __name__ == "__main__":
    org = {
        "name": "Alice",
        "level": 5,
        "reports": [
            {"name": "Bob", "level": 3, "reports": []},
            {"name": "Carol", "level": 4, "reports": [
                {"name": "Dave", "level": 2, "reports": []},
                {"name": "Eve", "level": 5, "reports": []}
            ]}
        ]
    }

    print(count_senior(org, 4))  # Expected output: 3 (Alice, Carol, Eve)
