import streamlit as st
from googletrans import LANGUAGES, Translator

def main():
    # Set up the Streamlit app title and description
    st.title("Language Translator")
    st.write("Translate text from one language to another")

    # Set up the layout with two columns
    col1, col2 = st.columns(2)

    # Input area for the text to be translated on the left side
    with col1:
        text_input = st.text_area("Enter Text To Translate:", "",height=477)

    # Get the list of supported languages
    languages = get_languages()

    # Dropdown for selecting the target language on the right side
    with col2:
        target_lang = st.selectbox("Select Target Language:", languages)

    # Translate button
    if st.button("Translate"):
        if text_input:
            # Perform translation and display the result on the right side
            translation_result = translate_text(text_input, target_lang)
            with col2:
                st.subheader("Translation Result:")
                st.write(translation_result)
        else:
            st.write("Please Enter Text To Translate")


def get_languages():
    # Get the list of supported languages using Googletrans
    languages = [LANGUAGES[lang] for lang in LANGUAGES]
    return languages


def translate_text(text, target_lang):
    # Perform translation using the Translator class from Googletrans
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

# Run the Streamlit app
if __name__ == "__main__":
    main()
