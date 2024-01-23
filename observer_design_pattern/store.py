from observer_design_pattern.observable.iphone_observable_impl import IphoneAlertObservable
from observer_design_pattern.observer.email_alert_observer import EmailAlertObserver
from observer_design_pattern.observer.mobile_alert_observer import MobileAlertObserver


if __name__ == "__main__":
    iphone_observable = IphoneAlertObservable()

    observer1 = EmailAlertObserver(iphone_observable, "mauryashashank000@gmail.com")
    observer2 = EmailAlertObserver(iphone_observable, "vikasshashank7@gmail.com")
    observer3 = MobileAlertObserver(iphone_observable, "shashank_maurya")

    iphone_observable.add(observer2)
    iphone_observable.add(observer1)
    iphone_observable.add(observer3)
    iphone_observable.set_stock_count(10)

