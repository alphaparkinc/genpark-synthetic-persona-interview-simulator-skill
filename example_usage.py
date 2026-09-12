from client import SyntheticPersonaInterviewSimulatorClient

def main():
    client = SyntheticPersonaInterviewSimulatorClient()
    res = client.simulate_persona_focus_group()
    print('Persona Interview Simulator: ' + res['interview_session_id'])
    print('Composite Sentiment: ' + str(res['composite_market_sentiment']) + ' across ' + str(res['simulated_personas_count']) + ' personas')
    print('Purchase Drivers: ' + str(res['primary_purchase_drivers']))
    for fb in res['persona_feedback_matrix']:
        print('  - ' + fb['persona'] + ' (Sentiment: ' + str(fb['sentiment_score']) + '): ' + fb['key_objection'])
    print('Dossier URL: ' + res['interview_dossier_url'])

if __name__ == '__main__':
    main()
