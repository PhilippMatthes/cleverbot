from CleverBot import CleverBot
import traceback

if __name__=="__main__":
    try:
        Conversation = CleverBot()
        Conversation.talk()
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as err:
        print(traceback.format_exc(err))
