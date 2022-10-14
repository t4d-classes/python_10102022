""" patterns """

from typing import Callable


def console_log(msg: str) -> None:
    """ console log method """
    print(msg)


# unconstrained mocking/testing
# legacy code
def action_a() -> None:
    """ action a method """
    console_log("action a")


# constrained mocking/testing
# modern code
def action_b(log: Callable[..., None]) -> None:
    """ action b method """
    log("action b")
