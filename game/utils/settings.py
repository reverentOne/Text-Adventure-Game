def change_settings(user_input):
    """
    Show or change game settings.

    Args:
        user_input: Get input from game_action function.

    Usage:
        > settings
        > settings hud on
        > options hud hints off
    """

    settings_printout = f"""\n        -------------------- SETTINGS --------------------
        {on_off(rimuru.textcrawl)}\ttextcrawl <on/off>\t-- Enable or disable text crawl effect.
        {on_off(rimuru.show_actions)}\thud/interface <on/off>\t-- Show available actions player can take.
        {on_off(rimuru.show_art)}\tart/ascii <on/off>\t-- Show ASCII art.
        {on_off(rimuru.show_hints)}\thints/clues <on/off>\t-- Show game hints, highly recommended for first timers.
        {on_off(rimuru.hardcore)}\thardcore <on/off>\t-- Hides playable actions, tutorial, and hints.

    Usage:
        /settings COMMAND(S) on/off
        Example: '/settings textcrawl off', '/options hud hints off
    """

    new_value = None
    # Tries to extract game settings and on/off section from user_input.
    try:
        split_input = user_input.split()
        # Checks if player wants to enable/disable a setting.
        if get_any(split_input[-1], off_subs): new_value = False
        elif get_any(split_input[-1], on_subs): new_value = True
        # User can change multiple game settings with one go.
        settings_input = ''.join(user_input[:-1])
    except: new_value = None

    # If not detected game settings with usable on/off data from user_input.
    if not user_input or new_value is None:
        print(settings_printout)
        return

    if 'textcrawl' in settings_input: rimuru.textcrawl = new_value
    if 'hardcore' in settings_input: rimuru.hardcore = new_value
    # strict_match is false so user can change multiple game settings in one go.
    if get_any(settings_input, ['hud', 'interface'], strict_match=False): rimuru.show_actions = new_value
    if get_any(settings_input, ['art', 'ascii'], strict_match=False): rimuru.show_art = new_value
    if get_any(settings_input, ['hints', 'clues'], strict_match=False): rimuru.show_hints = new_value

    print(settings_printout)
