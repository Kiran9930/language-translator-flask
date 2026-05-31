from translate import Translator


def get_language():
    print("\n===== Language Translator =====")
    print("1. Hindi")
    print("2. French")
    print("3. Spanish")
    print("4. German")
    print("5. Japanese")

    choice = input("Choose language (1-5): ")

    languages = {
        "1": "hi",
        "2": "fr",
        "3": "es",
        "4": "de",
        "5": "ja"
    }

    return languages.get(choice)


def translate_text(text, lang):
    translator = Translator(to_lang=lang)
    return translator.translate(text)


def main():
    lang = get_language()

    if not lang:
        print("Invalid choice!")
        return

    text = input("Enter text to translate: ")

    try:
        translated_text = translate_text(text, lang)

        print("\nTranslated Text:")
        print(translated_text)

    except Exception as e:
        print("Translation failed!")
        print(e)


main()