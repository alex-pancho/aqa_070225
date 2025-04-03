import logging


logging.basicConfig(
    filename="hello.log",
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
if __name__ == "__main__":
    logging.debug("debug")
    logging.info("info")
    logging.error("error")
    logging.critical("critical")