import subprocess

# ps1 = subprocess.run(['ls'], universal_newlines=True, stdout=subprocess.PIPE)
# ps2 = subprocess.run(['pwd'], universal_newlines=True, input=ps1.stdout)

ps1 = subprocess.Popen(['xprctl login -u ASahu2 -w qa'], universal_newlines=True, stdout=subprocess.PIPE)
# ps2 = subprocess.Popen(['pwd'], universal_newlines=True, input=ps1.stdout)
# ps3 = subprocess.Popen(['xprctl info'], universal_newlines=True, input=ps2.stdout)
