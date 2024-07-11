from typing import overload

__all__ = ['irange']

@overload
def irange(steps:int, span:tuple[int, int]) -> range: ...

@overload
def irange(steps:int) -> range: ...

def irange(steps:int, span:tuple[int, int] | None = None) -> range:
	"""An alternative formulation for ranges that is more intuitive(?) for one-indexed ranges
	
	Args:
		steps (int): The number of steps in the range
		span (tuple[int, int], optional): The start and stop of the range (inclusive). Defaults to (1, steps).
	"""
	if span is None:
		return range(1, steps + 1)
	start, stop = span
	assert (stop - start) % (steps - 1) == 0
	interval = (stop - start) // (steps - 1)
	return range(start, stop + 1, interval)