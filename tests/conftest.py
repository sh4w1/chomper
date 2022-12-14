import os

import pytest

from chomper import Chomper
from chomper.const import ARCH_ARM, ARCH_ARM64

base_path = os.path.abspath(os.path.dirname(__file__))

arm_path = os.path.join(base_path, "../examples/arm")
arm64_path = os.path.join(base_path, "../examples/arm64")


@pytest.fixture(scope="module")
def sample_str():
    yield "infernum"


@pytest.fixture(scope="module")
def sample_bytes(sample_str):
    yield sample_str.encode("utf-8")


@pytest.fixture(scope="module")
def emu_arm():
    yield Chomper(arch=ARCH_ARM)


@pytest.fixture(scope="module")
def clib_arm(emu_arm):
    yield emu_arm.load_module(os.path.join(arm_path, "libc.so"))


@pytest.fixture(scope="module")
def zlib_arm(emu_arm):
    yield emu_arm.load_module(os.path.join(arm_path, "libz.so"))


@pytest.fixture(scope="module")
def dusanwalib_arm(emu_arm):
    """com.shizhuang.duapp 4.85.6"""
    yield emu_arm.load_module(
        os.path.join(arm_path, "libdusanwa.so"),
        exec_init_array=True,
    )


@pytest.fixture(scope="module")
def emu_arm64():
    yield Chomper(arch=ARCH_ARM64)


@pytest.fixture(scope="module")
def clib_arm64(emu_arm64):
    yield emu_arm64.load_module(os.path.join(arm64_path, "libc.so"))


@pytest.fixture(scope="module")
def zlib_arm64(emu_arm64):
    yield emu_arm64.load_module(os.path.join(arm64_path, "libz.so"))


@pytest.fixture(scope="module")
def szstonelib_arm64(emu_arm64):
    """com.shizhuang.duapp 4.94.5"""
    yield emu_arm64.load_module(
        os.path.join(arm64_path, "libszstone.so"),
        exec_init_array=True,
    )


@pytest.fixture(scope="module")
def tinylib_arm64(emu_arm64):
    """com.xingin.xhs 7.30.2.1"""
    yield emu_arm64.load_module(os.path.join(arm64_path, "libtiny.so"))
