import re

def sanitize_file(source, output):
    
    sanitized_content = ""
    
    with open(source, "r") as source_file:
        content = source_file.read()
        for char in content:
            if not char.isdigit():
                sanitized_content += char
    with open(output, "w") as output_file:
        output_file.write(sanitized_content)
