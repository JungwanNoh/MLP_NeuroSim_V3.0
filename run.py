import subprocess
import os

# Add execute permission to 'makerun.sh'
subprocess.run(["chmod", "+x", "makerun.sh"], check=True)

# Run the shell script
subprocess.run(["./makerun.sh"], check=True)
