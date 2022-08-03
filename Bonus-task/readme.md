		Bonus Task 
		
		Captcha Reader
		
it was really fun to solve this problem

 step 1 > import all the required libraries
 
 		selenium 

		bs4
		
		PIL
		
		pytesseract
		
		os
		
step 2> get the url and open it with the help of driver

step 3> created a while loop

		due to low accuracy of image reader to extract text .
		i tried to implement a while loop which till it gets right character 				for captcha

step 4 > locate the image of captcha 

step 5 > download captcha image with the help of (urllib.request)

step 6 > extract text from the image with the help of (pytesseract)

step 7 > input captcha and click button with the help of (.click())

step 8 > delete captcha image that is stored in our directory (os.remove())

step 9 > check in while loop. if url is same as before than repeat 
	 same steps again and again till it gets right 	
