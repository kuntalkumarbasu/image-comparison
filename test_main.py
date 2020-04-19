from colorama import init,Fore,Style
from main import compare_images,output_file,scale_images,process_input_csv
import sys,pathlib
import cv2,csv,time,sys

#write input csv file
def create_input_file(file1, file2):
	input_csv = str(pathlib.Path(__file__).parent.absolute()) + '/image-comparison.csv'
	csvfile = open(input_csv, "w")
	csvfile.truncate()
	csvfile.close()
	with open(input_csv, 'a') as csvfile:
		csvfile.truncate()
		writer = csv.writer(csvfile, delimiter=',',
							quotechar='|', quoting=csv.QUOTE_MINIMAL)
		pathA = str(pathlib.Path(__file__).parent.absolute()) + '/images/' + file1
		pathB = str(pathlib.Path(__file__).parent.absolute()) + '/images/' + file2
		writer.writerow(['image1', 'image2'])
		writer.writerow([pathA, pathB])
		return input_csv

# Comapre expected and actual csvs
def compare_csv(file1,file2):
	# Only comparing the "similar" column as other value will be different based on the environment
	interesting_cols = [2] 

	with open(file1, 'r') as file1,\
	     open(file2, 'r') as file2:

	    reader1, reader2 = csv.reader(file1), csv.reader(file2)

	    for line1, line2 in zip(reader1, reader2):
	        equal = all(x == y
	            for n, (x, y) in enumerate(zip(line1, line2))
	            if n in interesting_cols
	        )
	        return(equal)


# test different size image
def test_diff_size_images():
	input_csv = create_input_file('original-resized-cucumbers.png', 'original-cucumbers.png')
	with open(input_csv) as csvfile:
		process_input_csv(csvfile)
		pathA = str(pathlib.Path(__file__).parent.absolute()) + '/expected_results/' + 'expected_results_diff_size.csv'
		pathB = str(pathlib.Path(__file__).parent.absolute()) + '/results.csv'
		result = compare_csv(pathA,pathB)
	if result:
		 print(f'{Fore.GREEN} test different size image is Passed{Style.RESET_ALL}')
	else:
		 print(f'{Fore.RED} test different size image is FAILED{Style.RESET_ALL}')


# test same image with different extension
def test_diff_ext_images():
	input_csv = create_input_file('original-dogs.jpg', 'original-dogs.png')
	with open(input_csv) as csvfile:
		process_input_csv(csvfile)
		pathA = str(pathlib.Path(__file__).parent.absolute()) + '/expected_results/' + 'expected_results_diff_extn.csv'
		pathB = str(pathlib.Path(__file__).parent.absolute()) + '/results.csv'
		result = compare_csv(pathA,pathB)
	if result:
		 print(f'{Fore.GREEN} test same image with different extension is Passed{Style.RESET_ALL}')
	else:
		 print(f'{Fore.RED} test same image with different extension is FAILED{Style.RESET_ALL}')

# test same image 
def test_same_images():
	input_csv = create_input_file('original-cucumbers.png', 'original-cucumbers.png')
	with open(input_csv) as csvfile:
		process_input_csv(csvfile)
		pathA = str(pathlib.Path(__file__).parent.absolute()) + '/expected_results/' + 'expected_results_same_image.csv'
		pathB = str(pathlib.Path(__file__).parent.absolute()) + '/results.csv'
		result = compare_csv(pathA,pathB)
	if result:
		 print(f'{Fore.GREEN} test same image is Passed{Style.RESET_ALL}')
	else:
		 print(f'{Fore.RED} test same image is FAILED{Style.RESET_ALL}')


def main():
	test_diff_size_images()
	test_diff_ext_images()
	test_same_images()

if __name__ == '__main__':
	main()



# test visibly same image with different extension
# test output format