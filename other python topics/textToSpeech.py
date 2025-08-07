import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")

names=["Alice","Bob","Aditya","Mayur"]

for name in names:
    speaker.Speak(f"Shoutout to {name}")