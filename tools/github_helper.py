"""
GitHub Helper – generate README, LICENSE, .gitignore, and project folder structure.
"""

import os
import datetime

def create_readme(project_name, description):
    return f"""# {project_name}

{description}

## Installation

```bash
git clone https://github.com/batplatbot/{project_name}
cd {project_name}
# further instructions
