import requests
import time

VIRUSTOTAL_TOKEN = "YOUR TOKEN"
base_virustotal_url = "https://www.virustotal.com/api/v3/files/"



def analyze_virustotal(hash: str) -> str:
    api_url = base_virustotal_url + hash
    header = {'X-Apikey': VIRUSTOTAL_TOKEN}
    response = requests.get(api_url, headers=header)
    time.sleep(16)

    if response.status_code == 200:
        if(response.json()['data']['attributes']['last_analysis_results']['TrendMicro']['result']):
            return response.json()['data']['attributes']['last_analysis_results']['TrendMicro']['result']
    return "not walware / zero day"