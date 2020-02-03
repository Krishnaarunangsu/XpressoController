import subprocess

# ps1 = subprocess.run(['ls'], universal_newlines=True, stdout=subprocess.PIPE)
# ps2 = subprocess.run(['pwd'], universal_newlines=True, input=ps1.stdout)

ps1 = subprocess.run(['xprctl -h'], universal_newlines=True, stdout=subprocess.PIPE)
ps2 = subprocess.run(['xprctl list'], universal_newlines=True, input=ps1.stdout)
ps3 = subprocess.run(['xprctl info'], universal_newlines=True, input=ps2.stdout)