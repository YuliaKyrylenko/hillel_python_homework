import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()
    clean_text = re.sub(r'<[^>]+>', '', html)
    with open(result_file, 'w', encoding='utf-8') as new_file:
        lines = clean_text.splitlines()
        for line in lines:
            if line.strip():
                new_file.write(line.strip() + '\n')
    return clean_text
delete_html_tags('draft.html', 'cleaned.txt')