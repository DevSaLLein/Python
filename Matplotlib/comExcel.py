import numpy as np
import matplotlib.pyplot as plt
import numpy
import csv
file = open('file.csv')
reader = csv.reader(file)
array = ['','','', '','','','','',''];
i = 0
for x in reader:
    test = numpy.array_split(x, 1)
    array[i] = numpy.array_split(x, 1)

    i += 1
 #   list = x.array_split(x, 2);

for x in array:
    print(x)




#plt.grid();
#plt.scatter(x, y);
#plt.show();