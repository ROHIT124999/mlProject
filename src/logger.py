import logging
import os
from datetime import datetime
LOG_FiLE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs", LOG_FiLE)
os.makedirs(logs_path,exist_ok=True)

LOG_FiLE_Path = os.path.join(logs_path,LOG_FiLE)

logging.basicConfig(
    filename= LOG_FiLE_Path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)


if __name__=="__main__":
    logging.info("logging has started")
