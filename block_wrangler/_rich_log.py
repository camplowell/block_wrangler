import logging

from typing import TYPE_CHECKING, Mapping, cast

class RichLogger(logging.Logger):
	VERBOSE = (logging.INFO + logging.DEBUG) // 2
	if TYPE_CHECKING:
		def verbose(
			self, msg: object,
			*args: object,
			exc_info: logging._ExcInfoType = None,
			stack_info: bool = False,
			stacklevel: int = 1,
			extra: Mapping[str, object] | None = None
		) -> None:
			pass
	else:
		def verbose(self, msg: object, *args, **kwargs):
			if self.isEnabledFor(self.VERBOSE):
				self._log(
					self.VERBOSE, 
					msg, 
					args, 
					**kwargs
				)

logging.addLevelName(RichLogger.VERBOSE, "VERBOSE")
logging.setLoggerClass(RichLogger)

FORMAT = "%(message)s"

try:
    from rich.logging import RichHandler
    logging.basicConfig(
        format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
    )
except ImportError: pass

def getLogger(name:str | None = 'block_wrangler'):
	"""Return a logger with the specified name, creating it if necessary.

	If no name is specified, return the root logger."""
	ret = logging.getLogger(name)
	if not isinstance(ret, RichLogger):
		ret.error(f'{name} not a rich logger?!')
		ret.__class__ = RichLogger
	return cast(RichLogger, ret)

__all__ = ['getLogger']
