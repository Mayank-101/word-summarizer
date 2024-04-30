# Streamlit UI
def main():
    st.title("Text Summarization App")
    text = st.text_area("Enter your text here:")
    
    lang_options = {
        'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani',
        'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan',
        'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-cn': 'Chinese (Simplified)', 'zh-tw': 'Chinese (Traditional)',
        'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English',
        'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'fy': 'Frisian',
        'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole',
        'ha': 'Hausa', 'haw': 'Hawaiian', 'iw': 'Hebrew', 'he': 'Hebrew', 'hi': 'Hindi', 'hmn': 'Hmong',
        'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian',
        'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer', 'ko': 'Korean',
        'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian',
        'lb': 'Luxembourgish', 'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam',
        'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongolian', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali',
        'no': 'Norwegian', 'or': 'Odia', 'ps': 'Pashto', 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese',
        'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic', 'sr': 'Serbian',
        'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian',
        'so': 'Somali', 'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik',
        'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'ug': 'Uyghur',
        'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'
    }
    
    trans_lang = st.selectbox("Select language for translation:", list(lang_options.values()))

    if st.button("Summarize"):
        if text.strip() == "":
            st.warning("Please enter some text to summarize.")
        else:
            lang_code = [k for k, v in lang_options.items() if v == trans_lang][0]
            summarized_text = generate_summary(text, word_embeddings)

            st.subheader("Original Text:")
            st.write(text)

            st.subheader("Summarized Text:")
            for i in range(min(5, len(summarized_text))):
                st.write(summarized_text[i][1])

            # Language detection
            try:
                lang_detection = detect_langs(text)
                st.write("Detected language:", lang_detection)
            except Exception as lang_error:
                st.error("Error detecting language: " + str(lang_error))

            # Translation
            translator = Translator()
            translated_sentences = []
            for _, sentence in summarized_text[:5]:
                try:
                    translated_sentence = translator.translate(sentence, dest=lang_code).text
                    translated_sentences.append(translated_sentence)
                except Exception as e:
                    st.warning(f"Translation failed for '{sentence}' with error: {e}")

            st.subheader("Translated Summary:")
            for translated_sentence in translated_sentences:
                st.write(translated_sentence)

if __name__ == "__main__":
    main()
