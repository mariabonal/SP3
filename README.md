# SP3 SCAV
#### Maria Bonal ✨

In this repository you can find the SP3 of the subject _Sistemes de codificació d'àudio i vídeo_. For running this seminar we need the `BBB.mp4` video.

We need to run the `main.py` script that will run the exercises of this lab. 
First, it will run the first exercise which will use the videos BBB already converted to:
- 720p
- 480p
- 360x240
- 160x120
and convert them into VP8, VP9, h265 and AV1. This task can be found inside the class FinalExercises(). 

Then, it will run the second exercise which will compare two codecs, the VP8 and the VP9. This exercise can be found in the script `video_comparison.py`.
The output will be saved as `output_ex2.webm`. 
When we compare these videos we can see that the vp9 video has better quality than the vp8, as we expected. 

The third exercise is about creating a live streaming of the BBB video and open the IP inside the VLC Media Player. This exercise can be found in the script `live_streaming.py`.

Finally, the last exercise asks us to create a a script that let you choose the IP to broadcast the BBB video. 
We ask the user which IP they want to use for broadcasting and then we call the function from exercise 3. This exercise can be found in the script `ip.py`.
