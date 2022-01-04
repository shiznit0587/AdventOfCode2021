def day16():
    print('Running Day 16 - Part 1')

    with open('Day16/input.txt', 'r') as f:
        input = f.readline().strip()

    transmission = Transmission(input)
    packet = transmission.parsepacket()

    print(f'Packet version sum = {packet.sumversion()}')

    print('Running Day 16 - Part 2')

    print("Day 16 Complete")


# forward-declare the class so it can be self-referential
class Packet:
    pass


class Packet:
    version: int = None
    typeid: int = None
    lengthtypeid: int = None
    literal: int = None
    subpackets: list[Packet] = None
    length: int = 6

    def __init__(self, version: int, typeid: int) -> None:
        self.version = version
        self.typeid = typeid

    def sumversion(self) -> int:
        v = self.version
        if self.subpackets is not None:
            v += sum(map(lambda p: p.sumversion(), self.subpackets))
        return v


class Transmission:
    def __init__(self, transmission: str) -> None:
        self.transmission = transmission
        self.bits = 0
        self.buffer = 0

    def take(self, n: int):
        while self.bits < n:
            self.buffer = self.buffer << 8
            self.buffer = self.buffer | int(self.transmission[:2], 16)
            self.transmission = self.transmission[2:]
            self.bits += 8
        shift = self.bits - n
        v = self.buffer >> shift
        self.buffer -= v << shift
        self.bits -= n
        return v

    def parsepacket(self) -> Packet:
        packet = Packet(self.take(3), self.take(3))

        if packet.typeid == 4:
            self.parseliteral(packet)
        else:
            packet.lengthtypeid = self.take(1)
            packet.length += 1

            if packet.lengthtypeid == 0:
                subpacketbits = self.take(15)
                packet.length += 15
                parsedbits = 0
                packet.subpackets = []

                while parsedbits < subpacketbits:
                    subpacket = self.parsepacket()
                    packet.subpackets.append(subpacket)
                    packet.length += subpacket.length
                    parsedbits += subpacket.length
            else:
                subpacketcount = self.take(11)
                packet.length += 11
                packet.subpackets = [self.parsepacket() for _ in range(subpacketcount)]
                packet.length += sum(p.length for p in packet.subpackets)

        return packet

    def parseliteral(self, packet: Packet) -> None:
        v, last = 0, False
        while not last:
            b = self.take(5)
            packet.length += 5
            last = b & 16 == 0
            b = b & 15
            v = v << 4 | b
        packet.literal = v
