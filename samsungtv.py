import socket


class SamsungExLinkTV:
    def __init__(self, host, port=4001):
        self.host = host
        self.port = port

    def _send(self, data: bytes):
        with socket.create_connection((self.host, self.port), timeout=3) as sock:
            sock.sendall(data)

    def power_on(self):
        self._send(b"\x08\x22\x00\x00\x00\x02\xd4")

    def power_off(self):
        self._send(b"\x08\x22\x00\x00\x00\x01\xd5")

    def volume_up(self):
        self._send(b"\x08\x22\x01\x00\x01\x00\xd4")

    def volume_down(self):
        self._send(b"\x08\x22\x01\x00\x02\x00\xd3")

    def mute(self):
        self._send(b"\x08\x22\x02\x00\x00\x00\xd4")

    def select_hdmi(self, port):
        commands = {
            1: b"\x08\x22\x0a\x00\x05\x00\xc7",
            2: b"\x08\x22\x0a\x00\x05\x01\xc6",
            3: b"\x08\x22\x0a\x00\x05\x02\xc5",
            4: b"\x08\x22\x0a\x00\x05\x03\xc4",
        }
        self._send(commands[port])
