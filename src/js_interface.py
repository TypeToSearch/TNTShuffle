from spotify import SpotifyContext


class JsInterface:
    """
    Methods directly exposed to javascript
    """
    def authenticate(self):
        try:
            SpotifyContext()
            return True
        except SpotifyException:
            return False

    def test(self):
        SpotifyContext().test()

