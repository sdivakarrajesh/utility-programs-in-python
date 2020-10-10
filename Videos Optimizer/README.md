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

# License 

Copyright 2020 DIVAKAR RAJESH S

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

