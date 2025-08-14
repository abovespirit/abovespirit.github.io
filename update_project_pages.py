import os
import glob

def get_head_template(relative_depth):
    """Generate the head template with correct relative paths based on depth."""
    # Calculate the relative path prefix (e.g., "../" for depth 1, "../../" for depth 2, etc.)
    relative_prefix = '../' * relative_depth
    
    return f'''    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Project</title>
    <!-- Main CSS -->
    <link rel="stylesheet" href="{relative_prefix}CSS/main.css" />
    <!-- User Information CSS -->
    <link rel="stylesheet" href="{relative_prefix}CSS/userinformationstyle.css?v=1.0" />
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
    <!-- Material Icons -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&display=swap" />
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" />
    <!-- Custom Favicon -->
    <link rel="icon" href="{relative_prefix}Resources/favicon/pilfav.png" type="image/png"/>'''

def update_html_file(file_path, relative_depth):
    """Update a single HTML file with the correct head template."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the head section
        head_start = content.find('<head>')
        head_end = content.find('</head>')
        
        if head_start != -1 and head_end != -1:
            # Generate the head template with the correct relative depth
            head_content = get_head_template(relative_depth)
            
            # Replace the head content with our template
            new_content = content[:head_start + 6] + '\n' + head_content + '\n  ' + content[head_end:]
            
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
            return True
        else:
            print(f"Could not find head section in: {file_path}")
            return False
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return False

def process_directory(directory_path, relative_depth):
    """Process all HTML files in a directory with the given relative depth."""
    html_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    success_count = 0
    for file_path in html_files:
        if update_html_file(file_path, relative_depth):
            success_count += 1
    
    return success_count, len(html_files)

# Main execution
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define directories to process with their relative depth from the HTML files to the root
    directories_to_process = [
        (os.path.join(base_dir, 'Projects'), 2),  # Projects are 2 levels deep (e.g., Projects/ProjectName/file.html)
        (os.path.join(base_dir, 'development'), 2)  # Development projects are also 2 levels deep
    ]
    
    total_updated = 0
    total_files = 0
    
    for directory, depth in directories_to_process:
        if os.path.exists(directory):
            print(f"\nProcessing directory: {directory}")
            updated, total = process_directory(directory, depth)
            total_updated += updated
            total_files += total
        else:
            print(f"\nDirectory not found: {directory}")
    
    print(f"\nUpdate complete! Processed {total_files} files, successfully updated {total_updated}.")
