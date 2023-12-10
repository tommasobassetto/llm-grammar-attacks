class BaseInterface:
    def getToken(self) -> None:
        pass

    def call(self, query: str) -> str:
        pass

    def callInNewChat(self, query: str) -> str:
        pass