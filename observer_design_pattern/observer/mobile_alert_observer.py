from observer_design_pattern.observable.stock_observable import StocksObservableInterface
from observer_design_pattern.observer.notification_alert_observer import NotificationAlertObserver


class MobileAlertObserver(NotificationAlertObserver):
    def __init__(self, stock_observer: StocksObservableInterface, user_name: str):
        self.stock_observer = stock_observer
        self.user_name = user_name

    def update(self):
        self.send_msg_on_mobile(self.user_name)

    @staticmethod
    def send_msg_on_mobile(user_name: str):
        print("msg sent to" + user_name)
