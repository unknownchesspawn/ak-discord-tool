import requests
import time

ascii_art = r"""
         _       __     __    __                __      _____                                          
        | |     / /__  / /_  / /_  ____  ____  / /__   / ___/____  ____ _____ ___  ____ ___  ___  _____
        | | /| / / _ \/ __ \/ __ \/ __ \/ __ \/ //_/   \__ \/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/
        | |/ |/ /  __/ /_/ / / / / /_/ / /_/ / ,<     ___/ / /_/ / /_/ / / / / / / / / / / /  __/ /    
        |__/|__/\___/_.___/_/ /_/\____/\____/_/|_|   /____/ .___/\__,_/_/ /_/ /_/_/ /_/ /_/\___/_/                                              /_/                                         
"""

print(ascii_art)


webhook = input("Enter the webhook URL: ").strip()
text = input("Enter the message you want to send: ").strip()

if not webhook or not text:
    print("Webhook URL and message cannot be empty.")
else:
    print(f"Sending message: '{text}' to the webhook...")

    while True:
        try:
            payload = {"content": text}
            response = requests.post(webhook, json=payload)
            
            if response.status_code == 204:
                print("Message sent successfully.")
            else:
                print(f"Failed to send message. Status code: {response.status_code}")
            
            time.sleep(0.1)

        except KeyboardInterrupt:
            print("\nStopped by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
