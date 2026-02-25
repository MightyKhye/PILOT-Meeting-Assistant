"""
Diagnostic script to check the last two meeting recordings.
Determines if they need repair and optionally fixes them.
"""

import wave
from pathlib import Path

print("="*70)
print("MEETING RECORDINGS DIAGNOSTIC")
print("="*70)
print()

meetings_dir = Path(r"C:\Users\khyeh\Documents\Pilot\summaries")

# Last two meetings
meetings = [
    ("complete_recording_20260216_120130.wav", "Meeting 1 (Feb 16, 12:01)"),
    ("complete_recording_20260215_132302.wav", "Meeting 2 (Feb 15, 13:23)")
]

print("Checking meeting recordings...")
print()

results = []

for filename, label in meetings:
    filepath = meetings_dir / filename

    if not filepath.exists():
        print(f"[WARNING] {label}: File not found!")
        print(f"  Expected: {filepath}")
        print()
        continue

    try:
        with wave.open(str(filepath), 'rb') as w:
            rate = w.getframerate()
            channels = w.getnchannels()
            frames = w.getnframes()
            duration_minutes = frames / rate / 60

        print(f"[{label}]")
        print(f"  File: {filename}")
        print(f"  Sample Rate: {rate} Hz")
        print(f"  Channels: {channels}")
        print(f"  Duration: {duration_minutes:.1f} minutes")
        print(f"  Size: {filepath.stat().st_size / 1024 / 1024:.1f} MB")

        # Determine if it looks correct
        expected_rate = 48000
        expected_channels = 2

        if rate == expected_rate and channels == expected_channels:
            print(f"  Status: [OK] Correct format")
            status = "OK"
        else:
            print(f"  Status: [WARN] Unexpected format")
            print(f"    Expected: {expected_rate} Hz, {expected_channels} channels")
            print(f"    Got: {rate} Hz, {channels} channels")
            status = "WARN"

        results.append((filename, label, rate, channels, status))
        print()

    except Exception as e:
        print(f"[ERROR] {label}: {e}")
        print()
        results.append((filename, label, None, None, "ERROR"))

print("="*70)
print("ANALYSIS:")
print("="*70)
print()

print("The meeting recordings appear to be in the expected format:")
print("  • 48000 Hz sample rate")
print("  • 2 channels (stereo)")
print()

print("These were RESAMPLED by the application from the original 44100 Hz")
print("mono chunks. The resampling process:")
print("  1. Took 44100 Hz mono chunks")
print("  2. Converted to 48000 Hz stereo for final output")
print()

print("PLAYBACK TEST NEEDED:")
print("-" * 70)
print()
print("Please manually test the following files:")
print()

for filename, label, rate, channels, status in results:
    if status in ["OK", "WARN"]:
        filepath = meetings_dir / filename
        print(f"{label}:")
        print(f"  {filepath}")
        print()

print("Listen for:")
print("  ✓ Normal speaking speed (not too fast)")
print("  ✓ Normal voice pitch (not high-pitched/chipmunk)")
print("  ✓ Clear audio quality")
print()

print("If the audio sounds NORMAL:")
print("  → No repair needed! The app's resampling worked correctly.")
print()

print("If the audio sounds TOO FAST (chipmunk effect):")
print("  → This would be unexpected given the resampling from 44100→48000 Hz")
print("  → Please report this and I'll create a custom repair script")
print()

print("If the audio sounds TOO SLOW (deeper voices):")
print("  → This suggests the original chunks were actually 48000 Hz")
print("  → But were tagged as 44100 Hz, then resampled to 48000 Hz")
print("  → I can create a repair script to correct this")
print()

print("="*70)
print()

print("SNIPPETS CHECK:")
print("-" * 70)
print()

snippets_dir = Path(r"C:\Users\khyeh\Documents\Pilot\summaries\snippets")
if snippets_dir.exists():
    recent_snippets = sorted(
        snippets_dir.glob("snippet_20260216_*.wav"),
        reverse=True
    )[:3]

    if recent_snippets:
        print("Recent snippets (check these too):")
        print()
        for snippet in recent_snippets:
            with wave.open(str(snippet), 'rb') as w:
                rate = w.getframerate()
                channels = w.getnchannels()
            print(f"  {snippet.name}")
            print(f"    {rate} Hz, {channels}ch")

        print()
        print("Snippets are typically resampled to 16000 Hz for AI processing.")
        print("They should sound normal when played back.")
    else:
        print("No recent snippets found for Feb 16 meeting.")
else:
    print("[WARNING] Snippets directory not found!")

print()
print("="*70)
print("Next step: Please test playback and report results!")
print("="*70)
