import os
import re

def find_files_without_abstract(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    pattern = r'\babstract\b|\ba\s*b\s*s\s*t\s*r\s*a\s*c\s*t\b'
                    if not re.search(pattern, content, re.IGNORECASE):
                        file_list.append(file)
    return file_list

# Example usage
directory_path = '/Users/lucianamacedo/Downloads/corpus_teste_limpeza'
files_without_abstract = find_files_without_abstract(directory_path)
file_names = [os.path.basename(file) for file in files_without_abstract]
print(file_names)