# Quelle: https://www.zoho.com/crm/developer/docs/api/v3/oauth-overview.html
# Import den notwendigen Libraries
import requests
import json
import os

# Übertragung des aus Case-Aufgabenstellung angegebenen Refresh Tokens
refresh_token = ""

# Definition einer Funktion zur Generierung von Access- und Refreshtoken mithilfe des Grant Tokens (Funktion wird nicht benötigt, da durch Case-Aufgabenstellung der Refresh-Token zur Verfügung gestellt wurde)
'''def generate_access_refresh_tokens(grant_token):
    # Festlegen der Anmeldeinformationen des "Self-Clients", die für die Refresh- und Access Token-Generierung notwendig sind
    accounts_url = "https://accounts.zoho.eu"
    client_id = ""
    client_secret = ""
    redirect_uri = "https://api.einfach-zum-angebot.de/docs/authentication/"
    
    # Festlegen der URL für den POST-Request
    token_url = f"{accounts_url}/oauth/v2/token"
    
    # Festlegen der Daten für den POST-Request
    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "code": grant_token
    }
    
    # Senden des POST-Requests und Empfang der Response als JSON-Objekt
    response = requests.post(token_url, data=data)
    response_json = response.json()
    
    # Auslesen des Refresh- und Access Tokens aus der API-Response
    access_token = response_json["access_token"]
    refresh_token = response_json["refresh_token"]

    # Rückgabe des Refresh- und Access Tokens
    return access_token, refresh_token'''

# Definition einer Funktion zur Generierung eines neuen Access Tokens (Für den Fall, dass alter Access Token nach 1h abgelaufen ist)
def generate_new_access_token(refresh_token):
    # Festlegen der Anmeldeinformationen des "Self-Clients", die für die Access Token-Erneuerung notwendig sind
    accounts_url = "https://accounts.zoho.eu"
    client_id = ""
    client_secret = ""
    
    # Festlegen der URL für den POST-Request
    token_url = f"{accounts_url}/oauth/v2/token?refresh_token={refresh_token}&client_id={client_id}&client_secret={client_secret}&grant_type=refresh_token"

    # Senden des POST-Requests und Empfang der Response als JSON-Objekt
    response = requests.post(token_url)
    response_json = response.json()
    
    # Auslesen des aktualisierten Access Tokens aus der API-Response
    new_access_token = response_json["access_token"]
    
    # Rückgabe des aktualisierten Access Tokens
    return new_access_token

