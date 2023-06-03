def clean_text_file(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find and remove sections
    keywords = ['acknowledgements', 'funding', 'references']
    cleaned_lines = []
    delete_section = False

    for line in lines:
        lower_line = line.lower().strip()

        if any(keyword in lower_line for keyword in keywords):
            delete_section = True

        if not delete_section:
            cleaned_lines.append(line)

    # Write the cleaned lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(cleaned_lines)

# Usage example
clean_text_file('00443_ART.txt')
