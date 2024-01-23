import abc


class NotificationAlertObserver:
    @abc.abstractmethod
    def update(self):
        pass
