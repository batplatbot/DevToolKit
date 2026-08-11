"""
GitHub Helper – generate README, LICENSE, .gitignore, and project folder structure.
"""

import os
import datetime

def create_readme(project_name, description):
    template = """# {project_name}

{description}

## Installation

```bash
git clone https://github.com/yourusername/{project_name}
cd {project_name}
# further instructions
