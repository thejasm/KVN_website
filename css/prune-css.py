import re

# Read the list of unused selectors from a file
with open('remove.txt', 'r', encoding='utf-8') as unused_file:
    unused_selectors = [line.strip() for line in unused_file]

# Print the list of unused selectors
print(f'Unused Selectors: {unused_selectors}')

# Read your CSS file into a string
with open('main.css', 'r', encoding='utf-8') as css_file:
    css_content = css_file.read()

# Print the CSS content before modification
print(f'CSS Content (Before):\n{css_content}')

# Create a regular expression pattern to match the entire selector block
pattern = '|'.join(re.escape(selector) for selector in unused_selectors)

# Define a function to remove the matched selector blocks
def remove_selector(match):
    removed = match.group(0)
    print(f'Removing: {removed}')
    return ''

# Use re.sub with the function to remove the matching selector blocks
css_content = re.sub(r'[^}{]*' + r'({})[^{{}}]*{{[^{{}}]*}}'.format(pattern), remove_selector, css_content)

# Print the CSS content after modification
print(f'CSS Content (After):\n{css_content}')

# Save the modified CSS back to the file
with open('your_styles.css', 'w', encoding='utf-8') as css_file:
    css_file.write(css_content)