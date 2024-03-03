# Stamp Boundary Segmentation


In this repository, the aim is to detect the edge of company stamps. This is a projection of an ellipse. 


The problem to solve is much easier because we need to detect color red in images and two parameters for the traditional image processing algorithm, instead of three for the Circular Hough Transform transform.


## Prerequisites
- Python 
- Opencv-python
- Opencv-contrib-python
- Numpy >= 1.14.3

## Quick Start

### Running
```bash
$ cd RDDN
$ python run_ellipse.py
```

### Demonstration

Only listed several examples, more results can be found in my [github]([https://github.com/KhoiTrant68/Stamp-Boundary-Segmentation]).


<table>
  	<tr>
		<th>Original</th>
		<th>Mask</th>	
	</tr>
  	<tr>
		<th><img src="./data/stamp/0.jpg"/></th>		
		<th><img src="./results/stamp/0.jpg"/></th>
	</tr>
 	<tr>
		<th><img src="./data/stamp_advance/1.jpg"/></th>		
		<th><img src="./results/stamp_advance/1.jpg"/></th>
	</tr>
<table>
 
 