# Definition einer Funktion zur Abfrage von Marketing-Leads der https://einfach-zum-angebot.de/ Webseite sowie der Übertragung der Leads in das ZOHO CRM System
def create_leads(access_token):
    # Festelgen der URL, von der die Marketing-Leads des Typs "Immobilie" abgerufen werden sollen (Imaginär, da kein Autorisierungstoken für die API zur Verfügung gestellt wurde)
    leads_url = "https://api.einfach-zum-angebot.de/leads?type=IMMOBILIE"
    
    # Festlegen des Autorisierungstokens der https://einfach-zum-angebot.de/- Webseite (Imaginär, da kein Autorisierungstoken für die API zur Verfügung gestellt wurde)
    headers = {"Authorization": "1234567890"}
    
    # Senden des GET-Requests und Empfang der Response als JSON-Objekt
    #response = requests.get(leads_url, headers=headers)
    #response_json = response.json()

    # Erstellung einer imaginären Response, die so aufgebaut ist, wie die Response der API Schnittstelle 
    fake_response = {"data": {
    "id": 135861,
    "contact_firstname": "Max",
    "contact_name": "Mustermann",
    "contact_street": "Weißenseestraße 101",
    "contact_zip": "81539",
    "contact_city": "München",
    "contact_email": "test@ajaska.de",
    "contact_tel": "00000000000",
    "contact_mobile": "11111111111",
    "contact_gender": "MALE",
    "lead_type": "IMMOBILIE",
    "comment_extern": "Test Kommentar für Anbieter",
    "sent_at": "2022-03-09 11:05:04",
    "lead_data": [
      {"data_key": "type",
        "data_value": "Haus"},
      {"data_key": "haus_flaeche_grund",
        "data_value": "500"},
      { "data_key": "haus_flaeche_wohn",
        "data_value": "100"},
      {"data_key": "haus_etagenanzahl",
        "data_value": "1,5"},
      {"data_key": "haus_anzahl_zimmer",
        "data_value": "5"},
      {"data_key": "haus_baujahr",
        "data_value": "1980"},
      {"data_key": "interesse",
        "data_value": "Verkauf"},
      {"data_key": "teilverkauf",
        "data_value": "Telefonische Beratung"},
      {"data_key": "verkaufszeitpunkt",
        "data_value": "Innerhalb 6 Monaten"},
      {"data_key": "firma",
        "data_value": ""},
      {"data_key": "contact_mobile",
        "data_value": ""},
      {"data_key": "termin_erwuenscht",
        "data_value": "Ja"},
      {"data_key": "verkauf_erwuenscht",
        "data_value": "Ja"},
      {"data_key": "verkaufszeitpunkt_abfrage",
        "data_value": "Innerhalb 6 Monate"},
      {"data_key": "ist_eigentuemer",
        "data_value": "Ja"},
      {"data_key": "makler_vorhanden",
        "data_value": "Nein"}]}}

    # Transformation der hartcodierten Response in ein JSON-Objekt
    fake_response_json = json.loads(json.dumps(fake_response))
    
    # Auslesen der Lead-Informationen aus der Response und Übertragung in das von ZOHO CRM erforderliche Format
    lead_data = {
    "Company": "https://einfach-zum-angebot.de/",
    "Email": fake_response_json["data"]["contact_email"],
    "Street": fake_response_json["data"]["contact_street"],
    "Zip_Code": fake_response_json["data"]["contact_zip"],
    "id": fake_response_json["data"]["id"],
    "Data_Source": "API",
    "City": fake_response_json["data"]["contact_city"],
    "First_Name": fake_response_json["data"]["contact_firstname"],
    "Lead_Status": "New Lead",
    "Phone": fake_response_json["data"]["contact_tel"],
    "Mobile": fake_response_json["data"]["contact_mobile"],
    "Last_Name": fake_response_json["data"]["contact_name"],
    "Lead_Source": "Partner"}
    record_list = list()
    record_list.append(lead_data)
    request_body = dict()
    request_body['data'] = record_list

    # URL für die Erstellung von Leads in ZOHO
    # Festelgen der ZOHO CRM URL, an die Marketing-Leads versendet werden soll
    zoho_url = "https://www.zohoapis.eu/crm/v2/Leads"
    
    # Festelegen des Access Tokens, der durch die Funktion "generate_new_access_token" erstellt wurde
    zoho_headers = {"Authorization": f"Zoho-oauthtoken {access_token}"}

    # Festlegen der Aktivität, die im ZOHO CRM System durchgeführt werden soll -> In diesem Fall die "Erstellung" neuer Leads
    parameters = {"scope": "ZohoCRM.modules.leads.CREATE"}
    
    # Senden des POST-Requests
    zoho_response = requests.post(zoho_url, headers=zoho_headers, params=parameters, data=json.dumps(request_body))
    
    # Überprüfung ob die Anfrage erfolgreich war
    if zoho_response.ok:
        print("Lead created successfully!")
        print(zoho_response.json())
    else:
        print(f"Failed to create lead: {zoho_response.status_code} - {zoho_response.text}")

# Main Funktion, die die zuvor erstellen Funktionen aggregiert
def main(refresh_token):
    new_access_token = generate_new_access_token(refresh_token)
    create_leads(new_access_token)

# Aufrufen der Main Funktion
main(refresh_token)

# Benachrichtigung die unter MacOS angezeigt wird, sobald das main.py Skript erfolgreich ausgeführt wurde -> Anleitung für die Festlegung der täglichen Ausführung des Skripts via Cronjobs unter https://github.com/lukas-bst/1K5-Case
os.system('osascript -e \'display notification "ZOHO Lead Skript wurde erfolgreich ausgeführt." with title "Skript"\'')