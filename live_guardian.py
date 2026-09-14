# Live Guardian - TikTok Reputation Protector
# Built by Sengezo from PE, SA
# Purpose: Detect when someone is shamed by name on LIVE

import re

# List of negative / defaming words - you can add more
BAD_WORDS = [
    "scammer", "thief", "ugly", "slut", "bitch", 
    "stupid", "fake", "fraud", "prostitute", "loser",
    "is a", "is an"  # catches "is a thief" pattern
]

# Fake list of private names for demo - in real app, this comes from face detection
PRIVATE_PEOPLE = ["Lutho", "Amahle", "Sipho", "Grade 10 girl"]

def check_live_transcript(text):
    text_lower = text.lower()
    
    # Check if a private person is mentioned
    person_found = None
    for person in PRIVATE_PEOPLE:
        if person.lower() in text_lower:
            person_found = person
            break
    
    # Check if bad word is also in same sentence
    bad_found = None
    for bad in BAD_WORDS:
        if bad in text_lower:
            bad_found = bad
            break
    
    # If BOTH happen = Reputation Attack
    if person_found and bad_found:
        print(f"\n🚨 WARNING DETECTED!")
        print(f"Transcript: {text}")
        print(f"-> Private person: {person_found}")
        print(f"-> Negative word: {bad_found}")
        print(f"-> ACTION: BEEP name, Show warning to host: 'You are discussing a private person'")
        print(f"-> BEEPED VERSION: {text.replace(person_found, 'BEEP')}")
        return True
    else:
        print(f"✅ Safe: {text}")
        return False

# --- DEMO SIMULATION OF A TIKTOK LIVE ---
print("=== Live Guardian Started - Listening to Live ===")

fake_live_talks = [
    "Hello guys welcome to my live",
    "Today I want to talk about my day at school",
    "That Lutho is a scammer he stole my money",  # <- Should trigger
    "Ah okay let's continue",
    "Amahle is ugly I don't like her",  # <- Should trigger
    "Thanks for gifts guys"
]

for talk in fake_live_talks:
    check_live_transcript(talk)

print("\n=== Live Ended - Report: 2 reputation attacks blocked ===")
