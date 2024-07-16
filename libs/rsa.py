class RSA(object):
    def generateKeys(self, keyByte):
        key = [0] * 56
        loop = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        keys = []
        for i in range(16):
            keys.append([0] * 48)

        for i in range(7):
            k = 7
            for j in range(8):
                key[i * 8 + j] = keyByte[8 * k + i]
                k -= 1
        for i in range(16):
            tempLeft = 0
            tempRight = 0
            for j in range(loop[i]):
                tempLeft = key[0]
                tempRight = key[28]
                for k in range(27):
                    key[k] = key[k + 1]
                    key[28 + k] = key[29 + k]
                key[27] = tempLeft
                key[55] = tempRight
            tempKey = []
            tempKey.append(key[13])
            tempKey.append(key[16])
            tempKey.append(key[10])
            tempKey.append(key[23])
            tempKey.append(key[0])
            tempKey.append(key[4])
            tempKey.append(key[2])
            tempKey.append(key[27])
            tempKey.append(key[14])
            tempKey.append(key[5])
            tempKey.append(key[20])
            tempKey.append(key[9])
            tempKey.append(key[22])
            tempKey.append(key[18])
            tempKey.append(key[11])
            tempKey.append(key[3])
            tempKey.append(key[25])
            tempKey.append(key[7])
            tempKey.append(key[15])
            tempKey.append(key[6])
            tempKey.append(key[26])
            tempKey.append(key[19])
            tempKey.append(key[12])
            tempKey.append(key[1])
            tempKey.append(key[40])
            tempKey.append(key[51])
            tempKey.append(key[30])
            tempKey.append(key[36])
            tempKey.append(key[46])
            tempKey.append(key[54])
            tempKey.append(key[29])
            tempKey.append(key[39])
            tempKey.append(key[50])
            tempKey.append(key[44])
            tempKey.append(key[32])
            tempKey.append(key[47])
            tempKey.append(key[43])
            tempKey.append(key[48])
            tempKey.append(key[38])
            tempKey.append(key[55])
            tempKey.append(key[33])
            tempKey.append(key[52])
            tempKey.append(key[45])
            tempKey.append(key[41])
            tempKey.append(key[49])
            tempKey.append(key[35])
            tempKey.append(key[28])
            tempKey.append(key[31])

            for m in range(48):
                keys[i][m] = tempKey[m]
        return keys

    def initPermute(self, originalData):
        m = 1
        n = 0
        ipByte = [0] * 64
        for i in range(4):
            j = 7
            k = 0
            while j >= 0:
                ipByte[i * 8 + k] = originalData[j * 8 + m]
                ipByte[i * 8 + k + 32] = originalData[j * 8 + n]
                k += 1
                j -= 1
            m += 2
            n += 2
        return ipByte

    def xor(self, byteOne, byteTwo):
        xorByte = []
        for i in range(len(byteOne)):
            xorByte.append(byteOne[i] ^ byteTwo[i])
        return xorByte

    def bin_test(self, s):
        binary = bin(s).replace('0b', '')
        binary = binary[::-1]
        if len(binary) < 4:
            for i in range(4 - len(binary)):
                binary += '0'
        binary = binary[::-1]
        return binary

    def sBoxPermute(self, expandByte):
        sBoxByte = [0] * 32
        binary = ""
        s1 = [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ]
        s2 = [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ]
        s3 = [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ]
        s4 = [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ]
        s5 = [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ]
        s6 = [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ]
        s7 = [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ]
        s8 = [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
        for m in range(8):
            i = 0
            j = 0
            i = expandByte[m * 6 + 0] * 2 + expandByte[m * 6 + 5]
            j = expandByte[m * 6 + 1] * 2 * 2 * 2 + expandByte[m * 6 + 2] * 2 * 2 + expandByte[m * 6 + 3] * 2 + \
                expandByte[
                    m * 6 + 4]

            if m == 0:
                binary = self.bin_test(s1[i][j])
            elif m == 1:
                binary = self.bin_test(s2[i][j])
            elif m == 2:
                binary = self.bin_test(s3[i][j])
            elif m == 3:
                binary = self.bin_test(s4[i][j])
            elif m == 4:
                binary = self.bin_test(s5[i][j])
            elif m == 5:
                binary = self.bin_test(s6[i][j])
            elif m == 6:
                binary = self.bin_test(s7[i][j])
            elif m == 7:
                binary = self.bin_test(s8[i][j])

            sBoxByte[m * 4 + 0] = int(binary[0])
            sBoxByte[m * 4 + 1] = int(binary[1])
            sBoxByte[m * 4 + 2] = int(binary[2])
            sBoxByte[m * 4 + 3] = int(binary[3])
        return sBoxByte

    def pPermute(self, sBoxByte):
        pBoxPermute = []
        pBoxPermute.append(sBoxByte[15])
        pBoxPermute.append(sBoxByte[6])
        pBoxPermute.append(sBoxByte[19])
        pBoxPermute.append(sBoxByte[20])
        pBoxPermute.append(sBoxByte[28])
        pBoxPermute.append(sBoxByte[11])
        pBoxPermute.append(sBoxByte[27])
        pBoxPermute.append(sBoxByte[16])
        pBoxPermute.append(sBoxByte[0])
        pBoxPermute.append(sBoxByte[14])
        pBoxPermute.append(sBoxByte[22])
        pBoxPermute.append(sBoxByte[25])
        pBoxPermute.append(sBoxByte[4])
        pBoxPermute.append(sBoxByte[17])
        pBoxPermute.append(sBoxByte[30])
        pBoxPermute.append(sBoxByte[9])
        pBoxPermute.append(sBoxByte[1])
        pBoxPermute.append(sBoxByte[7])
        pBoxPermute.append(sBoxByte[23])
        pBoxPermute.append(sBoxByte[13])
        pBoxPermute.append(sBoxByte[31])
        pBoxPermute.append(sBoxByte[26])
        pBoxPermute.append(sBoxByte[2])
        pBoxPermute.append(sBoxByte[8])
        pBoxPermute.append(sBoxByte[18])
        pBoxPermute.append(sBoxByte[12])
        pBoxPermute.append(sBoxByte[29])
        pBoxPermute.append(sBoxByte[5])
        pBoxPermute.append(sBoxByte[21])
        pBoxPermute.append(sBoxByte[10])
        pBoxPermute.append(sBoxByte[3])
        pBoxPermute.append(sBoxByte[24])
        return pBoxPermute

    def expandPermute(self, rightData):
        epByte = [0] * 48
        for i in range(8):
            if i == 0:
                epByte[i * 6 + 0] = rightData[31]
            else:
                epByte[i * 6 + 0] = rightData[i * 4 - 1]

            epByte[i * 6 + 1] = rightData[i * 4 + 0]
            epByte[i * 6 + 2] = rightData[i * 4 + 1]
            epByte[i * 6 + 3] = rightData[i * 4 + 2]
            epByte[i * 6 + 4] = rightData[i * 4 + 3]
            if i == 7:
                epByte[i * 6 + 5] = rightData[0]
            else:
                epByte[i * 6 + 5] = rightData[i * 4 + 4]
        return epByte

    def finallyPermute(self, endByte):
        fpByte = []
        fpByte.append(endByte[39])
        fpByte.append(endByte[7])
        fpByte.append(endByte[47])
        fpByte.append(endByte[15])
        fpByte.append(endByte[55])
        fpByte.append(endByte[23])
        fpByte.append(endByte[63])
        fpByte.append(endByte[31])
        fpByte.append(endByte[38])
        fpByte.append(endByte[6])
        fpByte.append(endByte[46])
        fpByte.append(endByte[14])
        fpByte.append(endByte[54])
        fpByte.append(endByte[22])
        fpByte.append(endByte[62])
        fpByte.append(endByte[30])
        fpByte.append(endByte[37])
        fpByte.append(endByte[5])
        fpByte.append(endByte[45])
        fpByte.append(endByte[13])
        fpByte.append(endByte[53])
        fpByte.append(endByte[21])
        fpByte.append(endByte[61])
        fpByte.append(endByte[29])
        fpByte.append(endByte[36])
        fpByte.append(endByte[4])
        fpByte.append(endByte[44])
        fpByte.append(endByte[12])
        fpByte.append(endByte[52])
        fpByte.append(endByte[20])
        fpByte.append(endByte[60])
        fpByte.append(endByte[28])
        fpByte.append(endByte[35])
        fpByte.append(endByte[3])
        fpByte.append(endByte[43])
        fpByte.append(endByte[11])
        fpByte.append(endByte[51])
        fpByte.append(endByte[19])
        fpByte.append(endByte[59])
        fpByte.append(endByte[27])
        fpByte.append(endByte[34])
        fpByte.append(endByte[2])
        fpByte.append(endByte[42])
        fpByte.append(endByte[10])
        fpByte.append(endByte[50])
        fpByte.append(endByte[18])
        fpByte.append(endByte[58])
        fpByte.append(endByte[26])
        fpByte.append(endByte[33])
        fpByte.append(endByte[1])
        fpByte.append(endByte[41])
        fpByte.append(endByte[9])
        fpByte.append(endByte[49])
        fpByte.append(endByte[17])
        fpByte.append(endByte[57])
        fpByte.append(endByte[25])
        fpByte.append(endByte[32])
        fpByte.append(endByte[0])
        fpByte.append(endByte[40])
        fpByte.append(endByte[8])
        fpByte.append(endByte[48])
        fpByte.append(endByte[16])
        fpByte.append(endByte[56])
        fpByte.append(endByte[24])
        return fpByte

    def enc(self, dataByte, keyByte):
        keys = self.generateKeys(keyByte)
        ipByte = self.initPermute(dataByte)
        ipLeft = []  # 32
        ipRight = []  # 32
        tempLeft = [0] * 32  # 32

        for k in range(32):
            ipLeft.append(ipByte[k])
            ipRight.append(ipByte[32 + k])
        for i in range(16):
            for j in range(32):
                tempLeft[j] = ipLeft[j]
                ipLeft[j] = ipRight[j]
            key = []
            for m in range(48):
                key.append(keys[i][m])
            tempRight = self.xor(self.pPermute(self.sBoxPermute(self.xor(self.expandPermute(ipRight), key))), tempLeft)
            for n in range(32):
                ipRight[n] = tempRight[n]
        finalData = [0] * 64
        for i in range(32):
            finalData[i] = ipRight[i]
            finalData[32 + i] = ipLeft[i]
        return self.finallyPermute(finalData)

    def bin2hex(self, byteData):
        hex = ""
        for i in range(16):
            bt = ""
            for j in range(4):
                bt += str(byteData[i * 4 + j])
            hex += format(int(bt, 2), 'x')

        return hex

    def str_to_16bin(self, s):
        ans = []
        for st in s:
            bt = ''.join([bin(ord(c)).replace('0b', '') for c in st])
            btArry = []
            i = 0
            while i < 16:
                if i < (16 - len(bt)):
                    btArry.append(0)
                    i += 1
                else:
                    for val in bt:
                        btArry.append(int(val))
                        i += 1
            ans += btArry
        if len(s) == 1:
            for i in range(48):
                ans.append(0)
        elif len(s) == 2:
            for i in range(32):
                ans.append(0)
        elif len(s) == 3:
            for i in range(16):
                ans.append(0)
        return ans

    def strEnc(self, data):
        encData = ""
        firstKey = '1'
        secondKey = '2'
        thirdKey = '3'
        firstKeyBt = self.str_to_16bin(firstKey)
        secondKeyBt = self.str_to_16bin(secondKey)
        thirdKeyBt = self.str_to_16bin(thirdKey)

        leng = len(data)
        irator = int(leng / 4)
        remainder = leng % 4
        for i in range(irator):
            tempData = data[i * 4 + 0:i * 4 + 4]
            tempBtyte = self.str_to_16bin(tempData)

            tempBt = tempBtyte

            tempBt = self.enc(tempBt, firstKeyBt)
            tempBt = self.enc(tempBt, secondKeyBt)
            tempBt = self.enc(tempBt, thirdKeyBt)

            encByte = tempBt
            encData += self.bin2hex(encByte)
        if remainder > 0:
            remainderData = data[irator * 4 + 0:leng]
            tempByte = []
            if leng <= 4:
                tempByte = self.str_to_16bin(remainderData)
            else:
                tempByte = self.str_to_16bin(remainderData[0:4])

            tempBt = tempByte
            tempBt = self.enc(tempBt, firstKeyBt)
            tempBt = self.enc(tempBt, secondKeyBt)
            tempBt = self.enc(tempBt, thirdKeyBt)
            encByte = tempBt
            encData += self.bin2hex(encByte)
        return encData.upper()
