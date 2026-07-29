import os
import sounddevice as sd
import soundfile as sf

from speech_to_text import speech_to_text
from llm import ask_llm
from text_to_speech import text_to_speech


SAMPLE_RATE = 16000
DURATION = 5
AUDIO_FILE = "input.wav"


def get_microphone():

    print("\n🔎 Searching for microphone...")

    devices = sd.query_devices()

    for index, device in enumerate(devices):

        if device["max_input_channels"] > 0:

            name = device["name"]

            # Avoid WDM-KS devices
            if (
                "MME" in name
                or "DirectSound" in name
                or "WASAPI" in name
            ):
                print(f"✅ Microphone selected: {name}")
                print(f"Device ID: {index}")

                return index


    print("❌ No compatible microphone found")
    return None



MIC_DEVICE = get_microphone()



def record_audio():

    print("\n🎤 Speak now for 5 seconds...")


    try:

        if MIC_DEVICE is None:
            print("❌ No microphone available")
            return False


        recording = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32",
            device=MIC_DEVICE
        )


        sd.wait()


        sf.write(
            AUDIO_FILE,
            recording,
            SAMPLE_RATE
        )


        if os.path.exists(AUDIO_FILE):

            print("✅ Audio saved successfully")
            return True


        else:

            print("❌ Audio file was not created")
            return False



    except Exception as e:

        print("❌ Audio recording error:")
        print(e)

        return False





def main():


    print("=" * 50)
    print("🎙️ Voice-to-Voice AI Assistant")
    print("=" * 50)



    while True:


        recorded = record_audio()


        if not recorded:
            continue



        print("\n📝 Converting speech to text...")



        try:


            user_text = speech_to_text(AUDIO_FILE)



            if not user_text or not user_text.strip():

                print("⚠️ No clear speech detected")
                continue



            print("\n👤 You:")
            print(user_text)



            if user_text.lower().strip() in [
                "exit",
                "quit",
                "stop"
            ]:

                print("👋 Assistant stopped")
                break




            print("\n🤖 Thinking...")


            answer = ask_llm(user_text)



            print("\n🤖 Assistant:")
            print(answer)



            print("\n🔊 Playing response...")


            text_to_speech(answer)



        except Exception as e:


            print("\n❌ Error:")
            print(e)





if __name__ == "__main__":

    main()
