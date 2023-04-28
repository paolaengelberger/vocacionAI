# Vocación AI Chile 🤖🇨🇱

Este es un programa que te ayudará a descubrir cuáles son las principales carreras que podrías estudiar en universidades chilenas (públicas o privadas) según tus respuestas a un cuestionario vocacional 📝

## Cómo funciona 🤔

El programa funciona de la siguiente manera:

1. El programa te hará una serie de preguntas sobre tus preferencias y habilidades 🤓. Estas preguntas están diseñadas para conocer tus intereses, habilidades y preferencias con el objetivo de recomendarte las carreras que mejor se adapten a ti. 

2. Deberás responder cada pregunta seleccionando una de las opciones que se te presentan 🤷‍♂️🤷‍♀️. Las opciones que se te presentan en cada pregunta han sido cuidadosamente seleccionadas para que puedas elegir la que mejor se adapte a tus preferencias.

3. Al finalizar, deberás hacer clic en el botón "Ver Resultados" para recibir tus recomendaciones de carreras 👨‍🎓👩‍🎓. Una vez que hayas respondido todas las preguntas, el programa te mostrará las tres carreras que mejor se adaptan a tus intereses y habilidades.

## Código del Programa 🖥️

El programa está escrito en Python y utiliza las siguientes librerías:

- `streamlit`: Una librería que facilita la creación de aplicaciones web. Esta librería permite diseñar la interfaz de usuario de manera sencilla y eficiente.

- `openai`: Una plataforma que proporciona servicios de inteligencia artificial. En este programa, se utiliza la plataforma `openai` para generar un mensaje motivacional y serio que presenta las 3 principales carreras para el usuario según sus respuestas al cuestionario.

El código se divide en dos partes principales: 

1. Definición de las preguntas y almacenamiento de las respuestas del usuario.

```
questions = {
    "¿Disfrutas trabajar con números?": ["Sí", "No"],
    "¿Prefieres trabajar en interiores o exteriores?": ["Interiores", "Exteriores"],
    "¿Te gusta trabajar en equipo o solo?": ["Equipo", "Solo"],
    "¿Eres más creativo o analítico?": ["Creativo", "Analítico"],
    "¿Prefieres trabajar con tecnología o personas?": ["Tecnología", "Personas"],
    "¿Disfrutas resolver problemas?": ["Sí", "No"],
    "¿Estás interesado en ciencias?": ["Sí", "No"],
    "¿Te gusta ayudar a los demás?": ["Sí", "No"],
    "Menciona una habilidad que consideres que tienes": None,
    "¿Qué temas te interesan más en tus estudios?": None,
}

user_answers = {}

for question, options in questions.items():
    if options:
        answer = st.radio(question, options)
    else:
        answer = st.text_input(question)
    user_answers[question] = answer
```

En esta parte del código, se definen las preguntas que se le harán al usuario y se almacenan las respuestas en un diccionario llamado `user_answers`. Cada pregunta tiene dos posibles tipos de respuesta: una lista de opciones (`options`) o una respuesta de texto (`None`). Para las preguntas con opciones, se utiliza la función `st.radio` para mostrar las opciones y permitir al usuario seleccionar una. Para las preguntas de texto, se utiliza la función `st.text_input` para permitir al usuario escribir su respuesta.

2. Generación de recomendaciones de carreras.

```
def generate_answer():
    messages = [{"role": "system", "content": "Usa markdown para formatear el texto. Sugiere las 3 principales carreras para esta persona en universidades chilenas (públicas o privadas) según sus respuestas a un cuestionario vocacional. Usa un lenguaje motivacional, serio y con emojis:"}]
    # Add the user answers to the messages in only one string
    messages.extend([{"role": "user", "content": answer} for answer in user_answers.values()])
    completions = openai.ChatCompletion.create(
        model="davinci",
        messages=messages,
        temperature=0.7,
    )

    return completions.choices[0]["text"]
```

En esta parte del código, se utiliza la plataforma `openai` para generar un mensaje motivacional y serio que presenta las 3 principales carreras para el usuario según sus respuestas al cuestionario. Para generar el mensaje, se utiliza el modelo de lenguaje natural `davinci` de OpenAI. El mensaje se genera a partir de una serie de mensajes que incluyen las preguntas y respuestas del usuario. El resultado es el mensaje motivacional y serio que presenta las 3 principales carreras para el usuario.

## Cómo Ejecutar el Código 🏃‍♂️

Si deseas ejecutar el código en tu ordenador, sigue los siguientes pasos:

1. Clona el repositorio en tu ordenador. Para hacer esto, dirígete al repositorio en Github y haz clic en el botón "Clone or download". Luego, copia la URL del repositorio y ejecuta el siguiente comando en tu terminal:

```
git clone URL_DEL_REPOSITORIO
```

2. Instala las librerías necesarias con el comando `pip install -r requirements.txt`. Este comando instalará todas las librerías necesarias para ejecutar el programa.

3. Crea un archivo `secrets.toml` y agrega tu clave de API de OpenAI en el siguiente formato:

```
[openai]
api_key = "TU_CLAVE_DE_API_AQUÍ"
```

La clave de API de OpenAI es necesaria para utilizar la plataforma de inteligencia artificial que genera las recomendaciones de carreras. Si no tienes una clave de API, puedes crear una cuenta en el sitio web de OpenAI y seguir las instrucciones para obtener una.

4. Ejecuta el programa con el comando `streamlit run main.py`. Este comando iniciará el programa y te permitirá responder las preguntas del cuestionario.

5. Responde las preguntas y haz clic en "Ver Resultados" para obtener tus recomendaciones de carreras. Una vez que hayas respondido todas las preguntas, el programa te mostrará las tres carreras que mejor se adaptan a tus intereses y habilidades.

## Conclusión 🎓

Esperamos que este programa te ayude a descubrir tu vocación en el campo de la inteligencia artificial en Chile. Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto con nosotros. ¡Buena suerte en tu búsqueda de carreras! 🚀🇨🇱