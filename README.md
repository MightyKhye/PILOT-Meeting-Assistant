# Meeting Listener 🎤

An intelligent Windows application that captures system audio from Zoom/Teams meetings, transcribes in real-time using OpenAI's Whisper API, and uses Claude AI to identify action items and decisions with instant toast notifications.

## Features

- **🎧 System Audio Capture**: Captures audio from Zoom, Teams, or any meeting app using Windows WASAPI loopback
- **✍️ Real-time Transcription**: Transcribes audio chunks using AssemblyAI API
- **🤖 AI-Powered Analysis**: Claude AI extracts action items, decisions, and key points
- **📬 Toast Notifications**: Instant Windows notifications for important items
- **📊 Meeting Summaries**: Automatic summary generation at meeting end
- **🖥️ System Tray Interface**: Minimal UI with start/stop controls

## Architecture

```
┌─────────────────┐
│  System Audio   │
│   (Loopback)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌──────────────────┐
│ Audio Capture   │────▶│  AssemblyAI API  │
│  (30s chunks)   │     │  (Transcription) │
└─────────────────┘     └────────┬─────────┘
                                 │
                                 ▼
                        ┌──────────────────┐
                        │   Claude API     │
                        │   (Analysis)     │
                        └────────┬─────────┘
                                 │
                                 ▼
                        ┌──────────────────┐
                        │  Notifications   │
                        │    & Summary     │
                        └──────────────────┘
```

## Prerequisites

- **Windows 10/11** (required for WASAPI loopback and toast notifications)
- **Python 3.10+**
- **AssemblyAI API Key** (for transcription)
- **Anthropic API Key** (for Claude analysis)

## Installation

### 1. Clone or Download

```bash
cd C:\Users\khyeh\assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Copy the example environment file:

```bash
copy .env.example .env
```

Edit `.env` and add your API keys:

```env
ASSEMBLYAI_API_KEY=your-assemblyai-key-here
ANTHROPIC_API_KEY=sk-ant-...
```

**Get API Keys:**
- AssemblyAI: https://www.assemblyai.com/ (5 hours/month free)
- Anthropic: https://console.anthropic.com/settings/keys

### 5. Configure Windows Audio (Important!)

For loopback audio capture to work, you need to enable "Stereo Mix" or similar:

**Option A: Enable Stereo Mix (if available)**
1. Right-click the volume icon in system tray → "Open Sound settings"
2. Click "Sound Control Panel" or "More sound settings"
3. Go to "Recording" tab
4. Right-click in empty space → "Show Disabled Devices"
5. Enable "Stereo Mix" or "What U Hear"

**Option B: Use VoiceMeeter (recommended if Stereo Mix not available)**
1. Download VoiceMeeter: https://vb-audio.com/Voicemeeter/
2. Install and configure as virtual audio cable
3. Set it as default playback device

## Usage

### Running the Application

Activate your virtual environment and run:

```bash
venv\Scripts\activate
python -m src.main
```

The application will start in your system tray (look for the microphone icon).

### System Tray Controls

Right-click the microphone icon in system tray:

- **Start Recording** - Begin capturing meeting audio
- **Stop Recording** - End capture and generate summary
- **Status** - View current recording status
- **Open Meetings Folder** - View saved meeting summaries
- **Exit** - Close application

### Icon Colors

- 🔵 **Blue** - Idle, ready to record
- 🔴 **Red** - Recording in progress
- 🟠 **Orange** - Processing audio chunk
- ⚪ **Gray** - Error state

### During Meetings

1. Join your Zoom/Teams meeting
2. Start the Meeting Listener from system tray
3. Receive real-time notifications for:
   - ✅ Action items (with assignee if mentioned)
   - ⚡ Decisions made
   - 💡 Key discussion points (optional)
4. Stop recording when meeting ends
5. Receive summary notification with full meeting recap

## Testing Individual Components

Each module can be tested independently:

### Test Audio Capture

```bash
python -m src.audio_capture
```

Records 10 seconds of system audio and saves chunks.

### Test Transcription

```bash
python -m src.transcription
```

Transcribes audio files from the recordings directory.

### Test AI Analysis

```bash
python -m src.ai_analyzer
```

Analyzes sample meeting transcription.

### Test Notifications

```bash
python -m src.notifier
```

Shows test toast notifications.

### Test Meeting Manager

```bash
python -m src.meeting_manager
```

Full integration test (30 seconds recording + processing).

## Output Files

Meeting data is saved to:

```
assistant/
├── recordings/         # Audio chunks (WAV files)
├── meetings/          # Meeting summaries and data
│   ├── meeting_YYYYMMDD_HHMMSS.md    # Markdown summary
│   └── meeting_YYYYMMDD_HHMMSS.json  # Raw data
└── logs/              # Application logs
    └── meeting_listener.log
