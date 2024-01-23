from observer_design_pattern.observable.stock_observable import StocksObservableInterface
from observer_design_pattern.observer.notification_alert_observer import NotificationAlertObserver


class IphoneAlertObservable(StocksObservableInterface):
    def __init__(self):
        self.observer_list = []
        self.stock_count = 0

    def add(self, observer: NotificationAlertObserver):
        self.observer_list.append(observer)

    def remove(self, observer: NotificationAlertObserver):
        self.observer_list.remove(observer)

    def notify_subscriber(self):
        for observer in self.observer_list:
            observer.update()

    def get_stock_count(self):
        return self.stock_count

    def set_stock_count(self, new_stock_added: int):
        if self.stock_count == 0:
            self.notify_subscriber()

        self.stock_count += new_stock_added
