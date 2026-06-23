import logging

logging.basicConfig(
    filename='sauvegarde.log',
    level=logging.INFO,                       
    format='%(asctime)s - %(levelname)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'               
)


logging.info("Le système de log fonctionne parfaitement !")
