#!/usr/bin/env python3
import itertools
import string
import gnupg
import time
import threading
import argparse

class BruteForcer:
    """ Class use to bruteforce gpg passphrase """
    def __init__(self, fileName: str, numThreads: int) -> None:
        self.fileName = fileName
        self.numThreads = numThreads
        self.threads = []
        self.passwordLock = threading.Lock()
        self.passwordFound = False
        self.__password = None
        self.__totalTime = None
        self.__result = b''

    @property
    def password(self):
        return self.__password

    @property
    def totalTime(self):
        return self.__totalTime

    @property
    def resultingData(self):
        return self.__result

    def __listSpliter(self,combinations: list):
        """Method used to split the work of the threads"""
        tamannoSublista = len(combinations) // (self.numThreads)
        sublist = [combinations[i:i + tamannoSublista] for i in range(0, len(combinations), tamannoSublista)]
        return sublist

    def __createCombinations(self, length: int) ->list:
        """Create all the combinations with the length given"""
        characters = string.ascii_lowercase
        combinations = [''.join(combination) for combination in itertools.product(characters, repeat=length)]
        return combinations

    def __threadWord(self, id: int, combinations: list, data):
        """Method that delegated to the thread to try passphrase"""
        i = 0
        gpg = gnupg.GPG()

        for password in combinations:
            result = gpg.decrypt(data, passphrase=password)
            i = i + 1
            if result.ok:
                self.passwordLock.acquire()
                self.passwordFound = True
                self.__password = password
                self.__result = result.data
                self.passwordLock.release()
                break
            if self.passwordFound: break
            print(f'{password} id: {id} it : {i}')
            

    def bruteForce(self):
        """Method used to initizalize the threads work"""
        with open(self.fileName, "rb") as f:
            data = f.read()

        lenght = 1
        t1 = time.time()
        while not self.passwordFound:
            combinatios = self.__createCombinations(lenght)
            sublist = self.__listSpliter(combinatios)
            combinatios.clear()

            for i in range(0, self.numThreads):
                self.threads.append(threading.Thread(target=self.__threadWord, args=(i, sublist[i], data)))

            for i in range(0, self.numThreads): self.threads[i].start()

            for i in range(0, self.numThreads): self.threads[i].join()

            sublist.clear()
            self.threads.clear()
            lenght = lenght + 1
        t2 = time.time()

        self.__totalTime = t2 - t1

def main():
    """Main method"""
    executionOptions = parseComandLine()
    result = BruteForcer(executionOptions.fileName, executionOptions.threads)
    result.bruteForce()
    print(f'Password found : {result.password} total execution time : {result.totalTime}')
    with open(executionOptions.output, "wb") as f:
        f.write(result.resultingData)

def parseComandLine():
    """Method used to parse the comand line"""
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        '-f', '--fileName', type=str, default = None,
        help='gpg file to brute force', dest='fileName'
    )

    parser.add_argument(
        '-t' '--threads', type=int, default=10,
        help='set the number of threads', dest='threads'
    )

    parser.add_argument(
        '-o', '--outputFile', type=str, default='solution',
        help='output file of the dara decrypted', dest='output'
    )

    return parser.parse_args()

if __name__ == '__main__':
    main()
