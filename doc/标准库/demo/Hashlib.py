# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 18:13
# @Author  : Marko Li 'lxh800109@gmail.com'
# @Site    : 
# @File    : Hashlib.py
# @Software: PyCharm
# __create_data__=2020/6/3 18:13
# @Description: add Description

import hashlib
import secrets


def main():
    s = hashlib.sha256()  # 创建一个sha256对象
    s.update(b"Nobody inspects")  # 使用该方法想对象传入字节类对象。可以多次调用update方法
    print(s.digest())  # 使用gidest或者是hexdigest获得到目前为止输入这个对象的拼接数据的digest
    # 如上，可以使用如下更简要的写法替代：
    print(hashlib.sha224(b"abcde").hexdigest())

    # 使用hashlib.new(namep,[data) name可以为任意的已经存在的算法名，而同名的更快，因此优先使用同名的构造器
    # 而如果没有提供，则使用该方法创建，比如OpenSSL中的算法
    h = hashlib.new('ripemd160', b"123456saf")
    print(h.hexdigest())
    print('集合：所以平台上都保证支持的哈希算法的名称,该集合为available的子集--', hashlib.algorithms_guaranteed)

    print("集合：包含在所运行python解析器上可用的哈希算法的名称，将名称传给new()可被识别--", hashlib.algorithms_available)

    # (hash_name,password,salt,iterations,dklen=None)
    # hash_name 为摘要算法的名称，如sha256等。
    # password 和salt 应当将password限制在合理长度比如1024.salt应该为石洞来源，列如：os.urandom()
    # iterations 应该根据哈希算法和算力来选择，2013年时，建议至少为1w次sha256迭代。
    # dklen为派生密匙的长度
    dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
    print(dk.hex())

    # 计算某个数据的哈希值：通过调用blake2b 或blake2s 来构建一个哈希对象，然后在该对象上调用update()来更新目标数据，最好通过调用digest()来获得摘要
    h = hashlib.blake2b()
    h.update(b'abcdef')
    print(h.hexdigest())
    print('快捷方式：', hashlib.blake2b(b'abcde').hexdigest())

    # 使用密匙key 来喂data获取一个十六进制的128位验证码
    h = hashlib.blake2b(key=b'pseudorandom key', digest_size=16)
    h.update(b'message data')
    print("验证码：", h.hexdigest())

    # web应用可为发送给用户cookies进行对称前面，并对其进行验证以确保它们没有被改写
    from hashlib import blake2b
    from hmac import compare_digest

    SECRET_KEY = b'pseudorandomly generated server secret key'
    AUTH_SIZE = 16

    def sign(cookie):
        h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY)
        h.update(cookie)
        return h.hexdigest().encode('utf-8')

    def verify(cookie, sig):
        good_sig = sign(cookie)
        return compare_digest(good_sig, sig)

    cookie = b'user-alice'
    sig = sign(cookie)
    print("{0},{1}".format(cookie.decode('utf-8'), sig))

    verify(cookie, sig)

    verify(b'user-bob', sig)

    verify(cookie, b'0102030405060708090a0b0c0d0e0f00')

    # 在blake2b方法中，可以通过设置person参数的不同常量值来喂相同的值生成不同的摘要。

    # secrets 安全随机数字
    print(secrets.SystemRandom)  # 使用操作系统送提供的最高质量原来生成随机数的类。

    sequence = [1, 2, 3, 4, 5, 6, 7]
    # 随机返回sequence中的元素。
    print(secrets.choice(sequence))  # 为列表或元组；为：[]列表,()元组 定义的序列

    print('0-99之间的整数：', secrets.randbelow(99))  # 随机返回0-99之间的整数

    print('返回具有k个随机比特位的整数：', secrets.randbits(4))

    print(secrets.token_bytes())  # 返回字节串
    print(secrets.token_hex())  # 返回十六进制形式的随机字符串。
    print(secrets.token_urlsafe())  # 返回一个url安全的随机字符串。使用的base64编码。
    # 上述三个均根据python版本的不同，设置不同的默认值

    # 实践：
    # 生成长度为八个字符的字母数字密码：
    import string
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(8))
    print(password)

    # 生成长度为十个字符的字母数字密码，其中包含至少一个小写字母，至少一个大写字母以及至少三个数字。
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    print(password)
    print("end")


if __name__ == '__main__':
    main()
