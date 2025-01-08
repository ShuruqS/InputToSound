import keyboard
from playsound import playsound

emoji_to_sound = {
    "input": "/Users/.....m4a" # change to what should input be, and the path to what should play in return 
}

def play_sound_for_emoji(emoji):
    if emoji in emoji_to_sound:
        sound_file = emoji_to_sound[emoji]
        print(f"Playing sound for emoji: {emoji}")
        playsound(sound_file)
    else:
        print("No sound assigned for this emoji.")

print("Enter an emoji to play its sound (or type 'exit' to quit):")
while True:
    user_input = input("Emoji: ")
    if user_input.lower() == "exit":
        print("Exiting the program.")
        break
    play_sound_for_emoji(user_input)


