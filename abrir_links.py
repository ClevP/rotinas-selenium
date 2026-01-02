from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import datetime

urls = [
    "https://mqv.institutodoalivio.com.br/Tasks/integracao_evo/rotina_integracao_allp.php",
    "https://mqv.institutodoalivio.com.br/Tasks/integracao_evo/rotina_prescricao_allp.php",
    "https://mqv.institutodoalivio.com.br/Tasks/integracao_pacto/rotina_integracao_pacto.php",
    "https://mqv.institutodoalivio.com.br/Tasks/integracao_pacto/rotina_prescricao_pacto.php",
    "https://mqv.institutodoalivio.com.br/Tasks/integracao_evo/rotina_prescricao2_allp.php",
    "https://mqv.institutodoalivio.com.br/Tasks/integracao_pacto/rotina_prescricao2_pacto.php"
]

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--log-level=3")

driver = webdriver.Edge(options=options)

print(f"Início da execução: {datetime.now()}")

for url in urls:
    driver.get(url)
    print(f"Executado: {url}")
    time.sleep(3)

driver.quit()

print(f"Fim da execução: {datetime.now()}")
