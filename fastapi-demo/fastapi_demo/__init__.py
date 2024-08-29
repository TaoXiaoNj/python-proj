import logging

# global config setting
logging.basicConfig(format="{asctime} - {levelname}: {message}", 
                    style='{',
                    level=logging.INFO,
                    datefmt="%Y-%m-%d %H:%M:%S"
                    )