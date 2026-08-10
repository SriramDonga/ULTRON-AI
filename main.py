from core.brain import UltronBrain


def main():
    ultron = UltronBrain()

    print("================================")
    print("        ULTRON AI v0.1")
    print("================================")
    print("Type 'exit' to quit.")

    while True:
        command = input("You: ")

        if command.lower() == "exit":
            print("ULTRON: Goodbye.")
            break

        response = ultron.think(command)

        print(f"ULTRON: {response}")


if __name__ == "__main__":
    main()