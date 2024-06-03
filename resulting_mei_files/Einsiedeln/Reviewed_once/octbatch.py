import os, octupdate
directory = os.fsencode("C:\\Users\\cole_\\Documents\\GitHub\\e2e-omr-resources\\resulting_mei_files\\Einsiedeln\\Reviewed_once")

i = 0 #for debugging
for mefile in os.listdir(directory):
    filename = os.fsdecode(mefile)
    if filename.endswith(".mei") and not filename.endswith("NEW.mei"):
        octupdate.main(filename)
        print(filename +" has been updated")
     #   i+=1

    #if i>=100:
    #    break
#print(err)