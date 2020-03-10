import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import time
import glob
import cv2

X_data = []
files = glob.glob ("C:/Users/usman/neural-net-random-art/final_results/*.PNG")
for myFile in files:
    print(myFile)
    image = cv2.imread (myFile)
    X_data.append (image)

print('X_data shape:', np.array(X_data).shape)

result1 = np.cumsum(X_data[0:6], axis = 0)
print(result1.shape)

result2 = np.cumsum(X_data[6:10], axis = 0)

result3 = np.cumsum(X_data[10:15], axis = 0)
result4 = np.cumsum(X_data[15:], axis = 0)

final_result = np.concatenate((result1, result2, result3, result4))

# plt.imsave('final1.png', final_result[1])

image14 = final_result[16]
plt.imsave("{}".format("final_im14.png"), image14)

# i = 1
# for image in final_result:
# 	fname = "final" + str(i) + ".png"
# 	plt.imsave("{}".format(fname), image)
# 	i += 1
