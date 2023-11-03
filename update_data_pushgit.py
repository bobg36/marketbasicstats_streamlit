import subprocess
import shutil

source_path = r'C:\Users\bobgu\Desktop\Axie Data\market overview over time\market_overview.csv'

destination_path = './market_overview.csv'
shutil.copy(source_path, destination_path)
print(f"File '{source_path}' has been copied to '{destination_path}'.")

print('pushing data updates to github. website should be live in 40 seconds')
git_add = 'git add .'
git_commit = 'git commit -m "data update"'
git_push = 'git push origin main'
subprocess.run(git_add, shell=True)
subprocess.run(git_commit, shell=True)
subprocess.run(git_push, shell=True)