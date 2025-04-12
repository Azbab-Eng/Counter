import os
directory = r"\Users\User\Desktop\Azbab\Python"
y2mate = []
for filename in os.listdir(directory):
    # print(filename)
    if filename.startswith("y2mate.com - "):
        new_file = filename[len("y2mate.com - "):].strip()
        # print(new_file)
        # y2mate.append(filename)
        old_files = os.path.join(directory,filename)
        new_files = os.path.join(directory,new_file)

        os.rename(old_files , new_files)
        print(f"files are changed successful")
print("Removing Y2mate prefix end")    
        


print("###########################")

print("ALHAMDULILLAH")
try:
    os.chdir(r"\Users\User\Desktop\vs code")
except:
    print("can't change directory")
print(os.getcwd())

