class IP:
    digits: int
    @staticmethod
    def from_ip(ip_str):
        if ip_str.count('.') == 3:
            self = IP()
            _digits = 0
            for index, item in enumerate(ip_str.split('.')):
                _digits += int(item) * (256**(3-index))
            self.digits = _digits
            return self
        else:
            raise ValueError("Invalid IP address")
    @staticmethod
    def from_digits(digits):
        self = IP()
        self.digits = digits
        return self
    @staticmethod
    def from_hex(hex_str):
        self = IP()
        self.digits = int(hex_str, 16)
        return self
    @staticmethod
    def from_bin(bin_str):
        self = IP()
        self.digits = int(bin_str, 2)
        return self
    @property
    def ip_str(self):
        return '.'.join(str(self.digits >> i & 0xff) for i in (24, 16, 8, 0))
    @property
    def ip_digits(self):
        return self.digits
    @property
    def ip_hex(self):
        return hex(self.digits)[2:].zfill(8).upper()
    @property
    def ip_bin(self):
        return bin(self.digits)[2:].zfill(32)