import streamlit as st
import pandas as pd
import openai
#from streamlit_option_menu import option_menu

openai.api_key = st.secrets["OPENAI_API_KEY"]

def page1():
    st.title("Proyecto VOC")  # Título de la app
    st.markdown("Este es como una prueba de concepto de cómo usar inteligencia artificial para sugerir carreras a estudiantes")  # Descripción de la app
    st.markdown("Este es un proyecto creado por EquipoVOC")

    questions = {
        "¿Disfrutas trabajar con números?": ["Sí", "No", "Más o menos"],
        "¿Prefieres trabajar en interiores o exteriores?": ["Interiores", "Exteriores", "Ambos"],
        "¿Te gusta trabajar en equipo o solo?": ["Equipo", "Solo", "Ambos"],
        "¿Eres más creativo o analítico?": ["Creativo", "Analítico"],
        "¿Prefieres trabajar con tecnología o personas?": ["Tecnología", "Personas"],
        "¿Disfrutas resolver problemas?": ["Sí", "No"],
        "¿Estás interesado en ciencias?": ["Sí", "No"],
        "¿Te gusta ayudar a los demás?": ["Sí", "No"],
        "Menciona una habilidad que consideres que tienes": None,
        "¿Qué temas te interesan más en tus estudios?": None,
    }
    
    # Get user answers
    user_answers = {}  # Creación de diccionario vacío con las respuestas del usuario

    for question, options in questions.items():
        if options:
            answer = st.radio(question, options)
        else:
            answer = st.text_input(question)
        user_answers[question] = answer

    # Generate the answer
    def generate_answer():
        messages = [{"role": "system", "content": "Usa markdown para formatear el texto. Sugiere las 3 principales carreras para esta persona en universidades chilenas (públicas o privadas) según sus respuestas a un cuestionario vocacional. Usa un lenguaje motivacional, serio y con emojis:"}]
        # Add the user answers to the messages in only one string
        messages.extend([{"role": "user", "content": answer} for answer in user_answers.values()])
        completions = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
        )

        return completions.choices[0]["message"]["content"]

    # Display the results if a button is clicked
    if st.button("Ver Resultados"):
        # Call the generate_answer() function to get the top 3 careers
        top_careers = generate_answer()
        st.header("Top 3 Carreras para Ti:")
        st.markdown(top_careers)

def page1():
    st.title("Proyecto VOC")  # Título de la app
    st.markdown("Este es como una prueba de concepto de cómo usar inteligencia artificial para sugerir carreras a estudiantes")  # Descripción de la app
    st.markdown("Este es un proyecto creado por EquipoVOC")

    questions = {
        "¿Disfrutas trabajar con números?": ["Sí", "No", "Más o menos"],
        "¿Prefieres trabajar en interiores o exteriores?": ["Interiores", "Exteriores", "Ambos"],
        "¿Te gusta trabajar en equipo o solo?": ["Equipo", "Solo", "Ambos"],
        "¿Eres más creativo o analítico?": ["Creativo", "Analítico"],
        "¿Prefieres trabajar con tecnología o personas?": ["Tecnología", "Personas"],
        "¿Disfrutas resolver problemas?": ["Sí", "No"],
        "¿Estás interesado en ciencias?": ["Sí", "No"],
        "¿Te gusta ayudar a los demás?": ["Sí", "No"],
        "Menciona una habilidad que consideres que tienes": None,
        "¿Qué temas te interesan más en tus estudios?": None,
    }
    
    # Get user answers
    user_answers = {}  # Creación de diccionario vacío con las respuestas del usuario

    for question, options in questions.items():
        if options:
            answer = st.radio(question, options)
        else:
            answer = st.text_input(question)
        user_answers[question] = answer

    # Generate the answer
    def generate_answer():
        messages = [{"role": "system", "content": "Usa markdown para formatear el texto. Sugiere las 3 principales carreras para esta persona en universidades chilenas (públicas o privadas) según sus respuestas a un cuestionario vocacional. Usa un lenguaje motivacional, serio y con emojis:"}]
        # Add the user answers to the messages in only one string
        messages.extend([{"role": "user", "content": answer} for answer in user_answers.values()])
        completions = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
        )

        return completions.choices[0]["message"]["content"]

    # Display the results if a button is clicked
    if st.button("Ver Resultados"):
        # Call the generate_answer() function to get the top 3 careers
        top_careers = generate_answer()
        st.header("Top 3 Carreras para Ti:")
        st.markdown(top_careers)
