# NEXPLANON REMS Meeting Listener - Quick Start Guide

## 🚀 Features

### Core Features
- **Real-time Audio Capture**: Records ambient audio from your microphone
- **Automatic Transcription**: Uses AssemblyAI to transcribe speech
- **AI Analysis**: Claude identifies action items, decisions, and key points
- **Windows Notifications**: Get instant alerts for important items
- **Confidence Tracking**: Shows transcript quality and flags unclear sections

### New Enhanced Features
- **Persistent Memory**: Remembers ALL previous meetings forever
- **Contextual Learning**: Builds on past meetings for better understanding
- **Live Query**: Ask questions about REMS or past meetings anytime
- **Document Upload**: Add REMS supporting documents to knowledge base
- **Desktop Shortcut**: One-click access from your desktop

## 🖥️ Setup Desktop Shortcut

1. Double-click `create_desktop_shortcut.bat`
2. A shortcut will appear on your desktop
3. Click the shortcut anytime to launch the Meeting Listener

## 📖 How to Use

### Basic Meeting Recording

1. **Launch the app** (click desktop shortcut or run `launch_meeting_listener.bat`)
2. **Choose option 1** to start recording
3. **Have your meeting** - the app will capture audio from your room
4. **Choose option 2** to stop recording when done
5. **Find your summary** - Check your Downloads folder for the meeting summary

### Query Past Meetings

1. **Choose option 4** - Ask Question
2. **Type your question**, for example:
   - "What training requirements were discussed in past meetings?"
   - "What are Sarah's pending action items?"
   - "What decisions were made about rural site training?"
3. **Get instant answers** - Claude will search all meetings and documents

### Upload REMS Documents

1. **Choose option 5** - Upload REMS Document
2. **Enter the full path** to your document
   - Example: `C:\Users\khyeh\Documents\NEXPLANON_REMS_Guide.pdf`
3. **Document is saved** - Will be used for future queries

### View History

- **Option 6**: See all uploaded documents
- **Option 7**: View summaries of past meetings

## 📁 Output Files

All files are saved in the `assistant` folder:

- **meetings/**: Meeting summaries (.md files)
- **meetings/persistent_memory.json**: All historical data
- **recordings/**: Raw audio chunks
- **Downloads/**: Copies of summaries for easy access

## 🎯 Understanding Output

### Meeting Summary Format

```
NEXPLANON REMS MEETING SUMMARY
Date: 2026-02-05 17:30
Transcription Quality: 88%

ACTION ITEMS
- [ ] Sarah: Update REMS training docs (Due: Friday) - Confidence: high

DECISIONS
- Approved virtual training for rural sites (Confidence: high)

ITEMS REQUIRING CLARIFICATION
- Specific requirements for rural provider authorization

MEETING SYNOPSIS
[Professional summary of key discussion points]

PARTICIPANTS
[List of identified participants]

COMPLETE TRANSCRIPT
[Full transcript with confidence markers]
[Low confidence sections marked like this] (confidence: 45% - unclear)
```

### Confidence Markers in Transcript

- **No marker**: High confidence (70%+)
- **[text] (confidence: 65%)**: Moderate confidence
- **[text] (confidence: 45% - unclear)**: Low confidence, may be inaccurate

## 💡 Tips

1. **Speak clearly** near the microphone for best transcription
2. **Let it run** - The app processes in 30-second chunks automatically
3. **Ask questions** - Use the query feature to find information from past meetings
4. **Upload documents** - Add REMS guides for better AI responses
5. **Check quality** - If overall quality is below 70%, audio may be too quiet

## 🔧 Troubleshooting

### No audio captured
- Check that microphone device 12 (AMD Microphone Array) is working
- Speak louder or move closer to microphone
- Verify Windows microphone permissions

### Low transcription quality
- Reduce background noise
- Move closer to speakers/microphone
- Check that audio is audible when played back

### Query not finding information
- Make sure recording was completed (option 2: Stop Recording)
- Upload relevant REMS documents for better context
- Try rephrasing your question

### Desktop shortcut not working
- Right-click shortcut → Properties
- Verify "Start in" path points to assistant folder
- Re-run `create_desktop_shortcut.bat`

## 📞 Support

For issues, check:
- `logs/` folder for error messages
- Verify API keys in `.env` file
- Ensure `venv` is properly activated

---

**Version**: Enhanced with Memory & Query Features
**Last Updated**: 2026-02-05
