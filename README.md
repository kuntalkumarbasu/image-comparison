# Image Comparison

## The Problem
We want to figure out how to compare two different images and measure their similarity.

### The Business Problem
Instead of having Bjorn manually open up two pairs of images and give a "Bjorn Score" for their similarities, we want to automate this process by iterating through an entire list of images pairs and calculating a score. This will be outputted into a results file so it will be nicely aggregated.

## The Solution
In a nutshell, this python script reads-in a csv file that contains (absolute) paths to images that are to be compared. Once the pair of images are known, it calculates the Structural Similarity Index, which is a method of evaluating the pixels in given windows of the image.
Information regarding the algorithm can be found here: https://en.wikipedia.org/wiki/Structural_similarity

## Design 

### Comparison Libraries
First looked into a few python libraries that handled image comparison. There were two methods that stood out: MSE, SSIM.

#### Mean Squared Error (MSE)
MSE performs its calculation by comparing each pixel, thus measuring absolute errors.

We then take the difference between the images by subtracting the pixel intensities. Next up, we square these difference (hence mean squared error, and finally sum them up.
In order to calculate the mean, all we are doing is dividing our sum of squares by the total number of pixels in the image.

![alt text](https://www.pyimagesearch.com/wp-content/uploads/2014/06/compare_mse.png)

#### Structural Similarity Index (SSIM)

SSIM is a method for predicting perceived quality of digital images, videos, etc. It was designed to improve traditional methods, such as MSE.
"SSIM is a perception-based model that considers image degradation as perceived change in structural information", also taking considerations to both luminance masking and contrast masking terms.

More information can be found on the wiki: https://en.wikipedia.org/wiki/Structural_similarity

##### The SSIM index is calculated on various windows of an image. The measure between two windows x and y of common size N×N is:


![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/63349f3ee17e396915f6c25221ae488c3bb54b66)

__where:__

<img src="http://www.sciweavers.org/tex2img.php?eq=%20c_%7B1%7D%20%3D%20%28k_%7B1%7DL%29%5E2&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" c_{1} = (k_{1}L)^2" width="94" height="21" />
<img src="http://www.sciweavers.org/tex2img.php?eq=%20c_%7B2%7D%20%3D%20%28k_%7B2%7DL%29%5E2&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" c_{2} = (k_{2}L)^2" width="94" height="21" />

L is the dynamic range of the pixels



__and__
<img src="http://www.sciweavers.org/tex2img.php?eq=%20k_%7B1%7D%20%3D%200.01%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" k_{1} = 0.01" width="82" height="18" />
<img src="http://www.sciweavers.org/tex2img.php?eq=%20k_%7B2%7D%20%3D%200.03%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" k_{2} = 0.03" width="82" height="18" />
__by default__


 ##### Since SSIM is undisputed to be an improved method of MSE, SSIM was chosen over MSE.
 
 Once the method was chosen, I then had to break down the rest of the script.
 
 ### Parsing an inputted CSV file
 
 Using the built-in __csv__ libraries, reading in CSV files were straightforward. 
 
 ### Using the Image Comparison library
 
 Each time a row from the csv file is read, it passes the two images into the function and does its magic.
 However, because SSIM requires the images to be of the same dimension, there is extra work prior to the calculation where the images are resized to a default value of 640x480 unless specified.
 Differing file types (tested with .jpg and .png) can be compared.
 
 ### Outputting Results into new CSV
 
 As each pair of images are compared, the similarity results and the elapsed time of the comparison are stored and outputted into a new csv file, in the required format from the assignment.
 
 The new csv file will have headers: image1, image2, similar, elapsed
 
 Once all the images are compared, the csv file should have the same amount of rows as the original csv file with the list of images to compare.
 
 ### Testing
 PNG and JPEG file types were tested. Comparison between the differing file types work as intended. 
 File types of different sizes are resized to the intended dimensions and can be properly compared.
 Output CSV file was checked to ensure it matches the order of images being compared from the original CSV file.

 Automated test cases has been written and it covers the following scenario,
 	1) different size image
 	2) different extension image
 	3) same image

 The expected_results folder has the expected resultset for each scenario. In the test cases we only compared the `similar` column


## Assumptions
1. Valid CSV file
* The headers, rows, and columns are valid
* The order of the columns are: image1, image2
* The paths of the images lead to an existing image

2. Python is already installed (I'm using version 3.7 in mac 3.6.8 in windows)
* ```pip``` is already installed

## SETUP 

### For MAC and Linux environments

#### Libraries Required 

##### cv2 version : 4.2.0.34 (for windows 3.3.0.9 )

``` pip3 install opencv-python ``` 

``` pip install opencv-python=3.3.0.9 ``` ( for windows)

##### scikit.image Version : 0.16.2

``` pip3 install scikit-image ```

##### colorama Version: 0.4.3

``` pip3 install colorama ```

##### pathlib Version: 1.0.1

```pip3 install pathlib ```

### For Windows environments

1. Setup Python in Windows
2. Setting up the code GIT BASH in Windows

#### 1. Setup Python in Windows

* go to [Python download page](https://www.python.org/downloads/)
* Select version 3.6.8 <<https://www.python.org/downloads/release/python-368/>>
* Download and Install

#### 2. Setting up the code GIT BASH in Windows
##### 2.1 Setting Up GIT BASH

* Download git from the link https://git-scm.com/download/win
* Install The downloaded installer

##### 2.2 Setup and run this image comparison in windows via GIT BASH

* `git colne git@github.com:kuntalkumarbasu/image-comparison.git`
*  setup the required libraries

 ## Libraries Required 

``` pip install opencv-python==3.3.0.9 ``` ( for windows)

``` pip install scikit-image ```

``` pip install colorama ```

``` pip install pathlib ```

 
 ## How to Use

 1. In winodws we used git bash client in linux or mac environment any client will work
 2. Import all the necessary libraries.
 3. Pull the code use ```git clone git@github.com:kuntalkumarbasu/image-comparison.git```
 you must make sure the `image-comparison.csv` file is in the same level as the `main.py` file. Or you can provide an absolute or relative filepath with a file name

 
 To run the script, 
 type: `python3 main.py` in the command line (if `image-comparison.csv` is available in same level as the `main.py` file ).
 type: `python3 main.py <absolute/relative file for the input csv>` in the command line


 To run the test, 
 type: `python3 test_main.py` in the command line 

 Note: I have added a sample csv which is compatible with the images in the image folder. if we run the below command from the base directory of this project, the code will run and generate result.

 `python3 main.py sample.csv`


 
 #### Note: Sample images
 I've included some sample images (original, contrasted, "photoshopped") in case you needed some quick "similar" photos to test with. Apologies for no sample csv file.
 
 ## Maintaining
 If this project is being passed onto someone else, I will tell that person to read this README to make sure they are following the steps. Unless there needs more features/capabilities, there should be no reason to modify the code.
 
 If all the modules have been installed/imported, yet errors regarding the modules are occuring, double check the versions of the libraries match the ones of the README. It is possible differing library versions can interfere with the functionality. Uninstall and reinstall the proper version of the libraries, or update them to the proper version if they are outdated.
 

 The base of this project is inspired from "https://github.com/denzelkwan/image-comparison". I already opened an PR to the orginal project with all my modifictaions and improvements
 
 
