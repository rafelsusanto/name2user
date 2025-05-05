import argparse

def generate_combinations(name_parts, domain=None):
    name_parts = [part.lower() for part in name_parts]

    if len(name_parts) == 1:
        first = name_parts[0]
        patterns = [
            f"{first}",
        ]

    elif len(name_parts) == 2:
        first, last = name_parts
        f = first[0]
        l = last[0]
        patterns = []

        for sep in ['.', '-', '_']:
            patterns.append(f"{first}{sep}{last}")
            patterns.append(f"{f}{sep}{last}")
            patterns.append(f"{first}{sep}{l}")

        patterns.extend([
            f"{first}{last}",
            f"{f}{last}",
            f"{first}",
            f"{last}"
        ])

    elif len(name_parts) >= 3:
        first, middle, last = name_parts[0], name_parts[1], name_parts[-1]
        f, m, l = first[0], middle[0], last[0]
        patterns = []

        for sep in ['.', '-', '_']:
            patterns.append(f"{first}{sep}{last}")
            patterns.append(f"{f}{sep}{last}")
            patterns.append(f"{first}{sep}{l}")
            patterns.append(f"{first}{sep}{middle}{sep}{last}")
            patterns.append(f"{first}{sep}{m}{sep}{last}")
            patterns.append(f"{f}{sep}{m}{sep}{last}")

        patterns.extend([
            f"{first}{last}",
            f"{f}{m}{last}",
            f"{first}",
            f"{last}"
        ])
    else:
        patterns = []

    return [pattern + '@' + domain if domain else pattern for pattern in patterns]

def main():
    parser = argparse.ArgumentParser(description="Generate common email or username combinations from names.")
    parser.add_argument("-d", "--domain", help="Optional domain name (e.g., test.com)")
    parser.add_argument("-u", "--users", default="user.txt", help="Input file with names")
    parser.add_argument("-o", "--output", help="Optional output file to save results")
    args = parser.parse_args()

    usernames = []

    try:
        with open(args.users, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                combos = generate_combinations(parts, args.domain)
                usernames.extend(combos)
    except FileNotFoundError:
        print(f"[!] File not found: {args.users}")
        return

    # Remove duplicates while preserving order
    unique_usernames = list(dict.fromkeys(usernames))

    # Print all results
    for name in unique_usernames:
        print(name)

    # Save to file only if -o was provided
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            for name in unique_usernames:
                f.write(name + "\n")

if __name__ == "__main__":
    main()
