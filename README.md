# Voice Avatar Agent

A real-time AI voice avatar built with LiveKit Agents and Anam AI. It listens, thinks, speaks, and lip-syncs a photorealistic avatar — all in the browser.

---

## Stack

| Layer | Provider |
|---|---|
| Speech-to-text | Deepgram Nova-2 (via LiveKit Inference) |
| LLM | GPT-4.1-mini (via LiveKit Inference) |
| Text-to-speech | ElevenLabs eleven_turbo_v2 (via LiveKit Inference) |
| Avatar | Anam AI — Hunter |
| Transport | LiveKit Cloud (WebRTC) |

---

## Setup

### 1. Prerequisites
- Python 3.10–3.14
- A [LiveKit Cloud](https://cloud.livekit.io) account (free)
- An [Anam AI](https://lab.anam.ai) account (free)

### 2. Install dependencies

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

### 3. Configure environment

Create a `.env` file in the project root:

```env
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

ANAM_API_KEY=your_anam_api_key
ANAM_AVATAR_ID=your_avatar_id
```

**Getting your keys:**
- LiveKit → [cloud.livekit.io](https://cloud.livekit.io) → Settings → API Keys
- Anam API key → [lab.anam.ai](https://lab.anam.ai) → API Keys
- Anam Avatar ID → run `python check_persona.py` and copy the `avatar.id` value

### 4. Run the agent

```bash
python agent.py dev
```

### 5. Test in browser

Open [cloud.livekit.io](https://cloud.livekit.io) → Agent Console → set agent name to `MedMuseum-Avatar` → Connect.

---

## Project Structure

```
livekit_worker/
├── agent.py            # Main agent — STT, LLM, TTS, avatar
├── check_persona.py    # Utility to find your Anam avatar ID
├── requirements.txt
└── .env
```

---

## Notes

- TTS sample rate is fixed at **16000 Hz** — required by Anam for lip-sync
- On corporate networks (e.g. Siemens), SSL is patched via `pip_system_certs` at the top of `agent.py`
- To change the avatar voice, update the `voice=` parameter in the `inference.TTS` block with any ElevenLabs voice ID
- To connect to a Neo4j knowledge graph, add a `@function_tool` to the agent that queries your Graph RAG pipeline