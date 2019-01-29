
try:
	f = open('testfile.txt')
	var = q
# catch the error and print
except FileNotFoundError as e:
	print(e)
# Run if the try doesn't run
else:
	print(f.read())
# Run in any case
finally:
	print('closing file...')
	f.close()
