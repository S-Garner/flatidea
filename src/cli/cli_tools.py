import subprocess

SYSTEM = (
    "You are a concise CLI assistant. "
    "Respond only to the user's latest input."
    "You will respond only in English."
)

def cli():
    history = f"System: {SYSTEM}\n"
    MODEL = "mistral:latest"

    while True:
        cmd = input("> ")
        if cmd == "/quit" or cmd == "/q":
            break

        tokens = cmd.split()
        
        if "/model" in tokens:
            MODEL = tokens[1]
            print(f"< Now set to {MODEL}")
            continue
        
        if "/list" in tokens:
            list_result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True
            )
            
            print(f"{list_result}")

        history += f"User: {cmd}\nAssistant:\n"

        result = subprocess.run(
            ["ollama", "run", MODEL, history],
            capture_output=True,
            text=True
        )

        reply = result.stdout.strip()
        print(f"< {reply}")

        history += reply + "\n"
