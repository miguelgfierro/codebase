# Cut audio
ffmpeg -i input.mp3 -vn -acodec copy -ss 00:00:10 -to 00:00:30 output.mp3
