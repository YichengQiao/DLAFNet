_base_ = [
    './upernet_swin_tiny_patch4_window7_256x256_20k_vaihingen_pretrain_224x224_1K.py'
]
model = dict(
    pretrained='pretrain/swin_small_patch4_window7_224.pth',
    backbone=dict(
        depths=[2, 2, 18, 2]),
    decode_head=dict(
        in_channels=[96, 192, 384, 768],
        num_classes=6
    ),
    auxiliary_head=dict(
        in_channels=384,
        num_classes=6
    ))
