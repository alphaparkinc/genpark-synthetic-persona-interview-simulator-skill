class SyntheticPersonaInterviewSimulatorClient:
    def simulate_persona_focus_group(self, product_offering='Roborock S8 MaxV Ultra with robotic arm side brush for $1599', persona_archetypes=['Cost-Conscious Suburban Parent', 'Tech-Early-Adopter Engineer', 'Luxury Minimalist']):
        panel_feedback = [
            {'persona': persona_archetypes[0], 'sentiment_score': 0.65, 'key_objection': 'Price point above $1500 is difficult to justify without seasonal bundle promotion'},
            {'persona': persona_archetypes[1], 'sentiment_score': 0.95, 'key_objection': 'Would like Matter / Home Assistant local API documentation upfront'},
            {'persona': persona_archetypes[2], 'sentiment_score': 0.88, 'key_objection': 'Base station footprint must match neutral interior aesthetics'}
        ]
        avg_sentiment = round(sum(f['sentiment_score'] for f in panel_feedback) / len(panel_feedback), 3)
        return {
            'interview_session_id': 'foc_sim_6619',
            'product_offering': product_offering,
            'simulated_personas_count': len(persona_archetypes),
            'composite_market_sentiment': avg_sentiment,
            'primary_purchase_drivers': ['Corner cleaning robotic arm', 'Auto detergent dispensing', 'Obstacle avoidance vision AI'],
            'persona_feedback_matrix': panel_feedback,
            'interview_dossier_url': 'https://feedback.persona.genpark.ai/sessions/6619.json'
        }
