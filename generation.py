import re

from interfaces.base import BaseInterface
from interfaces.chat_gpt import GPTInterface

def main() -> None:
    print("Please input your LLM of choice. \n[1] ChatGPT 3.5")

    model_name = input()

    model: BaseInterface

    match model_name:
        case "1":
            model = GPTInterface()
        case other:
            print("Unsupported model type, exiting")
            raise ValueError("Unsupported model type!")
        
    model.getToken()

    with open("prefixes/main.txt", 'r') as file:
        prefix = file.read()
    
    print("Please enter the topic of the scam, in a few words.")
    print("Example: \"Amazon suspicious purchase\"\n")

    topic = input()
    print("Please wait. It may take several minutes for ChatGPT to respond...")

    preliminary_output = model.call(prefix + topic)
    print("Preliminary output: ", preliminary_output)

    blanks = set(re.findall(r'\[.+?\]', preliminary_output))
    print("ChatGPT returned ", len(blanks), "blank fields.")

    for blank in blanks:
        print("Fill in the following blank with some information, or type 'g' to ask the LLM to generate input.")
        print(blank)
        blank_input = input()

        if blank_input == 'g':
            print("Would you like to generate a full [p]aragraph, or a [f]ragment only?")
            fragment_type = input()

            with open("prefixes/fragment.txt", 'r') as file:
                fragment = file.read()

            with open("prefixes/paragraph.txt", 'r') as file:
                paragraph = file.read()

            if fragment_type == "f":
                blank_input = model.call(fragment + blank)
            else:
                blank_input = model.call(paragraph + blank)

        else:
            preliminary_output = preliminary_output.replace(blank, blank_input)

    print("Final output: ", preliminary_output)


if __name__ == "__main__":
    main()