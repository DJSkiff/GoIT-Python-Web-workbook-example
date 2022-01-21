"""https://goit.global/python-material-dev/docs/module-16/lesson-16-01#:~:text=%D0%9D%D0%B5%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D0%BC%20%D0%BB%D0%BE%D0%B3%D0%B8%D1%80%D1%83%D0%B5%D0%BC%D1%83%D1%8E%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8E%3A"""

import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.DEBUG,
        handlers=[
        logging.FileHandler("program.log"),
        logging.StreamHandler()
    ])
logging.warning('An example message.')
logging.warning('Another message')