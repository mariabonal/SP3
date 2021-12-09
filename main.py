import subprocess
from video_comparison import video_comparison_func
from live_streaming import stream
from ip import ip_broadcasting


def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string


class FinalExercises:
    def exercise_1(self, videos):
        for vid in videos:
            v_name = remove_suffix(str(vid), '.mp4')
            # VP8
            subprocess.call(['ffmpeg', '-i', vid, '-c:v', 'libvpx', '-b:v', '1M', '-c:a', 'libvorbis',
                             'vp8_' + v_name + '.webm'])
            # VP9
            subprocess.call(['ffmpeg', '-i', vid, '-c:v', 'libvpx-vp9', '-b:v', '2M', 'vp9_' + v_name + '.webm'])
            # h265
            subprocess.call(['ffmpeg', '-i', vid, '-c:v', 'libx265', '-crf', '26', '-preset', 'fast', '-c:a', 'aac',
                            '-b:a', '128k', 'h265_' + v_name + '.mp4'])
            # AV1
            subprocess.call(["ffmpeg", "-i", vid, "-c:v", "libaom-av1", "-cpu-used", "3", "-crf", "40", "-preset",
                             "medium", "-c:a", "copy",  'av1_' + v_name + '.mkv'])


final_exercises = FinalExercises()
v = ['BBB_160x120.mp4', 'BBB_360x240.mp4', 'BBB_480p.mp4', 'BBB_720p.mp4']

# EXERCISE 1
final_exercises.exercise_1(v)

# EXERCISE 2
video1 = 'vp8_BBB_360x240.webm'
video2 = 'vp9_BBB_360x240.webm'
video_comparison_func(video1, video2)

# EXERCISE 3
BBB_video = 'BBB.mp4'
ip = 'udp://127.0.0.1:2222'
stream(BBB_video, ip)

# EXERCISE 4
ip_broadcasting(BBB_video)
