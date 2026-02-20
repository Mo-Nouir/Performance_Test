from locust import HttpUser, task, between
import random
from datetime import datetime, timedelta

def random_amount(min_val=10, max_val=1000):
    return round(random.uniform(min_val, max_val), 2)

def random_datetime():
    return (datetime.now() + timedelta(days=random.randint(0, 30))).isoformat()

class PaymentUser(HttpUser):
    wait_time = between(1, 5)

    # Task 1: Transfer money
    @task(8)
    def transfer_money(self):
        payload = {
            "from_account": f"ACC{random.randint(1000,9999)}",
            "to_account": f"ACC{random.randint(1000,9999)}",
            "amount": random_amount(),
            "currency": "USD",
            "description": "One-time transfer",
            "scheduled_date": random_datetime(),
            "recurring": {
                "enabled": False,
                "frequency": None,
                "end_date": None
            }
        }
        self.client.post("/api/v1/transfers", json=payload)

    # Task 2: Schedule recurring transfer
    @task(2)
    def schedule_recurring_transfer(self):
        payload = {
            "from_account": f"ACC{random.randint(1000,9999)}",
            "to_account": f"ACC{random.randint(1000,9999)}",
            "amount": random_amount(),
            "currency": "USD",
            "description": "Recurring transfer",
            "scheduled_date": random_datetime(),
            "recurring": {
                "enabled": True,
                "frequency": random.choice(["daily", "weekly", "monthly"]),
                "end_date": random_datetime()
            }
        }
        self.client.post("/api/v1/transfers", json=payload)

