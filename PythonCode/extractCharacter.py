def extract_character_count(line):
    """
    Extracts the character count from a line in the format:
    "Text" (XX characters)
    """
    if '(' in line and 'characters)' in line:
        # Extract the number between the parentheses
        start = line.rfind('(') + 1
        end = line.rfind(' characters)')
        return int(line[start:end].strip())
    else:
        # If the line doesn't follow the expected format, return the length of the line
        return len(line)

def process_file(filename):
    character_counts = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace and check if line is not empty
            line = line.strip()
            if line:
                count = extract_character_count(line)
                character_counts.append(count)

    return character_counts

# Usage
filename = '../DataSet/TXTdata.txt'
character_counts = process_file(filename)
print(character_counts)
print()
print(f"number of texts {len(character_counts)}")