import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import os
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentServer, AgentSession, Agent, inference
from livekit.plugins import anam, silero

load_dotenv()


class MedMuseumAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are Anil, an AI avatar all about fixing boredom at workplace." \
            " Answer with a bit of sarcasm. Be concise." \
            " Avoid long explanations. Use humor to keep the conversation light and engaging."
        )

    async def on_enter(self):
        await self.session.say("Hello! I'm Anil. Let's talk and chill out.")


server = AgentServer()


@server.rtc_session(agent_name="MedMuseum-Avatar")
async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
        stt=inference.STT("deepgram/nova-2"),
        llm=inference.LLM("openai/gpt-4.1-mini"),
        tts=inference.TTS(
            model="elevenlabs/eleven_turbo_v2",
            voice = "pNInz6obpgDQGcFmaJgB",
            sample_rate=16000,
        ),
        vad=silero.VAD.load(),
    )

    avatar = anam.AvatarSession(
        persona_config=anam.PersonaConfig(
            name="Anil",
            avatarId=os.environ["ANAM_AVATAR_ID"],
        ),
    )

    await avatar.start(session, room=ctx.room)
    await session.start(room=ctx.room, agent=MedMuseumAgent())


if __name__ == "__main__":
    agents.cli.run_app(server)