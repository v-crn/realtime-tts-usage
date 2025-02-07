import time

if __name__ == "__main__":
    from RealtimeTTS import KokoroEngine, TextToAudioStream

    # Example text generators
    def dummy_generator():
        yield "This is the first voice model speaking. "
        # yield "The elegance of the style and its flow is simply captivating. "
        # yield "We'll soon switch to another voice model. "

    def dummy_generator_2():
        yield "And here we are! "
        # yield "You're now listening to the second voice model, with a different style and tone. "
        # yield "It's fascinating how Kokoro can adapt to different voices. "

    def dummy_generator_3():
        yield "お待ちしておりました。お会いできて光栄です! "
        yield "こちらは日本語のボイスモデルです。 "
        yield "いかがでしょうか？ 問題ないですかね？ "

    # Initialize the KokoroEngine with a default language code and voice
    engine = KokoroEngine(
        # Kokoro language codes:
        # a  => American English
        # b  => British English
        # j  => Japanese
        # z  => Mandarin Chinese
        # e  => Spanish
        # f  => French
        # h  => Hindi
        # i  => Italian
        # p  => Brazilian Portuguese
        default_lang_code="a",  # choose any one of the above
        default_voice="af_bella",
        debug=True,
    )

    jp_voices = [
        "jf_alpha",
        "jf_gongitsune",
        "jf_nezumi",
        "jf_tebukuro",
        "jm_kumo",
    ]
    jp_engine = KokoroEngine(
        default_lang_code="j",
        default_voice=jp_voices[0],
        debug=True,
    )

    voices = engine.get_voices()
    print(f"Available voices: {voices}")

    # Create a TextToAudioStream object
    stream = TextToAudioStream(engine)
    jp_stream = TextToAudioStream(jp_engine)

    # Play with the first voice
    print("Playing with the first voice...")
    stream.feed(dummy_generator())
    stream.play(log_synthesized_text=True)

    # Switch to a different voice
    engine.set_voice("af_nicole")
    # Some other voice options you might try:
    # "af_nicole", "af_sarah", "am_adam", "am_michael", "bf_emma", "bf_isabella"

    # Play with the second voice
    print("Now switching to a different voice...")
    stream.feed(dummy_generator_2())
    stream.play(log_synthesized_text=True)

    time.sleep(2)

    for voice in jp_voices:
        jp_engine.set_voice(voice)
        jp_stream.feed(dummy_generator_3())
        jp_stream.play(log_synthesized_text=True)
        time.sleep(1.5)

    # Shutdown the engine after use
    engine.shutdown()
    jp_engine.shutdown()
