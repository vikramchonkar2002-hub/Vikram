"""Word-level transcription with faster-whisper. Usage: transcribe.py out.json in1.mp4 [in2.mp4 ...]"""
import json, sys
from faster_whisper import WhisperModel

out, files = sys.argv[1], sys.argv[2:]
model = WhisperModel("small.en", device="cpu", compute_type="int8")
result = {}
for f in files:
    segs, _ = model.transcribe(f, word_timestamps=True, vad_filter=False, beam_size=5,
                               initial_prompt="Um, uh, like, you know, so, I mean.")
    words = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3), "p": round(w.probability, 3)}
             for s in segs for w in s.words]
    result[f] = words
    print(f, "|", " ".join(w["w"] for w in words))
json.dump(result, open(out, "w"), indent=1)
