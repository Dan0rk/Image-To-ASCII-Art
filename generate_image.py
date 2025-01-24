import PIL.Image

i = input("Do you want to use space as a character for White? (y/n) (Default is n): \n")
if i == "y":
   space_flag = True
elif i == "n":
   space_flag = False
else:
    print("Invalid input \nNo is selected by default\n")
    space_flag = False

i = input("What width do you want? \nHigh = 1000 \nMedium = 500 \nLow = 100 \nEnter a number: ")
try:
   new_width = int(i)
except ValueError:
    print("Invalid input \nDefault value of 1000 is selected")
    new_width = 1000 

img_flag = True
path = input("Enter the path to the image field : \n")

path = path.replace('"', '')
 
try:
  img = PIL.Image.open(path)
  img_flag = True
except:
  print(path, "Unable to find image ")
 
width, height = img.size
aspect_ratio = height/width
# new_width = 1000
new_height = aspect_ratio * new_width * 0.55
img = img.resize((new_width, int(new_height)))
 
img = img.convert('L')
 
with open("utf-8_chars.txt", "r", encoding="utf-8") as f:
        chars = f.read().replace("\n", "").replace(" ", " ").strip()
 
pixels = img.getdata()
if space_flag:
    new_pixels = [chars[pixel // 25] if pixel < 255 else ' ' for pixel in pixels]
else:
    new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
 
with open("ascii_image.txt", "w", encoding="utf-8") as f:
 f.write(ascii_image)