
# from PIL import Image
#
# img=Image.open("Ghost.jpg")
# new_size=(200,200)    #  can reduce but cannot increase the size of original image
# img.thumbnail(new_size)
# img.save('Happy_Diwali_1.jpg')
# print("Done")


# from PIL import Image
#
# img=Image.open("3_idiots.jpg")
# img.rotate(180).show()
#
# print("Done")

# from PIL import Image
#
# img=Image.open("3_idiots.jpg")
# img.rotate(90).save('temp.jpg')
# img1=Image.open("temp.jpg")
# img1.show()
# print("Done")



# from PIL import Image
#
# img=Image.open("Balls.jpg")
# area=(180,40,560,210)
# img.crop(area).show()
#
# print("Done")






#
# from PIL import Image,ImageDraw,ImageFont
#
# size=height,width=(300,300)
# img=Image.new("RGB",size,"pink")
# draw=ImageDraw.Draw(img)
# myfont=ImageFont.truetype("arial.ttf",30)
# points=70,120
# title="All the best"
# draw.text(points, title,"white",font=myfont)
# img.show()
# print("Done")



# from PIL import Image,ImageFilter
#
# img=Image.open("Balls.jpg")
# img.filter(ImageFilter.BLUR()).show()
# img.filter(ImageFilter.EDGE_ENHANCE()).show()
# img.filter(ImageFilter.EMBOSS()).show()
# img.filter(ImageFilter.CONTOUR()).show()




# Writing text on the image

from PIL import Image,ImageDraw,ImageFont

img=Image.open("Ishant.jpg")
draw=ImageDraw.Draw(img)
myfont=ImageFont.truetype("arial.ttf",20)
points=380,350
title="Arre , isse kya huva!"
draw.text(points, title,"red",font=myfont)
img.show()





