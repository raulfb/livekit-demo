# LiveKit OpenAI Agent

Este proyecto es un agente conversacional que utiliza LiveKit y OpenAI para proporcionar interacciones de voz y texto. El agente puede manejar preguntas y respuestas en español, y está diseñado para ser utilizado en un entorno de desarrollo.

## Requisitos

- Python 3.11 o superior
- Docker y Docker Compose
- Claves de API de OpenAI

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. **Crear un entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate  # En Windows
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar las variables de entorno:**
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```env
   LIVEKIT_URL=ws://localhost:7880
   LIVEKIT_KEYS=devkey: devsecret
   LIVEKIT_API_KEY=devkey
   LIVEKIT_API_SECRET=devsecret
   OPENAI_API_KEY=sk-...tu_api_key_aqui...
   ```

## Uso

1. **Levantar el servidor LiveKit:**
   ```bash
   docker compose up -d
   ```

2. **Iniciar el agente en modo desarrollo:**
   ```bash
   python3 simple_agent.py dev
   ```
3. **Conectarse a una sala:**
   En otra terminal, puedes usar:
   ```bash
   python3 simple_agent.py connect --room mi-sala-prueba
   ```

   O para pruebas en modo texto:
   ```bash
   python3 simple_agent.py console
   ```

## Notas

- Asegúrate de que tu micrófono esté configurado correctamente si deseas usar el modo de audio.
- Puedes alternar entre el modo texto y audio usando `Ctrl + B` en el modo consola.
