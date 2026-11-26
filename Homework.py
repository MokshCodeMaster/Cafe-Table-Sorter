def cafe_message_sorter():
  urgent_messages = []
  normal_messages = []

  # Words/phrases that automatically flag a message as URGENT
  urgent_keywords = [
      "now",
      "give me",
      "hurry",
      "asap",
      "quick",
      "fast",
      "immediately",
      "waiting forever",
      "wrong",
      "cold",
      "spill",
      "refund",
      "late",
      "allergy",
      "missing",
  ]
  print("=== CAFE MESSAGE SORTER ===")
  print("Commands: 'msg' (new message), 'view', 'next', 'quit'\n")
  while True:
    command = input("Enter command: ").strip().lower()
    if command == "msg":
      sender = input("Customer name or Table # (optional): ").strip()
      message = input("Enter customer message: ").strip()
      if not message:
        print("Message cannot be empty.\n")
        continue
      clean_text = message.lower()
      for ch in "!?.,'\"":
        clean_text = clean_text.replace(ch, "")
      is_urgent = False
      for keyword in urgent_keywords:
        if keyword in clean_text:
          is_urgent = True
          break
      if "!!" in message:
        is_urgent = True
      formatted_msg = f"[{sender}] {message}" if sender else message
      if is_urgent:
        urgent_messages.append(formatted_msg)
        print(f"-> SORTED TO [URGENT]: \"{formatted_msg}\"\n")
      else:
        normal_messages.append(formatted_msg)
        print(f"-> SORTED TO [NORMAL]: \"{formatted_msg}\"\n")
    elif command == "view":
      print("\n=== URGENT MESSAGES ===")
      if urgent_messages:
        for i, m in enumerate(urgent_messages, 1):
          print(f"{i}. {m}")
      else:
        print("(No urgent messages)")
      print("\n=== NORMAL MESSAGES ===")
      if normal_messages:
        for i, m in enumerate(normal_messages, 1):
          print(f"{i}. {m}")
      else:
        print("(No normal messages)")
      print()
    elif command == "next":
      if urgent_messages:
        current = urgent_messages.pop(0)
        print(f"*** HANDLING [URGENT]: \"{current}\" ***\n")
      elif normal_messages:
        current = normal_messages.pop(0)
        print(f"--- HANDLING [NORMAL]: \"{current}\" ---\n")
      else:
        print("All caught up! No messages in queue.\n")
    elif command == "quit":
      print("Closing Cafe Message Sorter.")
      break
    else:
      print("Unknown command. Try: msg, view, next, quit\n")
if __name__ == "__main__":
  cafe_message_sorter()

