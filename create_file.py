import csv
with open("st1.csv","w") as f:
    write = csv.writer(f,delimiter=",")
    write.writerow(["one","two","three"])
    write.writerow(["four","five","six"])
    write.writerow(["Hello","World"])
