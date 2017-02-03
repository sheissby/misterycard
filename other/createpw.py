# encoding: utf-8
import string, random
def createPassword():
    '''随机生成密码，包含大小写及数字'''
    try:
        length = input('lenth of password:')
    except Exception: return createPassword()
    seedlower = string.lowercase
    # seeddigit = string.digits
    seedupper = string.uppercase
    pwdd = pwdl = pwdu = ''

    countl = random.randint(1, length-2)
    countu = random.randint(1, length-countl-1)
    countd = (length-countl-countu)

    # 生成随机的字符
    for l in range(countl):
        a = random.choice(seedlower)
        pwdl += a
    for u in range(countu):
        b= random.choice(seedupper)
        pwdu += b
    for d in range(countd):
        c = random.randint(0, 9)
        pwdd += str(c)

    # 在随机位置出现随机的字符
    seed = pwdl+pwdu+pwdd
    shuffler = random.sample(seed, len(seed))
    pwd = "".join(shuffler)
    print pwd

if __name__ == '__main__':
    createPassword()
