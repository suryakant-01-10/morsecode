Morse_code_dic={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
    '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-',
    '-.--.': '(', '-.--.-': ')', '.-..-.': '"', '.----.': "'", '...-..-': '$',
    '.--.-.': '@', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+',
    '...---...': 'SOS',}
def morse_code_to_english(morse_message):
    english_message=[]
    morse_words=morse_message.strip().split("/")
    for morse_word in morse_words:
        english_word=""
        morse_letters=morse_word.split(" ")
        for morse_letter in morse_letters:
            if morse_letter in Morse_code_dic:
                english_word+=Morse_code_dic[morse_letter]
            elif morse_letter=="":
                continue
            else:
                english_word="?"
        english_message.append(english_word)

    return" ".join(english_message)
if __name__=="__main__":
    print("Morse Code English Transletor")
    print("=================")
    print("Enter your Morse code below.")
    print("Separate letters with a single space(e.g,'.......'')")
    print("Separate words with a'/'")
    print("Type 'exit'or'quit' to stop the pogram.\n")
    
    try:
        while True:
            user_input=input("Morse Code:")
            if user_input.lower() in ["exit","quit"]:
                print("Goodbye!")
                break
            if not user_input:
                continue
            translated_text=morse_code_to_english(user_input)
            print(f"English: {translated_text}\n")
    except EOFError:
        print("\nGoodbye!")
    except KeyboardInterrupt:
        print("\nProgram Intterrupted. Goodbye!")
