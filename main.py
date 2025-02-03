import subprocess
import os


def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")


if __name__ == "__main__":
    # Check if library.db exists, if not, run setup_db.py.py
    if not os.path.exists("library.db"):
        print("Database not found. Running setup_db.py...")
        run_script("setup_db.py")
    else:
        print("Database already exists. Skipping setup_db.py")


    # Run the main library application
    print("Launching library.py...")
    run_script("library.py")