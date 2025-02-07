from RealtimeTTS import GTTSEngine, TextToAudioStream

engine = GTTSEngine()
stream = TextToAudioStream(engine)
stream.feed("Hello, world!")
stream.feed("こんにちは！今日はどんな一日にしたいですか？")
stream.play_async()
