import os
import shutil
import tempfile
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DIST_DIR = os.path.join(ROOT_DIR, "dist")

if not os.path.exists(DIST_DIR):
    raise RuntimeError("dist directory does not exist! Please run 'npm run build' first.")

temp_dir = os.path.join(tempfile.gettempdir(), "cytos_production_release")
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir, ignore_errors=True)

shutil.copytree(DIST_DIR, temp_dir, dirs_exist_ok=True)
print(f"Copied dist contents to {temp_dir}")

def run_git(args, cwd):
    res = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git error ({' '.join(args)}):\n{res.stderr}")
    else:
        print(f"Git success ({' '.join(args)}):\n{res.stdout.strip()}")
    return res

run_git(["init", "-b", "production"], temp_dir)
run_git(["config", "user.name", "Prasad Mhaske"], temp_dir)
run_git(["config", "user.email", "mhaskeprasad44@outlook.com"], temp_dir)
run_git(["add", "-A"], temp_dir)
run_git(["commit", "-m", "Compiled production release for Hostinger public_html (includes .htaccess, assets, images)"], temp_dir)
run_git(["remote", "add", "origin", "https://github.com/mhaskeprasad44/cytos.git"], temp_dir)
res = run_git(["push", "origin", "production", "--force"], temp_dir)

if res.returncode == 0:
    print("SUCCESS: Branch 'production' has been updated on https://github.com/mhaskeprasad44/cytos.git")
else:
    print("Push failed or requires attention.")

shutil.rmtree(temp_dir, ignore_errors=True)
