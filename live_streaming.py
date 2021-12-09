import subprocess


def stream(video, ip):
    subprocess.call(["ffmpeg", "-re", "-i", video, "-v", "0", "-c:v", "copy", "-f", "mpegts", ip])
