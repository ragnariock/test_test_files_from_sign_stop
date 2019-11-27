import cv2
from random import randint
import xml.etree.cElementTree as ET
import numpy as np
import random

def image_genearte(ragne_images,range_sign):
	iteration = 1
	name_folder_images = 'images/'
	name_folder_sign = 'allroadsign/'
	normal_folder = 'data_image/'
	
	num_range = int(ragne_images / range_sign)
	second_iteration = 0 
	iter_sign = 1 

	for i in range(range_sign):
		print(i)
		for j in range(second_iteration,num_range):		
			img_size_annots_h = np.random.random_integers(100,200) 
			img_size_annots_w = np.random.random_integers(100,200)
			img_size =(800,800)
			img_size_annots = (img_size_annots_h,img_size_annots_w)
			
			image = cv2.imread(name_folder_images+str(iteration)+'.jpg')
			image_sign = cv2.imread(name_folder_sign+str(iter_sign)+'.jpg')

			new_image = cv2.resize(image,img_size)

			new_image_sign = cv2.resize(image_sign,img_size_annots)

			sign = new_image_sign
			image = new_image

			radnom_down  = np.random.random_integers(200,400) 
			random_raght = np.random.random_integers(200,400) 
			image[img_size_annots[0] + radnom_down:img_size_annots[0]+radnom_down+sign.shape[0], img_size_annots[1]+random_raght:img_size_annots[1]+random_raght+sign.shape[1]] = sign 
			cv2.imwrite(normal_folder+str(iteration)+'.jpg',image)
			
			img_width,img_height= img_size
			img_depth = 3

			rectangles = [
			img_size_annots[0] + radnom_down,
			img_size_annots[0] * 2,
			img_size_annots[0],
			img_size_annots[1] * 3
			]
			
			name =str(iteration)+'.jpg'
			img_filename = (name)

			name_folder = "images"
			path = "/home/ostap/Documents/LNU/kiberg/Vision/test/images/" +str(iteration)+ ".jpg"
			database  = "Unknown"
			segmented = 0
			name_obj = "stop"
			pose = "Unspecified"
			fruncated = 0
			difficult = 0
			xmin_add = np.random.random_integers(0,10)
			ymin_add = np.random.random_integers(0,10)
			xmax_add = np.random.random_integers(0,10)
			ymax_add = np.random.random_integers(0,10)
			xmin = img_size_annots[1] + random_raght + img_size_annots_h + xmin_add
			xmax = img_size_annots[1] + random_raght + xmax_add
			ymax = img_size_annots[0] + radnom_down + ymax_add
			ymin = img_size_annots[0] + radnom_down + img_size_annots_w + ymin_add
			print(xmin, "\t",ymin,"\t",xmax,"\t",ymax)
			print("==================================")
			with open("data_annots/"+str(iteration)+".xml","w+") as f :
				f.write("<annotation>")
				f.write("\n\t<folder>" + name_folder + "</folder>")
				f.write("\n\t<filename>" + str(iteration)+ ".jpg" + "</filename>")
				f.write("\n\t<path>" + path + "</path>")	
				f.write("\n\t<source>")	
				f.write("\n\t\t<database>" + database +"</database>")
				f.write("\n\t</source>")
				f.write("\n\t<size>")	
				f.write("\n\t\t<width>" + str(img_width) + "</width>")
				f.write("\n\t\t<height>" + str(img_height) + "</height>")
				f.write("\n\t\t<depth>" + str(img_depth) + "</depth>")
				f.write("\n\t</size>")
				f.write("\n\t<segmented>" + str(segmented) + "</segmented>")
				f.write("\n\t<object>")
				f.write("\n\t\t<name>" + name_obj + "</name>")	
				f.write("\n\t\t<pose>" + pose + "</pose>")
				f.write("\n\t\t<truncated>" + str(fruncated) + "</truncated>")
				f.write("\n\t\t<difficult>" + str(difficult) + "</difficult>")
				f.write("\n\t\t<bndbox>")
				f.write("\n\t\t\t<xmin>" + str(xmin) + "</xmin>")
				f.write("\n\t\t\t<ymin>" + str(ymin) + "</ymin>")
				f.write("\n\t\t\t<xmax>" + str(xmax) + "</xmax>")
				f.write("\n\t\t\t<ymax>" + str(ymax) + "</ymax>")
				f.write("\n\t\t</bndbox>")
				f.write("\n\t</object>")
				f.write("\n</annotation>") 
				f.close()
			iteration+=1
			num_range +=1	
			second_iteration +=1
			
		iter_sign +=1

image_genearte(2000,6)

#print(np.random.random_integers(0,10))



with open("1.xml","w") as f:
	f.write(r"101")
	f.write(r"101")
	f.write(r"101")
	f.write(r"101")

with open("2.xml","w") as f:
	f.write(str(np.random.random_integers(100,200)))
	f.write(str(np.random.random_integers(100,200)))
	f.write(str(np.random.random_integers(100,200)))
	f.write(str(np.random.random_integers(100,200)))
