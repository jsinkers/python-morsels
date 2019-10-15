from dataclasses import dataclass


@dataclass
class PrintRange:
    start: int
    stop: int
    closed: bool

    def __str__(self):
        if self.start == self.stop:
            return f"{self.start}"
        else:
            return f"{self.start}-{self.stop}"


def format_ranges(nums):
    ranges = []
    nums = sorted(nums)

    for i, num in enumerate(nums):
        if i:
            set_flag = False
            ranges = sorted(ranges, key=lambda x: x.stop)
            for r in ranges:
                if not r.closed:
                    if num == r.stop + 1:
                        # Let's make this range bigger
                        r.stop = num
                        set_flag = True
                        break
                    elif num == r.stop:
                        # Check out the next open range
                        continue
                    else:
                        # This range isn't continuous.  Close it out
                        r.closed = True

            # We didn't change any ranges in the loop.  We need an extra range
            if not set_flag:
                ranges.append(PrintRange(num, num, False))
        else:
            # first time round, add a new range
            ranges.append(PrintRange(num, num, False))

    r_str = [str(r) for r in ranges]
    r_str = ','.join(r_str)
    return r_str
