import importlib
import platform
import sys

packages = [
    "paho.mqtt.client",
    "pydantic",
    "numpy",
    "matplotlib",
    "pandas",
    "serial",
    "requests",
]

print("OS:", platform.platform())
print("Python:", sys.version.split()[0])

failed = []

for name in packages:
    try:
        importlib.import_module(name)
        print(f"[OK] {name}")
    except Exception as exc:
        failed.append(name)
        print(f"[FAIL] {name}: {exc}")

if failed:
    raise SystemExit(
        "Environment check failed: " + ", ".join(failed)
    )

print("Python environment: OK")
