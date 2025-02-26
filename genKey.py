from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
import base58


# 批量生成Hyperspace私钥的函数
def generate_private_keys(count):

    for i in range(1, count + 1):
        print(f"正在生成第 {i} 个密钥对...")

        # 生成Ed25519私钥
        private_key = ed25519.Ed25519PrivateKey.generate()

        # 获取原始私钥的字节
        raw_private = private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption()  # 不加密私钥
        )
        # 将二进制数据转换为Base58编码
        private_key_base58 = base58.b58encode(raw_private).decode('utf-8')
        # print(private_key_base58)
        # 保存到文件

        public_key = private_key.public_key()

        # 获取原始公钥的字节
        raw_public = public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )

        # 将二进制数据转换为Base58编码
        public_key_base58 = base58.b58encode(raw_public).decode('utf-8')
        print(private_key_base58,public_key_base58)


#
if __name__ == "__main__":
    generate_private_keys(1)