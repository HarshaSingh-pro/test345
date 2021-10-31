 

# importing os module
import os
 
# Directory
directory = "/practice"
 
# Parent Directory path
parent_dir = r"C:/Users/Saurav/OneDrive/Pictures/Saved Pictures"
 
# Path
path = os.path.join(parent_dir, directory)
 
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)
 
# Directory
directory = "/practice"
 
# Parent Directory path
parent_dir = r"C:/Users/Saurav/OneDrive/Pictures/Saved Pictures"
 
# mode
mode = 0o666
 
# Path
path = os.path.join(parent_dir, directory)
 
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)