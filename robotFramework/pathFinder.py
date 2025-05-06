import sys
#this is for finding the PATH of python script for robotFramework fix 
for path in sys.path:
    print(path)

##this honestly helped nothing,but as a note : install both the robotframework and robot library in pip
#to make it usable - also install selenium and robotframework-seleniumlibrary later
#also databaselibrary is needed for database testing

#pip install robotframework
#pip install robot
#pip install robotframework-seleniumlibrary
#pip install -U robotframework-databaselibrary