import os

f = os.listdir('train')

for i in f:
	if i[0] == 'c':
		os.rename('train/'+i, 'cat/'+i)
	else:
		os.rename('train/'+i, 'dog/'+i)
