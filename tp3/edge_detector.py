import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)


def calculate_incoming_edge(previous_dilate, current_edges):
	num = np.sum(previous_dilate * current_edges)
	denum = np.sum(current_edges)
	return 1 - (num / denum)


def calculate_outcoming_edge(current_dilate, previous_edges):
	num = np.sum(previous_edges * current_dilate)
	denum = np.sum(previous_edges)
	return 1 - (num / denum)


def edge_detector(img):
	edges = cv2.Canny(img,100,200)
	cv2.imshow('edges', edges)
	return edges

def dilate_image(img):
	dilate = cv2.dilate(img, kernel, iterations=1)
	cv2.imshow('dilate', dilate)
	return dilate

"""
This function should process the video file.
Input: 
- file: the path to the video
Output:
- cut: vector of frame indices where cuts are detected
- grad: vector of tuples (start, end) of frame indices where gradations are detected
"""
def process_video(file: str):
	cut=[]
	grad=[]
	cap = cv2.VideoCapture(file)
	indextrame = 0

	while(True):
		ret, frame = cap.read()
		if ret:
			#TODO : frame processing algorithm
			cv2.imshow("frame", frame)
			edges = edge_detector(frame)
			dilate = dilate_image(edges)
			# if(indextrame>0):
			# 	incoming_edge = calculate_incoming_edge(previous_dilate, edges)
			# 	outcoming_edge = calculate_outcoming_edge(dilate, previous_edges)

			previous_edges = edges
			previous_dilate = dilate
			indextrame += 1

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			break

	cap.release()
	cv2.destroyAllWindows()
	return cut, grad

"""
This function provides the ground truth for a given video file.
Input: 
- file: the path to the video
Output:
- cut: vector of frame indices where cuts happen
- grad: vector of tuples (start, end) of frame indices where gradations happen
"""
def read_groundtruth(file: str):
	cut=[]
	grad=[]
	f = open(file, "r")
	line = f.readline().split()
	while(line != []):
		if len(line)==1:
			cut.append(int(line[0]))
		elif len(line)==2:
			grad.append([int(line[0]), int(line[1])])
		line = f.readline().split()
	return cut, grad

cut, grad = process_video('anni005.mpg')
gt_cut, gt_grad = read_groundtruth('anni005.txt')

#TODO : results analysis