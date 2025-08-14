import os
import glob

# Define the base directory for the project
base_dir = os.path.dirname(os.path.abspath(__file__))
projects_dir = os.path.join(base_dir, 'Projects')

# Template for the head section with all necessary dependencies
head_template = '''    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Project</title>
    <!-- Main CSS -->
    <link rel="stylesheet" href="../../CSS/main.css" />
    <!-- User Information CSS -->
    <link rel="stylesheet" href="../../CSS/userinformationstyle.css?v=1.0" />
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
    <!-- Material Icons -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&display=swap" />
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" />
    <!-- Custom Favicon -->
    <link rel="icon" href="../../Resources/favicon/pilfav.png" type="image/png"/>'''

# Find all HTML files in the Projects directory
html_files = []
for root, dirs, files in os.walk(projects_dir):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

# Update each HTML file
for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the head section
        head_start = content.find('<head>')
        head_end = content.find('</head>')
        
        if head_start != -1 and head_end != -1:
            # Replace the head content with our template
            new_content = content[:head_start + 6] + '\n' + head_template + '\n  ' + content[head_end:]
            
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
        else:
            print(f"Could not find head section in: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

print("\nUpdate complete!")
