def Initialize(depfilename: str, outfilename: str) -> int: ...
def Clear() -> int: ...
def getFeature(feature_name: str, values: list) -> int: ...
def getFeatureInt(feature_name: str, values: list[int]) -> int: ...
def getFeatureDouble(feature_name: str, values: list[float]) -> int: ...
def getMapIntData(data_name: str) -> list[int]: ...
def getMapDoubleData(data_name: str) -> list[float]: ...
def setFeatureInt(feature_name: str, values: list[int]) -> int: ...
def setFeatureDouble(feature_name: str, values: list[float]) -> float: ...
def setFeatureString(feature_name: str, value: str) -> int: ...
def featuretype(feature_name: str) -> str: ...
def getgError() -> str: ...
def getFeatureNames(feature_names: list[str]) -> None: ...
