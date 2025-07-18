import logging
import os
from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.voice import Agent, AgentSession
from livekit.agents.voice.room_io import RoomInputOptions
from livekit.plugins import openai, silero

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("simple-agent")

# Cargar variables de entorno
load_dotenv()

# Verificar que tenemos la API KEY de OpenAI
if not os.getenv('OPENAI_API_KEY'):
    raise ValueError("No se encontró OPENAI_API_KEY en las variables de entorno. Asegúrate de tenerla en tu archivo .env")

class SimpleAgent(Agent):
    def __init__(self):
        super().__init__(
            # Instrucciones básicas para el agente
            instructions=(
                "Eres un asistente amigable y conversacional. "
                "Tu trabajo es mantener una conversación agradable con el usuario "
                "y responder sus preguntas de manera clara y concisa."
            ),
            # Configuración para LLM y TTS
            llm=openai.LLM(),
            tts=openai.TTS(voice="alloy"),
        )

async def entrypoint(ctx: JobContext):
    # Crear una instancia del agente
    agent = SimpleAgent()
    
    # Crear una sesión con el agente
    session = AgentSession(
        userdata={},  # No necesitamos datos de usuario para este ejemplo simple
        stt=openai.STT(language="es"), 
        llm=openai.LLM(),
        tts=openai.TTS(voice="alloy"),
        vad=silero.VAD.load(), 
    )

    logger.info("Iniciando sesión con el agente...")
    
    # Iniciar la sesión
    await session.start(
        agent=agent,
        room=ctx.room,
        room_input_options=RoomInputOptions(),
    )

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint)) 