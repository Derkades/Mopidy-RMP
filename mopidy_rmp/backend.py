import pykka
from typing import TYPE_CHECKING, Optional

from mopidy import backend
from mopidy import httpclient

user_agent = httpclient.format_user_agent('Mopidy-RMP')

Uri = str


class RaphsonPlayback(backend.PlaybackProvider):

    def __init__(self, audio, bakend):
        super(RaphsonPlayback, self).__init__(audio, bakend)

    def get_time_position() -> int:
        return 0

    def is_live(uri: Uri):
        return False

    def pause() -> bool:
        return False

    def play() -> bool:
        return False

    def resume() -> bool:
        return False

    def seek(time_position: int) -> bool:
        return False

    def should_download(uri: Uri) -> bool:
        return True

    def stop() -> bool:
        return False

    def translate_uri(uri: Uri) -> Optional[Uri]:
        return None


class RaphsonBackend(pykka.ThreadingActor, backend.Backend):
    def __init__(self, config, audio):
        super(RaphsonBackend, self).__init__()
        self.audio = audio
        self.playback = RaphsonPlayback(audio, self)
