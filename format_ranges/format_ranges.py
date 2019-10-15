from dataclasses import dataclass


@dataclass
class PrintRange:
    start: int
    stop: int

    def __str__(self):
        return f"{self.start}-{self.stop}"


def format_ranges(nums):
    r = []
    for i, num in enumerate(nums):
        if i:
            if num == r[-1].stop + 1:
                r[-1].stop = num
            else:
                r.append(PrintRange(num, num))
        else:
            r.append(PrintRange(num, num))

    r_str = [str(rng) for rng in r]
    r_str = ','.join(r_str)
    return r_str
