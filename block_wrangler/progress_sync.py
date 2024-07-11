from typing import Iterable
from rich.progress import Progress, TaskID


class ProgressSync[T]:
	"""An iterator wrapper that updates one or more progress bars at the same time as iterating"""
	def __init__(self, wrapped:Iterable[T], progress:Progress, *tasks:TaskID, step:int=1):
		self._wrapped = iter(wrapped)
		self._progress = progress
		self._tasks = tasks
		self._step = step
	
	def __iter__(self):
		return self
	
	def __next__(self):
		ret = next(self._wrapped)
		for task in self._tasks:
			self._progress.update(task, advance=self._step)
		return ret