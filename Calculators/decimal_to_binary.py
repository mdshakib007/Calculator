class Binary:
    """Convert decimal to binary"""
    def __init__(self):
        self.n = int(input("Enter decimal number: "))

    def dec_to_binary(self):
        bits = []
        n = self.n
        if n == 0:
            return "The binary number: 0"

        while n > 0:
            bits.append(n % 2)
            n = n // 2

        bits.reverse()

        binary = ""
        for bit in bits:
            binary += str(bit)

        return f"The binary number: {binary}"

if __name__ == "__main__":
	b = Binary()
	print(b.dec_to_binary())