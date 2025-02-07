import torch.multiprocessing as mp
from RealtimeTTS import CoquiEngine, TextToAudioStream

if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)

    def dummy_generator():
        yield " Hey guys! These here are realtime spoken sentences based on local text synthesis. "
        yield " With a local, neuronal, cloned voice. So every spoken sentence sounds unique."
        # yield "こんにちは！はじめまして。こちらは日本語のTTS音声のテストです。ちょっとお時間よろしいですか？"

    # for normal use with minimal logging:
    engine = CoquiEngine(
        # voices_path="data/voices",
        voice="data/voices/coqui_Uta Obando.wav",
        language="en",
        # language="ja",
        speed=1.0,
    )

    # test with extended logging:
    # import logging
    # logging.basicConfig(level=logging.INFO)
    # engine = CoquiEngine(level=logging.INFO)

    stream = TextToAudioStream(engine)

    print("Starting to play stream")
    stream.feed(dummy_generator()).play(log_synthesized_text=True)

    print("Playout finished")

    engine.shutdown()
