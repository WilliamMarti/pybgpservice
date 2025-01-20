import sys
import socket
import selectors
import types
import struct


def main():
    """
    Test BGP Serivce
    """

    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 179  # TCP Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        s.listen()

        conn, addr = s.accept()

        with conn:

            print(f"Connected by {addr}")

            while True:

                #data = conn.recv(1024)

                unpacker = struct.Struct('>QQhbbHHIb')
                unpacked_data = unpacker.unpack(conn.recv(unpacker.size))

                print(unpacked_data)

                if not unpacked_data:

                    break

                conn.sendall(unpacked_data)

if __name__ == "__main__":

    main()
