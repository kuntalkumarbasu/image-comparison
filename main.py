#!/usr/bin/env python
from colorama import init,Fore,Style
from skimage.metrics import structural_similarity
import cv2,csv,time,sys,pathlib


def get_inputFile():
    try:
        input_csv=str(sys.argv[1])
    except IndexError as e:
        print(f'{Fore.RED} No explicit CSV file given')
        print(f' Assuming image-comparison.csv is present in current path{Style.RESET_ALL}')
        input_csv = 'image-comparison.csv'
        #input_csv = 'sample.csv'
    return input_csv


def compare_images(image1, image2):
    start_time = time.time()
    similar = 1- structural_similarity(image1, image2) ## Structural Similiarity Index has 1 signifying identical images, not 0
    elapsed = time.time() - start_time

    return round(similar,3), round(elapsed,3)
    

## appending to the results.csv file with the paths, similiarity index, and time elapsed for the comparison
def output_file(pathA, pathB, similar, elapsed):
    with open(str(pathlib.Path(__file__).parent.absolute()) + '/results.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([pathA, pathB, similar, elapsed])


## Necessary in order for SSIM to function. Both images must have the same resolution
def scale_images(image1, image2, width=640, height=480):
    
    ## Setting constant dimensions, with arbitrary default values of 640x480
    dim = (width, height)
    
    image1 = cv2.resize(image1, dim)
    image2 = cv2.resize(image2, dim)

    return image1, image2


## Full processing here

def process_input_csv(csvfile):
## creating new file and setting the headers
    with open(str(pathlib.Path(__file__).parent.absolute()) + '/results.csv', 'w') as newcsv:
        writer = csv.writer(newcsv, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['image1', 'image2', 'similar', 'elapsed'])

## skipping the first line because they are headers
    firstLine = True
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if firstLine:
            firstLine = False
            continue

        path1, path2 = row[0], row[1]

        image1, image2 = scale_images(cv2.imread(row[0]), cv2.imread(row[1]))
        
        resized_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        resized_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        similar, elapsed = compare_images(resized_image1, resized_image2)
        
        output_file(path1, path2, similar, elapsed)

    print(f'{Fore.GREEN} Please check results.csv in the current path for results {Style.RESET_ALL}')

def main():

## read in csv containing all images that are being compared
    input_csv = get_inputFile()
    print(input_csv)
    with open(input_csv) as csvfile:
        process_input_csv(csvfile)

if __name__ == '__main__':
    main()



