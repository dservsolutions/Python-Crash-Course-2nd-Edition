# 8.9 Messages
messages = ['Welcome', 'Hi, there..', 'Nice to meet you', 'Have a good one', 'Hope to see you again']

# def show_message():
#     for message in  messages:
#         print(message)
    
# show_message()    

# 8.10 Sending Messages
def send_messages(messages_to_send, sent_messages):
    while messages_to_send:
        messages = messages_to_send.pop()
        print(f"Messages to send: {messages}")
        sent_messages.append(messages)

def show_sent(sent_messages):
    print("\nThe following message were sended.")
    for messages in sent_messages:
        print(messages)

          
messages_to_send = messages[:]
sent_messages = []

"""8.11 Archived Messages"""
send_messages(messages_to_send[:], sent_messages)
show_sent(sent_messages)
print(messages_to_send)
print(sent_messages)


