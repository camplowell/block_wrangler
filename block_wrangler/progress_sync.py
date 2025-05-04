from __future__ import annotations
from typing import Iterable, TYPE_CHECKING, Iterator

if TYPE_CHECKING:
	from rich.progress import Progress, TaskID

class DummyTaskID: pass

class DummyProgress:
	def __init__(self, *args, **kwargs): pass
	
	def __enter__(self):
		return self

	def __exit__(self, *args, **kwargs):
		pass
	
	if TYPE_CHECKING:
		def add_task(self, *args, **kwargs) -> 'TaskID': ...
	else:
		def add_task(self, *args, **kwargs): return DummyTaskID()
		
	def update(self, *args, **kwargs): pass
	def remove_task(self, task): pass


class ProgressSync[T](Iterator[T]):
	"""An iterator wrapper that updates one or more progress bars at the same time as iterating"""
	def __init__(self, wrapped:Iterable[T], progress:Progress|DummyProgress, *tasks:TaskID|DummyTaskID, step:int=1):
		self._wrapped = iter(wrapped)
		self._progress = progress
		self._tasks = [task for task in tasks if not isinstance(task, DummyTaskID)]
		self._step = step
		
		if isinstance(progress, DummyProgress):
			def __next__(): return next(self._wrapped)
			self.__next__ = __next__
	
	def __next__(self):
		ret = next(self._wrapped)
		for task in self._tasks:
			self._progress.update(task, advance=self._step)
		return ret
