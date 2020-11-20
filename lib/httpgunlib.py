class Request:
    def __init__(self, request_id, name, user_agent):
        self.id = request_id
        self.name = name
        self.user_agent = user_agent


class UserAgent:
    def __init__(self, user_agent, op_sys, enabled, hardware, popularity):
        self.user_agent = user_agent
        self.OS = op_sys
        self.enabled = enabled
        self.hardware = hardware
        self.popularity = popularity

    def set_user_agent(self, user_agent):
        self.user_agent = user_agent
        return user_agent

    def set_opsys(self, op_sys):
        self.OS = op_sys
        return op_sys

    def set_enabled(self, enabled):
        self.enabled = enabled
        return enabled

    def set_hardware(self, hardware):
        self.hardware = hardware
        return hardware

    def set_popularity(self, popularity):
        self.popularity = popularity
        return popularity
