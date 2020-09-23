from pydub import AudioSegment

podcast = AudioSegment.from_mp3("./podcasts/eine.mp3")
ad = AudioSegment.from_mp3("./ads/fanfare.mp3")

# 8秒の位置に音源を差し込む
ad_position = 8 * 1000
left = podcast[:ad_position]
right = podcast[ad_position:]

out = left + ad + right

out.export("out/inserted.mp3", format="mp3")
