import os
import re

directories = [r"core\fill", r"core\mk_lib"]

for directory in directories:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace absolute imports
                new_content = re.sub(r'from meerk40t\.', 'from core.mk_lib.', content)
                new_content = re.sub(r'import meerk40t\.', 'import core.mk_lib.', new_content)
                
                # Additional fix for svgelements since it's now in the root of mk_lib
                new_content = re.sub(r'from core\.mk_lib\.svgelements', 'from core.mk_lib.svgelements', new_content)
                
                # Fix geomstr imports of fill module
                new_content = re.sub(r'core\.mk_lib\.fill\.fills', 'core.fill.fill.fills', new_content)
                new_content = re.sub(r'core\.mk_lib\.fill\.patternfill', 'core.fill.fill.patternfill', new_content)
                new_content = re.sub(r'core\.mk_lib\.fill\.patterns', 'core.fill.fill.patterns', new_content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Refactored: {filepath}")
