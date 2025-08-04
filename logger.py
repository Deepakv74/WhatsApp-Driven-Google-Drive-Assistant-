from datetime import datetime

def log_action(command, result):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()} | CMD: {command} | RESULT: {result[:100]}\n")
