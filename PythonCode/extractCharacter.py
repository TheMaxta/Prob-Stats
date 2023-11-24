import random
import csv

def generate_sample_population(character_counts, sample_size, random_seed=None):
    """
    Generates a random sample population from a list of character counts.
    
    Args:
        character_counts (list): List of character counts.
        sample_size (int): Size of the sample population.
        random_seed (int): Seed for random number generation (optional).
    
    Returns:
        list: Randomly selected character counts in the sample population.
    """
    if random_seed is not None:
        random.seed(random_seed)
    
    # Check if the sample size is greater than the total number of character counts
    if sample_size > len(character_counts):
        raise ValueError("Sample size cannot exceed the total number of character counts.")
    
    # Randomly select character counts for the sample population
    sample_population = random.sample(character_counts, sample_size)
    
    return sample_population

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

def write_dataset_to_file(character_counts, output_filename, output_format="txt"):
    """
    Writes the full dataset of character counts to a file in the specified format.
    
    Args:
        character_counts (list): List of character counts.
        output_filename (str): Name of the output file.
        output_format (str): Format of the output file ("txt" or "csv").
    """
    if output_format == "txt":
        with open(output_filename, 'w') as file:
            for count in character_counts:
                file.write(f"{count}\n")
    elif output_format == "csv":
        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for count in character_counts:
                writer.writerow([count])
    else:
        raise ValueError("Invalid output format. Use 'txt' or 'csv'.")

# Usage
filename = '../DataSet/TXTdata.txt'
character_counts = process_file(filename)
print(character_counts)
print()
print(f"number of texts {len(character_counts)}")


# Set a random seed for reproducibility (optional)
random_seed = 42

# Generate a sample population of size 10 with the specified random seed
sample_size = 30
sample_population = generate_sample_population(character_counts, sample_size, random_seed)

# Print the sample population
print(sample_population)
print()
print(f"Sample size: {len(sample_population)}")

# Write the full dataset of character counts to a new file
write_dataset_to_file(character_counts, "CharLengthDataset.csv", output_format="csv")
