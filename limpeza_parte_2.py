import glob
import re

def delete_lines(file_pattern):
    filepaths = glob.glob(file_pattern)
    for filepath in filepaths:
        # Read the contents of the file
        with open(filepath, 'r') as file:
            lines = file.readlines()

        # Apply re.sub for each line to modify specific cases
        lines = [re.sub(r'(http[s]?://|www\.)\S+', '', line) for line in lines]
        lines = [re.sub(r'Page \d{1,2} of \d{1,2}$', '', line) for line in lines]
        lines = [re.sub(r'[α-ωΑ-Ω]', '', line) for line in lines]  # Remove Greek letters
        lines = [re.sub(r'[\u0400-\u04FF]', '', line) for line in lines]  # Remove Cyrillic script
        lines = [re.sub(r'[⁰-⁹⁺⁻⁼⁽⁾ⁿᵃᵇᵈᵉʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻ]', '', line) for line in lines]  # Remove superscript and subscript characters
        lines = [re.sub(r'[‡†*#§µ௛~τ²σ²γΨ𝑙β½+\-=/^=∑ρπ∈$¥≥≤\\/²°"\,\']', '', line) for line in lines]  # Remove additional characters

        # Remove lines with less than 5 characters, empty lines, and lines containing numbers only
        lines = [line for line in lines if len(line.strip()) > 5 and not re.match(r'^[0-9]+$', line.strip())]

        # Write the modified lines back to the file
        with open(filepath, 'w') as file:
            file.writelines(lines)

        print(f"Lines modified in {filepath}.")


# Example usage with wildcard file pattern
file_pattern = './*.txt'  # Replace with your wildcard file pattern
delete_lines(file_pattern)
