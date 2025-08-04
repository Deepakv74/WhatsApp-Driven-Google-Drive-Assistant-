from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os
from drive_helper import list_files, delete_file, move_file, summarize_folder
from logger import log_action

load_dotenv()

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip()
    resp = MessagingResponse()
    msg = resp.message()

    try:
        parts = incoming_msg.split()
        cmd = parts[0].upper()

        if cmd == "LIST":
            folder = parts[1]
            result = list_files(folder)
        elif cmd == "DELETE":
            file_path = parts[1]
            result = delete_file(file_path)
        elif cmd == "MOVE":
            source, dest = parts[1], parts[2]
            result = move_file(source, dest)
        elif cmd == "SUMMARY":
            folder = parts[1]
            result = summarize_folder(folder)
        else:
            result = "Unknown command. Use LIST, DELETE, MOVE, or SUMMARY."

        msg.body(result)
        log_action(incoming_msg, result)

    except Exception as e:
        msg.body(f"Error: {str(e)}")
        log_action(incoming_msg, f"Error: {str(e)}")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)