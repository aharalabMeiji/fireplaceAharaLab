import logging


def get_logger(name, level=logging.DEBUG):
	logger = logging.getLogger(name)
	logger.setLevel(level)

	if not logger.handlers:
		ch = logging.StreamHandler()
		ch.setLevel(level)

		formatter = logging.Formatter(
			"[%(name)s.%(module)s]: %(message)s",
			datefmt="%H:%M:%S"
		)
		ch.setFormatter(formatter)

<<<<<<< HEAD
		# logger.addHandler(ch)
=======
		#logger.addHandler(ch)
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375

	return logger


log = get_logger("fireplace")
