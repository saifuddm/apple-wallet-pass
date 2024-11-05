import hashlib
import json
import os

pass_directory = "hugpass"
manifest = {}

# Delete signature file if present
if os.path.exists(os.path.join(pass_directory, 'signature')):
    os.remove(os.path.join(pass_directory, 'signature'))

# Delete hugpass.pkpass if present
if os.path.exists(os.path.join(pass_directory, 'hugpass.pkpass')):
    os.remove(os.path.join(pass_directory, 'hugpass.pkpass'))

# Delete manifest.json if present
if os.path.exists(os.path.join(pass_directory, 'manifest.json')):
    os.remove(os.path.join(pass_directory, 'manifest.json'))

for root, dirs, files in os.walk(pass_directory):
    for file in files:
        file_path = os.path.join(root, file)
        relative_path = os.path.relpath(file_path, pass_directory)
        with open(file_path, 'rb') as f:
            file_hash = hashlib.sha1(f.read()).hexdigest()
        manifest[relative_path.replace("\\", "/")] = file_hash

with open(os.path.join(pass_directory, 'manifest.json'), 'w') as f:
    json.dump(manifest, f, indent=4)
