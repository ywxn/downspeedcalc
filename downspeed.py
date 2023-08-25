filesize = ''

characters = ['0','1','2','3','4','5','6','7','8','9','.']

file_size = str(input("Use G for gigabytes, M for megabytes, K for kilobytes\nInsert the size of the file you are downloading: "))

for num in file_size:
    if num in characters:
        filesize += num
        size = float(filesize)

if file_size[-1] in characters:
    print("Assuming file size in gigabytes...")
    size *= 1024
if file_size[-1] == 'G':
    size *= 1024
if file_size[-1] == 'K':
    size /= 1024        

speed = float(input('Insert your download speed in mb/s: '))
speed *= 60

print("Your download should complete in " + str(int(size//speed)) + " minutes")
