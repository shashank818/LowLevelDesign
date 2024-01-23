from observer_design_pattern.observable.stock_observable import StocksObservableInterface
from observer_design_pattern.observer.notification_alert_observer import NotificationAlertObserver


class EmailAlertObserver(NotificationAlertObserver):
    def __init__(self, stock_observable: StocksObservableInterface, mail_id: str):
        self.stock_observable = stock_observable
        self.mail_id = mail_id

    def update(self):
        self.send_mail(self.mail_id)

    @staticmethod
    def send_mail(email_id: str):
        print("Mail sent to" + email_id)
