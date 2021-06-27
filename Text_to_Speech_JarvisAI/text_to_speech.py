import JarvisAI
# need to do pip install JarvisAI for using this.
obj = JarvisAI.JarvisAssistant(sync=False)

while True:
    response = obj.mic_input_ai(record_seconds=10, debug=False)
    print(response)