import abc
from observer_design_pattern.observer.notification_alert_observer import NotificationAlertObserver


class StocksObservableInterface:
    @abc.abstractmethod
    def add(self, notification_alert_observer: NotificationAlertObserver):
        pass

    @abc.abstractmethod
    def remove(self, notification_alert_observer: NotificationAlertObserver):
        pass

    @abc.abstractmethod
    def notify_subscriber(self):
        pass

    @abc.abstractmethod
    def get_stock_count(self):
        pass
