def check_bad_words(message, bad):
    message = message.split()
    for i in message:
        if i.lower() in bad and i != '':
            return False
    return True
