import aiml
import os

# Create the kernel and learn AIML files
kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
   kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
   kernel.saveBrain("bot_brain.brn")

# Press CTRL-C to break this loop
while True:
    message = raw_input("Enter your message to the bot: ")
    if message == "quit" or message == "goodbye":
       exit()
    elif message == "save":
      kernel.saveBrain("bot_brain.brn")
    else:
      bot_response = kernel.respond(message)
      print bot_response