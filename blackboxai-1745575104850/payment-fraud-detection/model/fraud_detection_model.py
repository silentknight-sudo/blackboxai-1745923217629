from datetime import datetime

class SimpleFraudDetector:
    def __init__(self):
        # Define rules for fraud detection
        self.amount_threshold = 1000
        self.suspicious_hours = set(range(0, 5))  # 12 AM to 4 AM
        self.max_daily_transactions = 10

    def predict(self, transaction):
        """
        Predict if a transaction is fraudulent based on simple rules
        Args:
            transaction: dict with keys 'amount', 'hour', 'n_transactions_day', 'country', 'type'
        Returns:
            dict with prediction details
        """
        risk_score = 0
        reasons = []

        # Check amount
        if transaction['amount'] > self.amount_threshold:
            risk_score += 40
            reasons.append(f"Amount (${transaction['amount']}) exceeds threshold (${self.amount_threshold})")

        # Check time of day
        if transaction['hour'] in self.suspicious_hours:
            risk_score += 30
            reasons.append(f"Transaction time ({transaction['hour']}:00) is during suspicious hours")

        # Check number of transactions
        if transaction['n_transactions_day'] > self.max_daily_transactions:
            risk_score += 30
            reasons.append(f"Number of transactions today ({transaction['n_transactions_day']}) exceeds limit ({self.max_daily_transactions})")

        # Determine risk level
        risk_level = 'High' if risk_score > 70 else 'Medium' if risk_score > 30 else 'Low'

        return {
            'is_fraud': risk_score > 70,
            'risk_score': risk_score,
            'risk_level': risk_level,
            'reasons': reasons,
            'timestamp': datetime.now().isoformat()
        }

    def get_rules_description(self):
        """Return the rules used for fraud detection"""
        return [
            f"Transactions over ${self.amount_threshold} are considered high risk",
            f"Transactions between 12 AM and 4 AM are considered suspicious",
            f"More than {self.max_daily_transactions} transactions per day is suspicious",
            "Risk score over 70 indicates potential fraud"
        ]

if __name__ == "__main__":
    print("This module provides the SimpleFraudDetector class for rule-based fraud detection.")
