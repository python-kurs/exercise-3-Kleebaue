# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script

# ---------

# Counts the occurences of each item in a text file
def count(listtocount):
    [[y,listtocount.count(y)] for y in set(listtocount)]
    return(dict((y,listtocount.count(y)) for y in set(listtocount)))

# write csv file file to outputdirectory
def writefile(file,outputdirectory,filename,fieldname1,fieldname2):
    import csv
    with open(outputdirectory / filename, "w") as fd:
        writer = csv.DictWriter(fd, fieldnames=[fieldname1, fieldname2]) 
        writer.writeheader()
        for key in file.keys():
            fd.write("%s,%s\n"%(key,file[key]))

