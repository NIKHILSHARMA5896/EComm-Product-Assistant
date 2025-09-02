import importlib.metadata as im
packages = [
    "langchain",
    "python-dotenv",
    "langchain-core",
]

for pkg in packages:
    try:
        version = im.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")