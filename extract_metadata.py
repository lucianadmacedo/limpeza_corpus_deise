import os

def extract_metadata(file_path):
    metadata_lines = []
    found_abstract = False  # Flag to track if "abstract" or "a b s t r a c t" is found

    # Read the lines and extract the metadata section
    with open(file_path, 'r') as file:
        for line in file:
            if line.lower().startswith('abstract') or line.lower().startswith('a b s t r a c t'):
                found_abstract = True
                break
            else:
                metadata_lines.append(line)

    if found_abstract:
        # Create a new file name
        new_file_name = file_path.replace('.txt', '_metadata.txt')

        # Write the extracted content to the new file
        with open(new_file_name, 'w') as new_file:
            new_file.writelines(metadata_lines)

        # Delete the metadata section from the original file
        with open(file_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            file.writelines(lines[len(metadata_lines):])

# Example usage
file_path = '/Users/lucianamacedo/Downloads/corpus_teste_limpeza/00440_ART.txt'
extract_metadata(file_path)