class ApplicationState:
    instance = None

    def __init__(self):
        self.is_logged_in = False

    @staticmethod
    def get_app_state():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance


appstate1 = ApplicationState().get_app_state()
print(appstate1.is_logged_in)
appstate1.is_logged_in = True

print(appstate1.is_logged_in)
appstate2 = ApplicationState().get_app_state()
print(appstate2.is_logged_in)

print(appstate2 == appstate1)



