# Videos Optimizer

A utility script that goes through all the folders in current working directory looking for video files and optimizes them, saving them to a "optimized" folder 

# Instructions

## Pre-requisites

- Python version > 3.5
- Installed FFmpeg or added the FFmpeg binaries to your PATH

## Running the script

- Place the script in the folder containing all the folders containing the videos
- Run the script by `python3 ./optimizer.py`
- it will keep track of all the tasks in a queue and write them to a file called '.optimize_queue.json' in the folder where its run, so you can always stop the program and continue where you left off
- The optimized videos will be in H.265 codec inside the 'optimized' folder

 

