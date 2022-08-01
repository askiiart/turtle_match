from pygame import mixer


class Audio:
    background_music = 0
    click_sound = 0
    match_made_sound = 0
    no_match_sound = 0
    game_success_sound = 0

    @staticmethod
    def start_audio():
        mixer.init()

        # Background music is Fisticuffs in Frederick Street, by Christophe Saunière
        mixer.music.load('audio/background.wav')

        # Click sound... I don't remember where I got it. Sorry for no link.
        Audio.click_sound = mixer.Sound('audio/mouse_click.wav')

        # Match made sound
        # https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=43637
        Audio.match_made_sound = mixer.Sound('audio/match_made.wav')

        # no_match sound is from https://freesound.org/people/distillerystudio/sounds/327738/
        Audio.no_match_sound = mixer.Sound('audio/no_match.wav')

        # game_success_sound is from https://freesound.org/people/jimhancock/sounds/376318/
        Audio.game_success_sound = mixer.Sound('audio/game_success.wav')

    @staticmethod
    def play_background_music():
        mixer.music.play(-1)
        mixer.music.set_volume(0.5)

    @staticmethod
    def stop_background_music():
        mixer.music.stop()

    @staticmethod
    def click():
        Audio.click_sound.play()

    @staticmethod
    def match_made():
        Audio.match_made_sound.play()

    @staticmethod
    def no_match():
        Audio.no_match_sound.play()

    @staticmethod
    def game_success():
        Audio.game_success_sound.play()
