"""
GitHub Helper – generate README, LICENSE, .gitignore, and project folder structure.
"""

import os
import datetime

def create_readme(project_name, description):
    lines = [
        f"# {project_name}",
        "",
        description,
        "",
        "## Installation",
        "",
        "```bash",
        f"git clone https://github.com/yourusername/{project_name}",
        f"cd {project_name}",
        "# further instructions",
        "```",
        "",
        "## Usage",
        "",
        "```bash",
        "python main.py",
        "```",
        "",
        "## License",
        "",
        "MIT"
    ]
    return "\n".join(lines)

def create_license(year, author):
    return f"""MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def create_gitignore():
    return """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*.so

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/

# Logs
*.log
"""

def create_project_structure(project_name):
    base = os.path.join(os.getcwd(), project_name)
    dirs = ['src', 'tests', 'docs']
    files = [('README.md', '# ' + project_name), ('main.py', 'def main():\n    print("Hello, world!")\n\nif __name__ == "__main__":\n    main()')]
    os.makedirs(base, exist_ok=True)
    for d in dirs:
        os.makedirs(os.path.join(base, d), exist_ok=True)
    for fname, content in files:
        with open(os.path.join(base, fname), 'w') as f:
            f.write(content)
    return base

def run():
    print("\n📂 GitHub Helper")
    print("-" * 40)

    # Generate README
    proj_name = input("Project name: ").strip() or 'myproject'
    desc = input("Short description: ").strip() or 'A Python project.'
    readme = create_readme(proj_name, desc)
    with open('README.md', 'w') as f:
        f.write(readme)
    print("✅ README.md created.")

    # Generate LICENSE
    author = input("Author name: ").strip() or 'Your Name'
    year = datetime.datetime.now().year
    license_text = create_license(year, author)
    with open('LICENSE', 'w') as f:
        f.write(license_text)
    print("✅ LICENSE created.")

    # Generate .gitignore
    with open('.gitignore', 'w') as f:
        f.write(create_gitignore())
    print("✅ .gitignore created.")

    # Create project folder structure
    create_proj = input("Create project folder structure? (y/n): ").strip().lower()
    if create_proj == 'y':
        folder = create_project_structure(proj_name)
        print(f"✅ Project structure created at: {folder}")
