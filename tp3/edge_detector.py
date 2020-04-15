import cv2
import numpy as np
import matplotlib.pyplot as plt
kernel = np.ones((5, 5), np.uint8)

def calculate_incoming_edge(previous_dilate, current_edges):
	previous_dilate =previous_dilate.clip(max=1)
	current_edges = current_edges.clip(max=1)
	num = np.sum(np.multiply(previous_dilate,current_edges))
	denum = np.sum(current_edges)
	return 1 - (num / denum)


def calculate_outcoming_edge(current_dilate, previous_edges):
	num = 0
	previous_edges = previous_edges.clip(max=1)
	current_dilate = current_dilate.clip(max=1)
	num = np.sum(np.multiply(previous_edges, current_dilate))
	denum = np.sum(previous_edges)
	return 1 - (num / denum)


def edge_detector(img):
	edges = cv2.Canny(img,100,200)
	cv2.subtract(0, img)
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
	in_edges = []
	out_edges = []
	cap = cv2.VideoCapture(file)
	indextrame = 1
	transition = ""
	trame_init = 0
	trame_final = 0
	compteur = 0
	while(True):
		ret, frame = cap.read()
		if ret:
			#TODO : frame processing algorithm
			cv2.imshow("frame", frame)
			edges = edge_detector(frame)
			dilate = dilate_image(edges)
			if indextrame > 1:
				incoming_edge = calculate_incoming_edge(previous_dilate, edges)
				outcoming_edge = calculate_outcoming_edge(dilate, previous_edges)
				in_edges.append(incoming_edge)
				out_edges.append(outcoming_edge)
				pic = max(incoming_edge, outcoming_edge)
				# if 0.2 >= pic:
				# 	if (transition== "" and incoming_edge > outcoming_edge):
				# 		transition ="fondu"
				# 		trame_init = indextrame
				# 	elif(transition=="fondu" and incoming_edge < outcoming_edge):
				# 		trame_final = indextrame
				#
				# elif 0.2 > pic and transition== "fondu":
				# 	transition = ""
				# 	trame_final = indextrame
				# 	grad.append([trame_init, trame_final])


				if pic >= 0.5 and transition == "":
					transition = "coupure"
					trame_init = indextrame

				elif pic < 0.5 and transition == "coupure":
					compteur += 1
					cut.append(trame_init)
					print(str(compteur) + ": " + str(trame_init))
					transition = ""





			previous_edges = edges
			previous_dilate = dilate
			indextrame += 1

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			break
	plt.plot(in_edges, label = "Arretes entrentes")
	plt.plot(out_edges, label = "Arretes sortantes")
	plt.xlabel("Frame number")
	plt.legend()
	plt.show()
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
