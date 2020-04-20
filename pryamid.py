blocks = int(input("Enter the number of blocks: "))
i=0
height=0
while blocks > 0:
    i=i+1
    blocks = blocks -i
    height=height+1
height-=1
#
# Write your code here.
#	

print("The height of the pyramid:", height)