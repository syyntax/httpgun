class Request:
    def __init__(self, obj_id, name=None, user_agent=None):
        self.id = int(obj_id)
        self.name = str(name)
        self.user_agent = user_agent


class UserAgent:
    def __init__(self, obj_id, name=None, op_sys=None, enabled=True, hardware=None, popularity=None):
        self.id = int(obj_id)
        self.name = str(name)
        self.OS = op_sys
        self.enabled = bool(enabled)
        self.hardware = hardware
        self.popularity = str(popularity)

    def set_id(self, obj_id):
        old = self.id
        self.id = int(obj_id)
        return f'ID: {old} --> {obj_id}'

    def set_name(self, name):
        old = self.name
        self.name = str(name)
        return f'User Agent: {old} --> {name}'

    def set_opsys(self, op_sys):
        old = self.OS
        self.OS = op_sys
        return f'OS: {old} --> {op_sys}'

    def set_enabled(self, enabled):
        if type(enabled) == bool:
            old = self.enabled
            self.enabled = enabled
            return f'Enabled: {old} --> {enabled}'

        else:
            raise Exception(f'Parameter {enabled} is not bool type.')

    def set_hardware(self, hardware):
        old = self.hardware
        self.hardware = hardware
        return f'Hardware: {old} --> {hardware}'

    def set_popularity(self, popularity):
        old = self.popularity
        self.popularity = popularity
        return f'Popularity: {old} --> {popularity}'
