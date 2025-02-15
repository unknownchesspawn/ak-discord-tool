import requests

ascii_art = r"""

                 _       __     __    __                __      ______          __           
                | |     / /__  / /_  / /_  ____  ____  / /__   /_  __/__  _____/ /____  _____
                | | /| / / _ \/ __ \/ __ \/ __ \/ __ \/ //_/    / / / _ \/ ___/ __/ _ \/ ___/
                | |/ |/ /  __/ /_/ / / / / /_/ / /_/ / ,<      / / /  __(__  ) /_/  __/ /    
                |__/|__/\___/_.___/_/ /_/\____/\____/_/|_|    /_/  \___/____/\__/\___/_/ 
                
"""

print(ascii_art)


def send_message_to_webhook(webhook_url):
    message = "Webhook Working"
    
    payload = {"content": message}
    
    try:
        response = requests.post(webhook_url, json=payload)
        
        if response.status_code == 204 or response.status_code == 200:
            print("Message sent successfully: Webhook Working")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user for the webhook URL
    webhook_url = input("Enter the webhook URL: ").strip()
    
    if webhook_url:
        send_message_to_webhook(webhook_url)
    else:
        print("Webhook URL cannot be empty.")
