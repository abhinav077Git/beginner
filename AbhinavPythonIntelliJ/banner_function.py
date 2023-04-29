# def banner_text(text):
#     screen_width=80
#     if len(text) > screen_width -4:
#         print("text is too large to fit in screen width")
#     if text == "*":
#         print("*" * screen_width)
#     else:
#         centered_string=text.center(screen_width - 4)
#         print(f"**{centered_string}**")

###default parameter value###
# def banner_text(text,screen_width=80):
#     if len(text) > screen_width -4:
#         print("text is too large to fit in screen width")
#     if text == "*":
#         print("*" * screen_width)
#     else:
#         centered_string=text.center(screen_width - 4)
#         print(f"**{centered_string}**")



# def banner_text(text,screen_width=80):
#     if len(text) > screen_width -4:
#         print("text is too large to fit in screen width")
#     if text == "*":
#         print("*" * screen_width)
#     else:
#         centered_string=text.center(screen_width - 4)
#         print(f"**{centered_string}**")
# banner_text("*")
# banner_text("Always look on the bright side of life...")
# banner_text("If life seems jolly rotten,")
# banner_text("There's something you've forgotten!")
# banner_text("And that's to laugh and smile and dance and sing,")
# banner_text(" ")
# banner_text("When you're feeling in the dumps,")
# banner_text("Don't be silly chumps,")
# banner_text("Just purse your lips and whistle - that's the thing!",66)
# banner_text("And... always look on the bright side of life...",66)
# banner_text("*")


###keyword argument####
def banner_text(text:str=" ",screen_width:int=80)->None:
    """_summary_

    Args:
        text (str, optional): _description_. Defaults to " ".
        screen_width (int, optional): _description_. Defaults to 80.
    """
    if len(text) > screen_width -4:
        print("text is too large to fit in screen width")
    if text == "*":
        print("*" * screen_width)
    else:
        centered_string=text.center(screen_width - 4)
        print(f"**{centered_string}**")
banner_text("*",60)
banner_text("Always look on the bright side of life...",60)
banner_text("If life seems jolly rotten,",60)
banner_text("There's something you've forgotten!",60)
banner_text("And that's to laugh and smile and dance and sing,",60)
banner_text(screen_width=60)#keyword argument
banner_text("When you're feeling in the dumps,",60)
banner_text("Don't be silly chumps,",60)
banner_text("Just purse your lips and whistle - that's the thing!",60)
banner_text("And... always look on the bright side of life...",60)
banner_text("*",60)

