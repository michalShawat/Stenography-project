# this file is to create train_x, train_y sets with different encoding techniques

import extractCifar10
import encoder4
import encoder8
import createSet

# first you need to create empty batchX, encodedX dir.

extractCifar10.extract_batch("data_batch_1", "./batch1/") #RUN ONLY ONCE
extractCifar10.extract_batch("data_batch_2", "./batch2/") #RUN ONLY ONCE
# now batch1, batch2 dir. full

encoder4.encode4()
encoder8.encode8()
# now encoded1, encoded2 dir. full

batch_size = 10000
createSet.create_train_y(batch_size)
# now train_y was created

# create a set of the unencoded images
train_x = createSet.batch1_in_train_x(batch_size)

# now we add the encoded images, and create a set for each encoding technique
train1_x = list(train_x)
createSet.batch2_in_train_x(train1_x, batch_size, "1")
# now train1_x was created

train2_x = list(train_x)
createSet.batch2_in_train_x(train2_x, batch_size, "2")
# now train2_x was created

train3_x = list(train_x)
createSet.batch2_in_train_x(train3_x, batch_size, "3")
# now train4_x was created

train4_x = list(train_x)
createSet.batch2_in_train_x(train4_x, batch_size, "4")
# now train4_x was created

train8_x = list(train_x)
createSet.batch2_in_train_x(train8_x, batch_size, "8")
# now train8_x was created

print("done!")