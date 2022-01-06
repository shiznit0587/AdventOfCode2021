import functools
import operator


def day16():
    print('Running Day 16 - Part 1')

    with open('Day16/input.txt', 'r') as f:
        packet = Transmission(f.readline().strip()).parsepacket()

    print(f'Packet version sum = {packet.sumversion()}')
    print('Running Day 16 - Part 2')
    print(f'Transmission value = {packet.calcvalue()}')
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
            v += sum(map(Packet.sumversion, self.subpackets))
        return v

    def calcvalue(self) -> int:
        values = list(map(Packet.calcvalue, self.subpackets)) if self.subpackets is not None else None

        match self.typeid:
            case 0: return sum(values)
            case 1: return functools.reduce(operator.mul, values)
            case 2: return min(values)
            case 3: return max(values)
            case 4: return self.literal
            case 5: return 1 if values[0] > values[1] else 0
            case 6: return 1 if values[0] < values[1] else 0
            case 7: return 1 if values[0] == values[1] else 0


class Transmission:
    def __init__(self, transmission: str) -> None:
        self.transmission = transmission
        self.bits = 0
        self.buffer = 0

    def take(self, n: int) -> int:
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
