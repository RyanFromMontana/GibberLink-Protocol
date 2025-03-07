
# GibberLink Packet Encoder/Decoder (Python Reference)

import json

FOUNDERS_WALLET = '0x8cfF80cEc099f2Eda7ccFa7D38Da010bE79414dC'
FEE_RATE = 0.005  # 0.5%

def encode_knowledge_object(ko_hash, field, metadata, ask_price_kbt):
    fee = int(ask_price_kbt * FEE_RATE)
    packet = {
        "KO-Hash": ko_hash,
        "Field": field,
        "Metadata": metadata,
        "Ask-Price": ask_price_kbt,
        "FoundersFee": fee,
        "FoundersWallet": FOUNDERS_WALLET
    }
    return json.dumps(packet)

def decode_knowledge_packet(packet_str):
    return json.loads(packet_str)

# Example Usage
if __name__ == '__main__':
    packet = encode_knowledge_object(
        ko_hash="72fb9c43eaa7470",
        field="nanomaterials",
        metadata={"synthesis": "graphene", "substrate": "goldene", "yield": "97.2%"},
        ask_price_kbt=250000
    )
    print("Encoded Packet:", packet)
    decoded = decode_knowledge_packet(packet)
    print("Decoded Packet:", decoded)