```

## Configuration

Edit `.env` to customize:

```env
# Audio chunk duration (seconds)
AUDIO_CHUNK_DURATION=30

# Sample rate (Hz) - 16000 recommended for Whisper
AUDIO_SAMPLE_RATE=16000

# Audio channels (1=mono, 2=stereo)
AUDIO_CHANNELS=1
```

## Troubleshooting

### No Loopback Device Found

**Problem**: `No loopback device found` error

**Solutions**:
1. Enable Stereo Mix in Windows Sound settings (see Installation step 5)
2. Install VoiceMeeter as virtual audio cable
3. Ensure no other app is blocking audio device access

### API Key Errors

**Problem**: `Missing or invalid API key`

**Solutions**:
1. Check `.env` file exists (copy from `.env.example`)
2. Verify API keys are correct (no extra spaces)
3. Ensure API keys have proper permissions/credits

### No Audio Captured

**Problem**: Audio files are empty or silent

**Solutions**:
1. Play audio during recording to test
2. Check Windows audio output is working
3. Verify correct audio device is selected as default
4. Try adjusting volume levels

### Notifications Not Showing

**Problem**: No toast notifications appear

**Solutions**:
1. Check Windows notification settings (ensure app notifications enabled)
2. Enable "Focus Assist" to Off or Priority
3. Verify notifications work by running: `python -m src.notifier`

### High API Costs

**Problem**: Transcription/analysis costs too high

**Solutions**:
1. Increase `AUDIO_CHUNK_DURATION` to 60+ seconds
2. Use shorter meetings for testing
3. Disable key point notifications in `meeting_manager.py`

## Cost Estimates

Approximate costs per hour of meeting:

- **Whisper API**: ~$0.36/hour (at $0.006/minute)
- **Claude API**: ~$0.15/hour (depends on analysis complexity)
- **Total**: ~$0.50/hour

*Costs vary based on audio quality, chunk duration, and analysis depth.*

## Development

### Project Structure

```
assistant/
├── src/
│   ├── __init__.py           # Package initialization
│   ├── main.py               # System tray GUI entry point
│   ├── audio_capture.py      # WASAPI loopback recording
│   ├── transcription.py      # Whisper API client
│   ├── ai_analyzer.py        # Claude API client
│   ├── notifier.py           # Windows toast notifications
│   ├── meeting_manager.py    # Orchestration layer
│   └── config.py             # Configuration management
├── requirements.txt          # Python dependencies
├── .env                      # API keys (gitignored)
├── .env.example              # API key template
├── .gitignore               # Ignore rules
└── README.md                # This file
```

### Adding Features

**To customize notifications**:
Edit `src/notifier.py` and modify notification methods.

**To change AI prompts**:
Edit `src/ai_analyzer.py` → `_create_analysis_prompt()` method.

**To adjust chunk duration**:
Edit `.env` → `AUDIO_CHUNK_DURATION` (in seconds).

**To add new analysis types**:
1. Update AI prompt in `ai_analyzer.py`
2. Add notification method in `notifier.py`
3. Connect in `meeting_manager.py` → `_send_notifications()`

## Limitations

- **Windows Only**: WASAPI loopback is Windows-specific
- **System Audio Only**: Captures all system audio, not just meeting app
- **No Speaker Diarization**: Cannot identify individual speakers
- **English Focus**: Optimized for English transcription
- **Real-time Lag**: 30-60 second delay for processing

## Future Enhancements

- [ ] Auto-detect meeting start/end
- [ ] Speaker identification (diarization)
- [ ] Multi-language support
- [ ] Web dashboard for meeting history
- [ ] Calendar integration (auto-start for scheduled meetings)
- [ ] Export to Notion/Confluence
- [ ] Meeting participant tracking
- [ ] Custom AI prompt templates

## Privacy & Security

- **Local Processing**: Audio is processed via APIs, not stored permanently
- **API Keys**: Keep `.env` file secure and never commit to git
- **Audio Files**: Stored locally in `recordings/` (can be deleted)
- **Meeting Data**: Summaries saved locally in `meetings/`

**Important**: This app sends audio to OpenAI and Anthropic APIs. Review their privacy policies and ensure compliance with your organization's policies before recording meetings.

## License

MIT License - Feel free to modify and distribute.

## Credits

Built with:
- [pyaudiowpatch](https://github.com/s0d3s/PyAudioWPatch) - Windows audio capture
- [OpenAI Whisper API](https://openai.com/research/whisper) - Transcription
- [Anthropic Claude](https://www.anthropic.com/) - AI analysis
- [winotify](https://github.com/versa-syahptr/winotify) - Windows notifications
- [pystray](https://github.com/moses-palmer/pystray) - System tray

## Support

For issues or questions:
1. Check logs in `logs/meeting_listener.log`
2. Test individual components (see Testing section)
3. Verify API keys and configuration
4. Check Windows audio settings

---

**Enjoy smarter meetings! 🚀**
