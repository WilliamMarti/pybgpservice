import socket
import struct

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8888 # The TCP port used by the server

class BGPOpenPacket:
    """
    BGP Open Message Packet
    """
    def __init__(self,
                 myas:  int,
                 hold_time: int,
                 bgp_identifier: int):
        self.myas = myas
        self.hold_time = hold_time
        self.bgp_identifier = bgp_identifier
    
    def build(self) -> bytes:

        packet = struct.pack(
            '>QQhbbHHi',          # setting data types that match the field lengths
            int(0xffffffffffffffff),     # marker, 8 octets
            int(0xffffffffffffffff),     # marker, 8 octets
            28,                   # length of entire packet in octets, 28 for an Open message, 2 octets
            1,                    # 1 for Open, 1 octets
            4,                    # BGP v4, 1 octet
            self.myas,            # autonomous system number of sender, 2 octets
            self.hold_time,       # hold time in seconds, 2 octets
            self.bgp_identifier   # IP Address of Sender, 2130706433127 = 127.0.0.1, 4 octets
        )

        return packet

pak = BGPOpenPacket(
    65000,                # autonomous system number of sender, 2 octets
    100,                   # hold time in seconds, 2 octets
    2130706433            # IP Address of Sender, 2130706433127 = 127.0.0.1, 4 octets
)


print(pak.build())





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b"Hello Sarah")

    pak.build()

    #s.sendto(pak.build(), HOST, PORT)
    #data = s.recv(1024)

print(f"Received {data!r}")