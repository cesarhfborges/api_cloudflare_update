class Imprimir:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def printWarning(self: str):
        """
        :argument self
        :rtype: void
        """
        print(Imprimir.WARNING + self + Imprimir.ENDC)


    def printSuccess(self: str):
        """
        :argument self
        :rtype: void
        """
        print(Imprimir.OKGREEN + self + Imprimir.ENDC)


    def printInfo(self: str):
        """
        :argument self
        :rtype: void
        """
        print(Imprimir.OKBLUE + self + Imprimir.ENDC)
