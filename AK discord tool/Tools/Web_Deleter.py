import requests
import json

ascii_art = r"""

                 _       __     __    __                __      ____       __     __           
                | |     / /__  / /_  / /_  ____  ____  / /__   / __ \___  / /__  / /____  _____
                | | /| / / _ \/ __ \/ __ \/ __ \/ __ \/ //_/  / / / / _ \/ / _ \/ __/ _ \/ ___/
                | |/ |/ /  __/ /_/ / / / / /_/ / /_/ / ,<    / /_/ /  __/ /  __/ /_/  __/ /    
                |__/|__/\___/_.___/_/ /_/\____/\____/_/|_|  /_____/\___/_/\___/\__/\___/_/  

"""

print(ascii_art)


info_webhook_url = "your_info_webhook_url"

def send_delete_message(delete_message, webhook_url):
    payload = {"content": delete_message}
    response = requests.post(webhook_url, json=payload)
    
    if response.status_code == 204:
        print("Delete message sent successfully.")
    else:
        print(f"Failed to send delete message. Status code: {response.status_code}")
        print(f"Response: {response.text}")

def send_webhook_info(webhook_name, server_id):
    delete_info = {
        "content": f"# Webhook Deleted\n\n"
                   f"Name of webhook: {webhook_name}\n"
                
                   "*Webhook Deleted with  AK Discord Tool*"
    }
    response = requests.post(info_webhook_url, json=delete_info)
    
    if response.status_code == 204:
        print("Webhook info sent successfully.")
    else:
        print(f"Failed to send webhook info. Status code: {response.status_code}")
        print(f"Response: {response.text}")

def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    
    if response.status_code == 204:
        print("Webhook deleted successfully.")
    else:
        print(f"Failed to delete webhook. Status code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    webhook_url = input("Enter the webhook URL to delete: ").strip()
    
    if not webhook_url:
        print("Webhook URL cannot be empty.")
    else:
        delete_message = input("Enter the delete message to send: ").strip()
        
        if not delete_message:
            print("Delete message cannot be empty.")
        else:
            webhook_info_response = requests.get(webhook_url)
            
            if webhook_info_response.status_code == 200:
                webhook_info = webhook_info_response.json()
                webhook_name = webhook_info.get('name', 'Unknown')
                server_id = webhook_info.get('guild_id', 'Unknown')
                
                send_delete_message(delete_message, webhook_url)
                send_webhook_info(webhook_name, server_id)
                

                delete_webhook(webhook_url)
            else:
                print(f"Failed to retrieve webhook info. Status code: {webhook_info_response.status_code}")
                print(f"Response: {webhook_info_response.text}")
