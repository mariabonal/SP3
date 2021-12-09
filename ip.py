from live_streaming import stream


def ip_broadcasting(video):
    ip = input('Which ip do you want for broadcasting the BBB video? For example, udp://127.0.0.1:2222 \n')
    stream(video, ip)
