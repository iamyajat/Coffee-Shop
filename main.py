import openai
from colorama import Fore, Style
import datetime
import time

ct = datetime.datetime(2019, 2, 14, 16, 0, 0)
current_time = ct.strftime("%Y-%m-%d %H:%M:%S")

openai_key = open("openai_key.txt", "r").read().strip()
openai.api_key = openai_key

eddie = """You are Eddie. Eddie is a student at VIT University, Vellore who is passionate about pursuing a degree in Computer Science and Engineering. Outside of his academic pursuits, he enjoys maintaining an active lifestyle and engaging in outdoor adventures. He is driven by ambition and aspires to work in a tech company that values innovation and creativity. He has a deep love for music and plays the guitar in his spare time. He is a North Indian and shares a strong bond with his younger sister, whom he cherishes and looks out for as an older brother. His parents, both professionals in their respective fields, have instilled in him the values of hard work, perseverance, and the importance of education. He loves baking as well.
"""
maria = """You are Maria. Maria is a vivacious and bold young woman in her sophomore year at VIT University, Vellore. She has a love for partying and alcohol, and embraces a carefree and adventurous lifestyle. She is not the most agreeable person, but is determined to score as low as possible in her rice purity test and uses Gen Z language and foul language. Maria hails from a wealthy family, and has a strong sense of independence and self-assurance. Her journey through college is one of self-discovery and embracing life's adventures. She is a South Indian. She hates baking.
"""

coffee_shop = """Talk in first person. You have 1 hour to spend together. Talk about anything. Make up stuff if you want but don't say yes to everything. DO NOT BE AFRAID TO BE DRAMATIC. Maria and Eddie meet at a cozy coffee shop in their university town. They exchange a warm smile and choose a corner table near a large window. The table is adorned with a small vase of fresh flowers and a flickering candle, creating a romantic atmosphere. Maria and Eddie visit a coffee shop for Valentine's Day, where they browse the menu and order coffees and pastries. The coffee shop provides a comfortable space for them to get to know each other, with a dreamy backdrop of snowfall and streetlights. With each sip, they embark on a journey of discovery, exploring their shared interests and unique chemistry. Use 1-2 sentences for your reply.
"""

eddie_system_prompt = eddie + "\n" + coffee_shop
maria_system_prompt = maria + "\n" + coffee_shop

eddie_conversation_history = [{
    "role": "system",
    "content": eddie_system_prompt
}]
maria_conversation_history = [{
    "role": "system",
    "content": maria_system_prompt
}]

eddie_chat = "Hey Maria, you look beautiful. Take a seat."
maria_chat = ""

print(current_time + " | " + Fore.GREEN + "Eddie: " +
      Style.RESET_ALL + eddie_chat.strip())

eddie_conversation_history.append({
    "role": "system",
    "content": "Current time: " + current_time
})
eddie_conversation_history.append({
    "role": "assistant",
    "content": eddie_chat
})

maria_conversation_history.append({
    "role": "system",
    "content": "Current time: " + current_time
})
maria_conversation_history.append({
    "role": "user",
    "content": eddie_chat
})

while True:
    # Maria's turn
    maria_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=maria_conversation_history,
    )
    maria_chat = maria_response["choices"][0]["message"]["content"]
    maria_conversation_history.append({
        "role": "assistant",
        "content": maria_chat
    })
    eddie_conversation_history.append({
        "role": "user",
        "content": maria_chat
    })
    print(current_time + " | " + Fore.GREEN + "Maria: " +
          Style.RESET_ALL + maria_chat.strip())

    ct += datetime.timedelta(minutes=2)
    current_time = ct.strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(5)

    # Eddie's turn
    eddie_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=eddie_conversation_history,
    )
    eddie_chat = eddie_response["choices"][0]["message"]["content"]
    eddie_conversation_history.append({
        "role": "assistant",
        "content": eddie_chat
    })
    maria_conversation_history.append({
        "role": "user",
        "content": eddie_chat
    })
    print(current_time + " | " + Fore.GREEN + "Eddie: " +
          Style.RESET_ALL + eddie_chat.strip())

    ct += datetime.timedelta(minutes=3)
    current_time = ct.strftime("%Y-%m-%d %H:%M:%S")

    # add time to conversation history
    eddie_conversation_history.append({
        "role": "system",
        "content": "Current time: " + current_time
    })
    maria_conversation_history.append({
        "role": "system",
        "content": "Current time: " + current_time
    })
    time.sleep(7)
