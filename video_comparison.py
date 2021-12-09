import subprocess


def video_comparison_func(video1, video2):
    subprocess.call(['ffmpeg', '-i', video1, '-i', video2, '-filter_complex',
                     "hstack=inputs=2", 'output_ex2.webm'])


