import logging

def setup_logger(name="MedicalAssistant"):

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] --- [%(message)s]')
    ch.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(ch)

    return logger

logger = setup_logger()

logger.info("RAG Process started.")
logger.debug("Debugging information for RAG Process.")
logger.warning("This is a warning message for RAG Process.")
logger.error("An error occurred in RAG Process.")
logger.critical("Critical issue in RAG Process.")